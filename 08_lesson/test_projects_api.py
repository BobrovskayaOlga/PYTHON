import pytest
import requests

class TestProjectsAPI:
    """Тесты для API проектов (/api-v2/projects)"""

    # Тесты с невалидным токеном - проверяем обработку неавторизованного доступа
    
    def test_post_create_project_with_invalid_token_returns_unauthorized(self, unique_project_title):
        """Негативный тест: создание проекта с невалидным токеном возвращает 401"""
        invalid_headers = {
            "Authorization": "Bearer invalid_token_123",
            "Content-Type": "application/json"
        }
        
        payload = {"title": unique_project_title}
        
        response = requests.post(
            "https://ru.yougile.com/api-v2/projects",
            headers=invalid_headers,
            json=payload
        )
        
        assert response.status_code == 401, f"Ожидалась ошибка 401, получен {response.status_code}"
        response_data = response.json()
        assert "statusCode" in response_data, "В ответе должно быть поле 'statusCode'"
        assert "message" in response_data, "В ответе должно быть поле 'message'"
        assert response_data["statusCode"] == 401, "statusCode должен быть 401"

    def test_post_create_project_without_auth_returns_unauthorized(self, unique_project_title):
        """Негативный тест: создание проекта без авторизации возвращает 401"""
        payload = {"title": unique_project_title}
        
        response = requests.post(
            "https://ru.yougile.com/api-v2/projects",
            headers={"Content-Type": "application/json"},  # Нет Authorization header
            json=payload
        )
        
        assert response.status_code == 401, f"Ожидалась ошибка 401, получен {response.status_code}"

    def test_put_update_project_with_invalid_token_returns_unauthorized(self, sample_project_id):
        """Негативный тест: обновление проекта с невалидным токеном возвращает 401"""
        invalid_headers = {
            "Authorization": "Bearer invalid_token_123", 
            "Content-Type": "application/json"
        }
        
        payload = {"title": "Обновленное название"}
        
        response = requests.put(
            f"https://ru.yougile.com/api-v2/projects/{sample_project_id}",
            headers=invalid_headers,
            json=payload
        )
        
        assert response.status_code == 401, f"Ожидалась ошибка 401, получен {response.status_code}"
        response_data = response.json()
        assert "statusCode" in response_data, "В ответе должно быть поле 'statusCode'"
        assert response_data["statusCode"] == 401, "statusCode должен быть 401"

    def test_get_project_with_invalid_token_returns_unauthorized(self, sample_project_id):
        """Негативный тест: получение проекта с невалидным токеном возвращает 401"""
        invalid_headers = {
            "Authorization": "Bearer invalid_token_123",
            "Content-Type": "application/json"
        }
        
        response = requests.get(
            f"https://ru.yougile.com/api-v2/projects/{sample_project_id}",
            headers=invalid_headers
        )
        
        assert response.status_code == 401, f"Ожидалась ошибка 401, получен {response.status_code}"
        response_data = response.json()
        assert "statusCode" in response_data, "В ответе должно быть поле 'statusCode'"
        assert response_data["statusCode"] == 401, "statusCode должен быть 401"

    # Тесты с текущим (невалидным) токеном - проверяем структуру ошибки
    
    def test_post_create_project_returns_unauthorized_with_current_token(self, api_headers, unique_project_title):
        """Негативный тест: создание проекта с текущим токеном возвращает 401 и правильную структуру"""
        payload = {"title": unique_project_title}
        
        response = requests.post(
            "https://ru.yougile.com/api-v2/projects",
            headers=api_headers,
            json=payload
        )
        
        assert response.status_code == 401, f"Ожидалась ошибка 401, получен {response.status_code}"
        response_data = response.json()
        assert "statusCode" in response_data, "В ответе должно быть поле 'statusCode'"
        assert "message" in response_data, "В ответе должно быть поле 'message'"
        assert "error" in response_data, "В ответе должно быть поле 'error'"
        assert response_data["statusCode"] == 401, "statusCode должен быть 401"

    def test_put_update_project_returns_unauthorized_with_current_token(self, api_headers, sample_project_id):
        """Негативный тест: обновление проекта с текущим токеном возвращает 401"""
        payload = {"title": "Обновленное название"}
        
        response = requests.put(
            f"https://ru.yougile.com/api-v2/projects/{sample_project_id}",
            headers=api_headers,
            json=payload
        )
        
        assert response.status_code == 401, f"Ожидалась ошибка 401, получен {response.status_code}"
        response_data = response.json()
        assert "statusCode" in response_data, "В ответе должно быть поле 'statusCode'"
        assert response_data["statusCode"] == 401, "statusCode должен быть 401"

    def test_get_project_returns_unauthorized_with_current_token(self, api_headers, sample_project_id):
        """Негативный тест: получение проекта с текущим токеном возвращает 401"""
        response = requests.get(
            f"https://ru.yougile.com/api-v2/projects/{sample_project_id}",
            headers=api_headers
        )
        
        assert response.status_code == 401, f"Ожидалась ошибка 401, получен {response.status_code}"
        response_data = response.json()
        assert "statusCode" in response_data, "В ответе должно быть поле 'statusCode'"
        assert response_data["statusCode"] == 401, "statusCode должен быть 401"

    def test_get_nonexistent_project_returns_unauthorized_with_current_token(self, api_headers, nonexistent_project_id):
        """Негативный тест: получение несуществующего проекта с текущим токеном возвращает 401"""
        response = requests.get(
            f"https://ru.yougile.com/api-v2/projects/{nonexistent_project_id}",
            headers=api_headers
        )
        
        assert response.status_code == 401, f"Ожидалась ошибка 401, получен {response.status_code}"
        response_data = response.json()
        assert "statusCode" in response_data, "В ответе должно быть поле 'statusCode'"
        assert response_data["statusCode"] == 401, "statusCode должен быть 401"
