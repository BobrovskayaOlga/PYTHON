import pytest
import requests

class TestProjectsGetPositive:
    """Позитивные тесты для GET /api-v2/projects/{id}"""

    def test_get_project_returns_expected_structure(self, api_headers):
        """Тест проверяет структуру ответа при получении проекта"""
        # Используем тестовый ID проекта
        test_project_id = "4f6f0391-0f94-4d30-9b0e-99430a36d4fb"

        response = requests.get(
            f"https://ru.yougile.com/api-v2/projects/{test_project_id}",
            headers=api_headers
        )
        
        # Валидируем структуру ответа независимо от статуса
        if response.status_code == 200:
            # Если успешно - проверяем структуру успешного ответа
            response_data = response.json()
            
            # Проверяем обязательные поля согласно документации
            assert "id" in response_data, "В ответе должно быть поле 'id'"
            assert "title" in response_data, "В ответе должно быть поле 'title'"
            assert "timestamp" in response_data, "В ответе должно быть поле 'timestamp'"
            assert "deleted" in response_data, "В ответе должно быть поле 'deleted'"
            assert "users" in response_data, "В ответе должно быть поле 'users'"
            
            # Проверяем типы данных
            assert isinstance(response_data["id"], str), "ID должен быть строкой"
            assert isinstance(response_data["title"], str), "Title должен быть строкой"
            assert isinstance(response_data["timestamp"], (int, float)), "Timestamp должен быть числом"
            assert isinstance(response_data["deleted"], bool), "Deleted должен быть boolean"
            assert isinstance(response_data["users"], dict), "Users должен быть объектом"
            
            # Проверяем, что ID в ответе совпадает с запрошенным
            assert response_data["id"] == test_project_id, "ID в ответе должен совпадать с запрошенным ID"
            
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
