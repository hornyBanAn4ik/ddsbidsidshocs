from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
import time
import random

# Налаштування Edge
options = webdriver.EdgeOptions()
options.add_argument("--headless")  # Без графічного інтерфейсу
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Запускаємо Edge WebDriver
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)

# URL сайту
URL = "https://disflip.com/server/1334611206421479557"  # Замінити на сайт

# Функція для бампа
def bump():
    driver.get(URL)
    time.sleep(random.randint(5, 10))  # Чекаємо завантаження сторінки

    try:
        # Знайти кнопку
        bump_button = driver.find_element(By.XPATH, '//*[@id="upButton"]') 
        bump_button.click()
        print("✅ Сервер успішно пробампано!")
    except Exception as e:
        print("❌ Помилка під час бампа:", e)

# Головний цикл
while True:
    bump()

    # Випадковий інтервал від 4 годин 1 хв до 4 годин 10 хв
    delay = 4 * 60 * 60 + random.randint(60, 600)
    print(f"⏳ Наступний бамп через {delay // 60} хвилин")
    
    time.sleep(delay)
