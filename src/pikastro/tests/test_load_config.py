from pikastro.app import config


def test_load_config():
    cfg = config.load_config("./tests/configs/local.yaml")
    assert cfg.x_google_backend == "http://localhost:8080"
