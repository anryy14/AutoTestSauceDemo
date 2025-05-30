import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Тестовые данные: логин, пароль, ожидаемый результат
# expected: success = вход, blocked = заблокирован, invalid = ошибка логина, empty = не введено
test_data = [
    ("standard_user", "secret_sauce", "success"),
    ("locked_out_user", "secret_sauce", "blocked"),
    ("problem_user", "secret_sauce", "success"),
    ("performance_glitch_user", "secret_sauce", "success"),
    ("error_user", "secret_sauce", "success"),
    ("visual_user", "secret_sauce", "success"),
    ("", "", "empty"),
    ("test", "123", "invalid")
]

@pytest.mark.parametrize("username,password,expected", test_data)
def test_login_various_users(username, password, expected):
    options = Options()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get("https://www.saucedemo.com/")

        # Ввод данных
        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()

        time.sleep(2)  # Ожидание загрузки

        if expected == "success":
            assert driver.find_element(By.CLASS_NAME, "inventory_list").is_displayed()
        else:
            error_container = driver.find_element(By.CLASS_NAME, "error-message-container")
            error_text = error_container.text.lower()

            if expected == "blocked":
                assert "sorry, this user has been locked out" in error_text
            elif expected == "invalid":
                assert "do not match any user" in error_text
            elif expected == "empty":
                assert "username is required" in error_text

    finally:
        driver.quit()

