import pytest
import requests

# Базовые настройки
BASE_URL = "https://ru.yougile.com"

@pytest.fixture
def api_headers():
    """Заголовки для API запросов - используем статический токен"""
    return {
        "Authorization": "Bearer VlFRT72Ym55u-LAaVY9jzKpaQcNpaBVPS8RjQWyKpB3QV07ec0iDALNEiLsMt4JY",
        "Content-Type": "application/json"
    }

@pytest.fixture
def unique_project_title():
    """Генерация уникального названия проекта"""
    import uuid
    return f"Тестовый проект {uuid.uuid4().hex[:8]}"

@pytest.fixture
def sample_project_id():
    """Пример ID проекта для тестов (в реальности нужно использовать существующий ID)"""
    return "4f6f0391-0f94-4d30-9b0e-99430a36d4fb"
