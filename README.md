# Selenium Test Project

Этот проект включает тесты для веб-приложения с использованием библиотеки Selenium и инструмента тестирования pytest. Тесты проверяют логику входа различных пользователей на сайте [Sauce Demo](https://www.saucedemo.com/).

## Установка

Чтобы запустить этот проект, выполните следующие шаги:

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/yourusername/yourproject.git
Перейдите в директорию проекта:

bash
Copy code
cd yourproject
Установите зависимости:

text
Copy code
pip install -r requirements.txt
Использование
Для запуска тестов используйте команду:

text
Copy code
pytest
Вы можете добавлять флаг -v для получения более подробной информации о тестах:

text
Copy code
pytest -v
Структура данных
Тестовые данные содержат логины, пароли и ожидаемые результаты:

success: вход выполнен успешно
blocked: пользователь заблокирован
invalid: ошибка логина
empty: поля пусты
Лицензия
Этот проект лицензирован под MIT License.

shell
Copy code

### 2. requirements.txt
В этом файле будут указаны зависимости, которые необходимы для работы проекта.

pytest
selenium
webdriver-manager

markdown
Copy code

### 3. .gitignore
Файл `.gitignore` помогает исключить лишние файлы из системы контроля версий Git.
