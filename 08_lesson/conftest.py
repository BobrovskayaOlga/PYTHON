import pytest
import requests
import uuid

# Базовые настройки
BASE_URL = "https://ru.yougile.com"

@pytest.fixture
def api_headers():
    """Заголовки для API запросов"""
    return {
        "Authorization": "Bearer VlFRT72Ym55u-LAaVY9jzKpaQcNpaBVPS8RjQWyKpB3QV07ec0iDALNEiLsMt4JY",
        "Content-Type": "application/json"
    }

@pytest.fixture
def unique_project_title():
    """Генерация уникального названия проекта"""
    return f"Тестовый проект {uuid.uuid4().hex[:8]}"

@pytest.fixture
def sample_project_id():
    """Пример ID проекта для тестов"""
    return "4f6f0391-0f94-4d30-9b0e-99430a36d4fb"

@pytest.fixture
def nonexistent_project_id():
    """Несуществующий ID проекта для негативных тестов"""
    return "00000000-0000-0000-0000-000000000000"

@pytest.fixture
def sample_users_data():
    """Пример данных пользователей для тестов"""
    return {
        "4902b994-b806-4af4-acec-018ea5ea6468": "worker",
        "8aeaeb9d-f94e-4c66-96d3-eb8d96fe7018": "ee88efd5-5cb2-41a0-9ea2-295da25863d4"
    }
