from config import get_openai_model, is_openai_configured


def test_missing_api_key_is_not_configured(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    assert is_openai_configured() is False


def test_blank_api_key_is_not_configured(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "   ")
    assert is_openai_configured() is False


def test_present_api_key_is_detected(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "test-placeholder-not-a-real-key")
    assert is_openai_configured() is True


def test_model_is_empty_when_not_configured(monkeypatch):
    monkeypatch.delenv("OPENAI_MODEL", raising=False)
    assert get_openai_model() == ""


def test_model_is_read_from_environment(monkeypatch):
    monkeypatch.setenv("OPENAI_MODEL", "example-test-model")
    assert get_openai_model() == "example-test-model"