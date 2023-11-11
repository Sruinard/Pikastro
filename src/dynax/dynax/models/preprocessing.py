

def preprocessing_fn(inputs):
  """tf.transform's callback function for preprocessing inputs.

  Args:
    inputs: map from feature keys to raw not-yet-transformed features.

  Returns:
    Map from string feature key to transformed feature operations.
  """
  outputs = {}
  for key in _DENSE_FLOAT_FEATURE_KEYS:
    # If sparse make it dense, setting nan's to 0 or '', and apply zscore.
    outputs[_transformed_name(key)] = transform.scale_to_z_score(
        _fill_in_missing(inputs[key]))

  for key in _VOCAB_FEATURE_KEYS:
    # Build a vocabulary for this feature.
    outputs[_transformed_name(
        key)] = transform.compute_and_apply_vocabulary(
            _fill_in_missing(inputs[key]),
            top_k=_VOCAB_SIZE,
            num_oov_buckets=_OOV_SIZE)

  for key in _BUCKET_FEATURE_KEYS:
    outputs[_transformed_name(key)] = transform.bucketize(
        _fill_in_missing(inputs[key]), _FEATURE_BUCKET_COUNT)

  for key in _CATEGORICAL_FEATURE_KEYS:
    outputs[_transformed_name(key)] = _fill_in_missing(inputs[key])

  # Was this passenger a big tipper?
  taxi_fare = _fill_in_missing(inputs[_FARE_KEY])
  tips = _fill_in_missing(inputs[_LABEL_KEY])
  outputs[_transformed_name(_LABEL_KEY)] = tf.where(
      tf.is_nan(taxi_fare),
      tf.cast(tf.zeros_like(taxi_fare), tf.int64),
      # Test if the tip was > 20% of the fare.
      tf.cast(
          tf.greater(tips, tf.multiply(taxi_fare, tf.constant(0.2))), tf.int64))

  return outputs