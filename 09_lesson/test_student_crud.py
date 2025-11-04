import pytest
from sqlalchemy.exc import IntegrityError
from models import Student

class TestStudentCRUD:
    """Тесты для работы со студентами в PostgreSQL 17 QA"""
    
    def test_create_student(self, db_session):
        """Тест создания нового студента"""
        print("🎯 Тест 1: Создание студента")
        
        # Arrange
        student_data = {
            "name": "Иван Иванов",
            "email": "ivan.ivanov@example.com",
            "course": "Computer Science"
        }
        
        # Act
        new_student = Student(**student_data)
        db_session.add(new_student)
        db_session.commit()
        db_session.refresh(new_student)
        
        # Assert
        assert new_student.id is not None
        assert new_student.name == student_data["name"]
        assert new_student.email == student_data["email"]
        assert new_student.course == student_data["course"]
        
        # Проверяем в БД
        saved_student = db_session.query(Student).filter_by(id=new_student.id).first()
        assert saved_student is not None
        assert saved_student.name == student_data["name"]
        
        print(f"✅ Создан студент: {new_student}")
    
    def test_update_student(self, db_session):
        """Тест обновления данных студента"""
        print("🎯 Тест 2: Обновление студента")
        
        # Arrange - создаем студента
        student_data = {
            "name": "Иван Иванов",
            "email": "ivan.update@example.com",
            "course": "Computer Science"
        }
        student = Student(**student_data)
        db_session.add(student)
        db_session.commit()
        db_session.refresh(student)
        
        # Act - обновляем данные
        student.name = "Петр Петров"
        student.course = "Mathematics"
        db_session.commit()
        db_session.refresh(student)
        
        # Assert
        assert student.name == "Петр Петров"
        assert student.course == "Mathematics"
        assert student.email == "ivan.update@example.com"
        
        print(f"✅ Обновлен студент: {student}")
    
    def test_delete_student(self, db_session):
        """Тест удаления студента"""
        print("🎯 Тест 3: Удаление студента")
        
        # Arrange - создаем студента
        student_data = {
            "name": "Студент для удаления",
            "email": "delete.me@example.com",
            "course": "Temporary Course"
        }
        student = Student(**student_data)
        db_session.add(student)
        db_session.commit()
        db_session.refresh(student)
        
        student_id = student.id
        
        # Act - удаляем студента
        db_session.delete(student)
        db_session.commit()
        
        # Assert - проверяем, что студент удален
        deleted_student = db_session.query(Student).filter_by(id=student_id).first()
        assert deleted_student is None
        
        print("✅ Студент успешно удален")

    def test_unique_email_constraint(self, db_session):
        """Тест уникальности email"""
        print("🎯 Тест 4: Проверка уникальности email")
        
        # Arrange - создаем первого студента
        student1 = Student(
            name="Первый Студент",
            email="unique@example.com",
            course="Course 1"
        )
        db_session.add(student1)
        db_session.commit()
        
        # Act & Assert - пытаемся создать второго студента с тем же email
        student2 = Student(
            name="Второй Студент", 
            email="unique@example.com",  # тот же email
            course="Course 2"
        )
        db_session.add(student2)
        
        # Ожидаем ошибку уникальности
        with pytest.raises(IntegrityError):
            db_session.commit()
        
        # Откатываем невалидную транзакцию
        db_session.rollback()
        
        print("✅ Тест уникальности email пройден")
