from tfx.components.example_gen.base_example_gen_executor import BaseExampleGenExecutor
import json
import tensorflow as tf
from typing import TypedDict
import tfx.v1 as tfx
from tfx.dsl.component.experimental.decorators import component
from tfx.types.standard_artifacts import Examples
from tfx.dsl.component.experimental.annotations import OutputArtifact, Parameter
import apache_beam as beam
import os
from typing import Any, Dict
import glob
from  dataclasses import dataclass

from absl import logging
import apache_beam as beam
import tensorflow as tf

from tfx.components.example_gen import utils
from tfx.components.example_gen.base_example_gen_executor import BaseExampleGenExecutor
from tfx.types import standard_component_specs
import pandas as pd


def _bytes_feature(value):
  """Returns a bytes_list from a string / byte."""
  if isinstance(value, type(tf.constant(0))):
    value = value.numpy() # BytesList won't unpack a string from an EagerTensor.
  return tf.train.Feature(bytes_list=tf.train.BytesList(value=value))

def _float_feature(value):
  """Returns a float_list from a float / double."""
  return tf.train.Feature(float_list=tf.train.FloatList(value=value))

def _int64_feature(value):
  """Returns an int64_list from a bool / enum / int / uint."""
  return tf.train.Feature(int64_list=tf.train.Int64List(value=value))

def get_feature(tensor, is_context_feature):
  dtype = tensor.dtype
  feature = []
  feature_values = tf.reshape(tensor, [-1]).numpy().tolist()
  # select only the first value if it is a context feature as all values will be the same
  if is_context_feature:
    feature_values = feature_values[:1] #keep list structure
  feature.extend(feature_values)

  train_feature = tf.train.Feature()

  if dtype == tf.string:
    train_feature = _bytes_feature(feature)
  elif dtype == tf.float32:
    train_feature = _float_feature(feature)
  elif dtype == tf.int64:
    train_feature = _int64_feature(feature)
  elif dtype == tf.int32:
    feature = tf.cast(feature, tf.int64)
    train_feature = _int64_feature(feature)
  else:
    raise ValueError("Feature type not supported")
  return train_feature

def to_sequence_example(batch, context_features, sequence_features):
    """Converts a batch of data to SequenceExample proto."""
    context_feature_dict = {}
    sequence_feature_dict = {}
    for feature_name, feature_tensor in batch.items():
        if feature_name in context_features:
            context_feature_dict[feature_name] = get_feature(feature_tensor, True)
        elif feature_name in sequence_features:
            sequence_feature_dict[feature_name] = tf.train.FeatureList(feature=[get_feature(feature_tensor, False)])
        else:
            raise ValueError("Feature name not recognized")
    
    
    return tf.train.SequenceExample(
        context=tf.train.Features(feature=context_feature_dict),
        feature_lists=tf.train.FeatureLists(feature_list=sequence_feature_dict))#.SerializeToString()

def csv_to_timeseries(src, history_size, target_size, shift, stride, context_features, sequence_features, max_items_to_process):
  ds: tf.data.Dataset = tf.data.experimental.make_csv_dataset(src, batch_size=1, shuffle=False)
  ds = ds.window(history_size + target_size, shift=shift, stride=stride, drop_remainder=True)
  ds = ds.flat_map(lambda x: tf.data.Dataset.zip({k: v.batch(history_size + target_size) for k, v in x.items()}))
  for batch in ds.take(max_items_to_process):
    yield to_sequence_example(batch, context_features, sequence_features)

@dataclass
class TimeseriesConfig:
  history_size: int
  target_size: int
  shift: int
  stride: int
  max_items_to_process: int
  context_features: list[str]
  sequence_features: list[str]
  
  @classmethod
  def from_dict(cls, d):
    return cls(**d)

@beam.ptransform_fn
@beam.typehints.with_input_types(beam.Pipeline)
@beam.typehints.with_output_types(tf.train.SequenceExample)
def _csv_to_sequence_examples(pipeline: beam.Pipeline, exec_properties: Dict[str, Any], split_pattern: str):
    """
    Component takes three steps.
    1. list files
    2. turn into tf.data and window
    3. write out as tfrecords
    """
    input_base_uri = exec_properties[standard_component_specs.INPUT_BASE_KEY]
    file_pattern = os.path.join(input_base_uri, split_pattern)
    logging.info('Processing input files data %s to TFSequenceExample.', file_pattern)
    files = glob.glob(file_pattern)
    print(files)

    print(exec_properties["input_config"])
    print(exec_properties["custom_config"])
    # config = TimeseriesConfig.from_dict(exec_properties["input_config"]["config"])
    logging.info('Received config %s.', json.dumps(exec_properties["custom_config"]))
    config = json.loads(exec_properties["custom_config"])
    config = TimeseriesConfig.from_dict(config)

    return (pipeline
        | "Create file path" >> beam.Create(files)
        | 'ToTFExample' >> beam.FlatMap(lambda x: csv_to_timeseries(x, config.history_size, config.target_size, config.shift, config.stride, config.context_features, config.sequence_features, config.max_items_to_process)))



class Executor(BaseExampleGenExecutor):
    """Generic TFX CSV example gen executor."""

    def GetInputSourceToExamplePTransform(self) -> beam.PTransform:
        """Returns PTransform for CSV to TF examples."""
        return _csv_to_sequence_examples