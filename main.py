from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Инициализация веб-драйвера
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Открытие главной страницы
    driver.get("https://chicago-pizza.ru/")
    time.sleep(2)  # Ждем загрузки страницы

    # Ввод запроса в поле поиска
    search_input = driver.find_element(By.CSS_SELECTOR, "input[type='search']")
    search_input.send_keys("пепперони")

    # Нажатие кнопки "Search"
    search_button = driver.find_element(By.XPATH, "//button[@aria-label='Поиск']")
    search_button.click()
    time.sleep(2)  # Ждем загрузки результатов

    # Проверка, что результаты поиска соответствуют ожидаемым
    results = driver.find_elements(By.CLASS_NAME, "line-clamp-3")
    assert any("пепперони" in result.text.lower() for result in results), "Товар не найден"

    # Добавление выбранного товара в корзину
    add_to_cart_button = driver.find_element(By.XPATH,
                                             "//div[contains(text(), 'Римская пицца пепперони')]//following-sibling::div//button[@aria-label='Добавить']")
    add_to_cart_button.click()
    time.sleep(2)  # Ждем, чтобы товар был добавлен в корзину

    # Проверка наличия товара в корзине
    cart_item_name = driver.find_element(By.XPATH, "//div[contains(text(), 'Римская пицца пепперони')]")
    assert cart_item_name.is_displayed(), "Товар не найден в корзине"

    print("Тест пройден успешно!")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # Закрытие браузера
    driver.quit()
