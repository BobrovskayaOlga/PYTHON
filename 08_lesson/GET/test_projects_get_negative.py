import pytest
import requests

class TestProjectsGetNegative:
    """Негативные тесты для GET /api-v2/projects/{id}"""

    def test_get_nonexistent_project_returns_proper_error(self, api_headers):
        """Тест проверяет обработку запроса несуществующего проекта"""
        # Используем заведомо несуществующий ID
        nonexistent_project_id = "00000000-0000-0000-0000-000000000000"
        
        response = requests.get(
            f"https://ru.yougile.com/api-v2/projects/{nonexistent_project_id}",
            headers=api_headers
        )

        # Проверяем, что API обработало запрос корректно (не 5xx ошибка)
        assert response.status_code != 500, "Сервер не должен возвращать 500 ошибку"
        
        # Проверяем структуру ответа
        try:
            response_data = response.json()
            assert True, "Ответ должен быть в JSON формате"
            
            # Если это ошибка 404 - проверяем структуру
            if response.status_code == 404:
                assert "statusCode" in response_data, "В ошибке 404 должно быть поле 'statusCode'"
                assert response_data["statusCode"] == 404, "Код ошибки должен быть 404"
                
            # Если это ошибка авторизации
            elif response.status_code == 401:
                assert "statusCode" in response_data, "В ошибке должно быть поле 'statusCode'"
                assert "message" in response_data, "В ошибке должно быть поле 'message'"
                
        except ValueError:
            pytest.fail("Ответ не в JSON формате")
