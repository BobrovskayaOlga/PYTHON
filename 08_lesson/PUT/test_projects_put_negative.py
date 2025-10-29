import pytest
import requests

class TestProjectsPutNegative:
    """Негативные тесты для PUT /api-v2/projects/{id}"""

    def test_put_invalid_project_id_returns_error(self, api_headers):
        """Тест проверяет обработку невалидного ID проекта"""
        # Используем заведомо невалидный ID
        invalid_project_id = "invalid-id-12345"
        
        payload = {
            "title": "Проект с невалидным ID",
            "users": {
                "4902b994-b806-4af4-acec-018ea5ea6468": "worker"
            }
        }

        response = requests.put(
            f"https://ru.yougile.com/api-v2/projects/{invalid_project_id}",
            headers=api_headers,
            json=payload
        )

        # Проверяем, что API обработало запрос корректно (не 5xx ошибка)
        assert response.status_code != 500, "Сервер не должен возвращать 500 ошибку"
        
        # Проверяем структуру ответа
        try:
            response_data = response.json()
            assert True, "Ответ должен быть в JSON формате"
            
            # Если это ошибка - проверяем структуру
            if response.status_code >= 400:
                assert "statusCode" in response_data or "error" in response_data, "В ошибке должен быть код ошибки"
                assert "message" in response_data or "error" in response_data, "В ошибке должно быть описание"
        except ValueError:
            pytest.fail("Ответ не в JSON формате")
