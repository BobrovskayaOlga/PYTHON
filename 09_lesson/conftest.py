import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from models import Base

# Настройки подключения к БД QA
DB_CONFIG = {
    "host": "localhost",
    "port": "5432", 
    "database": "QA",
    "user": "postgres",
    "password": "admin"
}

@pytest.fixture(scope="session")
def engine():
    """Фикстура для создания движка БД"""
    
    # Формируем URL для подключения
    db_url = f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
    
    print("🔄 Подключаемся к PostgreSQL 17...")
    print(f"База данных: {DB_CONFIG['database']}")
    
    try:
        engine = create_engine(db_url)
        
        # Проверяем подключение
        with engine.connect() as conn:
            result = conn.execute(text("SELECT version();"))
            version = result.fetchone()[0]
            print(f"✅ Подключение успешно: {version.split(',')[0]}")
        
        # Создаем таблицы
        print("🔄 Создаем таблицы...")
        Base.metadata.create_all(engine)
        print("✅ Таблицы созданы")
        
        yield engine
        
    except Exception as e:
        print(f"❌ Ошибка подключения: {e}")
        pytest.fail(f"Не удалось подключиться к базе данных: {e}")
    
    finally:
        # Удаляем таблицы после всех тестов
        if 'engine' in locals():
            print("🔄 Очищаем базу данных...")
            Base.metadata.drop_all(engine)
            engine.dispose()
            print("✅ Очистка завершена")

@pytest.fixture(scope="function")
def db_session(engine):
    """Фикстура для создания сессии БД"""
    Session = sessionmaker(bind=engine)
    session = Session()
    
    yield session
    
    # Очищаем данные после каждого теста
    try:
        session.rollback()
        # Удаляем все данные из таблицы student
        session.execute(text("TRUNCATE TABLE student RESTART IDENTITY CASCADE;"))
        session.commit()
        print("🧹 Данные очищены после теста")
    except Exception as e:
        print(f"⚠️ Ошибка при очистке данных: {e}")
        session.rollback()
    finally:
        session.close()
