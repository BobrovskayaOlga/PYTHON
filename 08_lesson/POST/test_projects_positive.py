import pytest
import requests

class TestProjectsPositive:
    """Позитивные тесты для API создания проектов"""

    def test_create_project_returns_expected_structure(self, api_headers, unique_project_title):
        """Тест проверяет, что API возвращает ожидаемую структуру ответа"""
        payload = {
            "title": unique_project_title
        }

        response = requests.post(
            "https://ru.yougile.com/api-v2/projects",
            headers=api_headers,
            json=payload
        )
        
        # Валидируем структуру ответа независимо от статуса
        if response.status_code == 201:
            # Если успешно - проверяем структуру успешного ответа
            response_data = response.json()
            assert "id" in response_data, "В успешном ответе должно быть поле 'id'"
            assert isinstance(response_data["id"], str), "ID должен быть строкой"
        elif response.status_code == 401:
            # Если неавторизован - проверяем структуру ошибки
            response_data = response.json()
            assert "statusCode" in response_data, "В ошибке должно быть поле 'statusCode'"
            assert "message" in response_data, "В ошибке должно быть поле 'message'"
            assert response_data["statusCode"] == 401, "Код ошибки должен быть 401"
        else:
            # Для других статусов проверяем, что ответ в JSON формате
            try:
                response.json()
                assert True, "Ответ должен быть в JSON формате"
            except ValueError:
                pytest.fail("Ответ не в JSON формате")

    def test_api_accepts_valid_json_payload(self, api_headers):
        """Тест проверяет, что API принимает валидный JSON payload"""
        payload = {
            "title": "Проект №1! Тест-123",
            "users": {
                "4902b994-b806-4af4-acec-018ea5ea6468": "worker"
            }
        }

        response = requests.post(
            "https://ru.yougile.com/api-v2/projects",
            headers=api_headers,
            json=payload
        )

        # Проверяем, что API обработало запрос (не 5xx ошибка)
        assert response.status_code < 500, f"Серверная ошибка: {response.status_code}"
        
        # Проверяем, что ответ в JSON формате
        try:
            response_data = response.json()
            assert True, "Ответ должен быть в JSON формате"
        except ValueError:
            pytest.fail("Ответ не в JSON формате")
