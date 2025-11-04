import sys
import os

# Добавляем текущую директорию в путь
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

print("📂 Содержимое директории:")
for file in os.listdir('.'):
    if file.endswith('.py'):
        print(f"  - {file}")

print("\n🔄 Попытка импорта...")
try:
    from formpage import FormPage
    print("✅ FormPage импортирован успешно!")
    
    # Проверяем BasePage
    from BasePage import BasePage
    print("✅ BasePage импортирован успешно!")
    
    # Проверяем Selenium
    from selenium import webdriver
    print("✅ Selenium импортирован успешно!")
    
except ImportError as e:
    print(f"❌ Ошибка импорта: {e}")
