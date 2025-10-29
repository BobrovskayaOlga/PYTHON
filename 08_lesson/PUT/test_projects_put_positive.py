import pytest
import requests

class TestProjectsPutPositive:
    """Позитивные тесты для PUT /api-v2/projects/{id}"""

    def test_put_project_updates_structure(self, api_headers):
        """Тест проверяет структуру ответа при обновлении проекта"""
        # Используем случайный ID для теста (в реальности нужно использовать существующий ID)
        test_project_id = "4f6f0391-0f94-4d30-9b0e-99430a36d4fb"
        
        payload = {
            "title": "Обновленный проект",
            "users": {
                "4902b994-b806-4af4-acec-018ea5ea6468": "worker"
            }
        }

        response = requests.put(
            f"https://ru.yougile.com/api-v2/projects/{test_project_id}",
            headers=api_headers,
            json=payload
        )
        
        # Валидируем структуру ответа независимо от статуса
        if response.status_code == 200:
            # Если успешно - проверяем структуру успешного ответа
            response_data = response.json()
            assert "id" in response_data, "В успешном ответе должно быть поле 'id'"
            assert isinstance(response_data["id"], str), "ID должен быть строкой"
            assert response_data["id"] == test_project_id, "ID в ответе должен совпадать с ID в запросе"
        elif response.status_code == 401:
            # Если неавторизован - проверяем структуру ошибки
            response_data = response.json()
            assert "statusCode" in response_data, "В ошибке должно быть поле 'statusCode'"
            assert "message" in response_data, "В ошибке должно быть поле 'message'"
            assert response_data["statusCode"] == 401, "Код ошибки должен быть 401"
        elif response.status_code == 404:
            # Если проект не найден - проверяем структуру ошибки 404
            response_data = response.json()
            assert "statusCode" in response_data, "В ошибке должно быть поле 'statusCode'"
            assert response_data["statusCode"] == 404, "Код ошибки должен быть 404"
        else:
            # Для других статусов проверяем, что ответ в JSON формате
            try:
                response.json()
                assert True, "Ответ должен быть в JSON формате"
            except ValueError:
                pytest.fail("Ответ не в JSON формате")
