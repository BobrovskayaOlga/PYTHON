import pytest
import requests

@pytest.fixture
def api_headers():
    return {
        "Authorization": "Bearer VlFRT72Ym55u-LAaVY9jzKpaQcNpaBVPS8RjQWyKpB3QV07ec0iDALNEiLsMt4JY",
        "Content-Type": "application/json"
    }

@pytest.fixture
def base_url():
    return "https://ru.yougile.com/api-v2"

@pytest.fixture
def sample_project_id():
    return "4f6f0391-0f94-4d30-9b0e-99430a36d4fb"
