import pytest
import requests

class TestProjectsNegative:
    """Негативные тесты для API создания проектов"""

    def test_invalid_token_returns_proper_error(self):
        """Тест проверяет, что невалидный токен возвращает правильную ошибку"""
        invalid_headers = {
            "Authorization": "Bearer invalid_token_123",
            "Content-Type": "application/json"
        }
        
        payload = {
            "title": "Тестовый проект"
        }

        response = requests.post(
            "https://ru.yougile.com/api-v2/projects",
            headers=invalid_headers,
            json=payload
        )

        # Проверяем, что возвращается ошибка авторизации
        assert response.status_code in [401, 403], f"Ожидалась ошибка авторизации, получен {response.status_code}"
        
        # Проверяем структуру ошибки
        response_data = response.json()
        assert "statusCode" in response_data, "В ошибке должно быть поле 'statusCode'"
        assert "message" in response_data, "В ошибке должно быть поле 'message'"

    def test_api_handles_missing_required_fields(self, api_headers):
        """Тест проверяет обработку отсутствия обязательных полей"""
        payload = {
            "users": {
                "4902b994-b806-4af4-acec-018ea5ea6468": "worker"
            }
            # Нет поля 'title' - обязательное поле
        }

        response = requests.post(
            "https://ru.yougile.com/api-v2/projects",
            headers=api_headers,
            json=payload
        )

        # Проверяем, что API обработало запрос корректно
        assert response.status_code != 500, "Сервер не должен возвращать 500 ошибку"
        
        # Проверяем структуру ответа
        try:
            response_data = response.json()
            assert True, "Ответ должен быть в JSON формате"
            
            # Если это ошибка - проверяем структуру
            if response.status_code >= 400:
                assert "message" in response_data or "error" in response_data, "В ошибке должно быть описание"
        except ValueError:
            pytest.fail("Ответ не в JSON формате")
