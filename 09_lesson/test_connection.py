from sqlalchemy import create_engine, text

# Настройки подключения к вашей БД QA
DB_CONFIG = {
    "host": "localhost",
    "port": "5432", 
    "database": "QA",
    "user": "postgres",
    "password": "admin"
}

def test_connection():
    """Проверка подключения к базе данных QA"""
    try:
        # Формируем URL для подключения
        db_url = f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
        
        engine = create_engine(db_url)
        
        # Пробуем подключиться
        with engine.connect() as conn:
            result = conn.execute(text("SELECT version();"))
            version = result.fetchone()[0]
            print(f"✅ Успешное подключение к PostgreSQL!")
            print(f"Версия: {version}")
            
            # Проверяем, что база данных QA
            result = conn.execute(text("SELECT current_database();"))
            db_name = result.fetchone()[0]
            print(f"База данных: {db_name}")
            
        # Убираем return для pytest
        assert True
        
    except Exception as e:
        print(f"❌ Ошибка подключения: {e}")
        assert False, f"Не удалось подключиться: {e}"

if __name__ == "__main__":
    test_connection()
