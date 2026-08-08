# FunPayPlus

Неофициальный Python клиент для FunPay

ВНИМАНИЕ: Только для образовательных целей! Проект создан для обучения и демонстрации навыков. Используйте на свой страх и риск.


## Установка

pip install requests beautifulsoup4

Или склонируйте репозиторий:

git clone https://github.com/yourusername/funpayplus.git
cd funpayplus
pip install -r requirements.txt


## Быстрый старт

from funpayplus import Account

# Создаем объект аккаунта
account = Account("ваш_golden_key", "ваш_user_agent")

# Получаем все данные
account.get()

# Выводим информацию
print(account)


## Свойства аккаунта

После вызова метода get(), становятся доступны следующие свойства:

- username (str) - Имя пользователя
- balance (float) - Текущий баланс в рублях
- active_sell (int) - Количество активных продаж
- active_buy (int) - Количество активных покупок
- active_message (int) - Количество непрочитанных сообщений (из профиля)
- rating (float) - Рейтинг пользователя (0.0 - 5.0)
- data (str) - Дата регистрации и другая информация
- id (int) - ID пользователя
- unread (int) - Количество непрочитанных сообщений (из чата)


## Методы

### __init__(token: str, user_agent: str = "")

Создает новый экземпляр аккаунта.

Параметры:
- token (str) - Golden key из кук FunPay
- user_agent (str, опционально) - Строка user-agent браузера

Пример:
account = Account("ваш_golden_key", "Mozilla/5.0...")


### get() -> bool

Получает все данные аккаунта с FunPay.

Возвращает:
- True - если успешно
- False - если произошла ошибка

Пример:
success = account.get()
if success:
    print(f"Баланс: {account.balance}₽")
else:
    print("Не удалось получить данные")


### event() -> bool

Проверяет наличие непрочитанных сообщений в чате.

Возвращает:
- True - если успешно
- False - если произошла ошибка

Пример:
account.event()
if account.unread > 0:
    print(f"У вас {account.unread} непрочитанных сообщений!")


### __str__() -> str

Возвращает строковое представление аккаунта.

Пример:
print(account)
# Вывод: Account(id=12345, username='JohnDoe', balance=1000.0₽)


## Вспомогательные методы (внутренние)

### _safe_text(element) -> str

Безопасно извлекает текст из элемента BeautifulSoup.

Параметры:
- element - Элемент BeautifulSoup или None

Возвращает:
- str - Извлеченный текст или пустая строка, если элемент равен None


### _safe_int(element) -> int

Безопасно извлекает целое число из элемента BeautifulSoup.

Параметры:
- element - Элемент BeautifulSoup или None

Возвращает:
- int - Извлеченное число или 0, если элемент равен None или невалидный


## Примеры использования

### Базовое использование

from funpayplus import Account

# Создаем экземпляр аккаунта
account = Account("ваш_golden_key", "ваш_user_agent")

# Получаем данные
account.get()

# Выводим всю информацию
print(f"Имя пользователя: {account.username}")
print(f"Баланс: {account.balance}₽")
print(f"Рейтинг: {account.rating}/5")
print(f"Активных продаж: {account.active_sell}")
print(f"Активных покупок: {account.active_buy}")
print(f"Сообщений: {account.active_message}")
print(f"ID: {account.id}")
print(f"Дата регистрации: {account.data}")

# Проверяем чат
account.event()
if account.unread > 0:
    print(f"У вас {account.unread} непрочитанных сообщений!")


### Обработка ошибок

from funpayplus import Account

account = Account("ваш_golden_key", "ваш_user_agent")

if not account.get():
    print("Не удалось получить данные аккаунта")
    print("Проверьте golden_key и user_agent")
else:
    print(f"Добро пожаловать {account.username}!")
    print(f"Баланс: {account.balance}₽")


### Проверка только сообщений

from funpayplus import Account

account = Account("ваш_golden_key", "ваш_user_agent")

if account.event():
    if account.unread > 0:
        print(f"У вас {account.unread} непрочитанных сообщений!")
    else:
        print("Нет непрочитанных сообщений")


## Как получить Golden Key

1. Авторизуйтесь на сайте FunPay
2. Откройте DevTools (нажмите F12)
3. Перейдите на вкладку Network (Сеть)
4. Обновите страницу (F5)
5. Нажмите на любой запрос к funpay.com
6. В Request Headers найдите заголовок Cookie
7. Найдите golden_key=ВАШ_ТОКЕН_ЗДЕСЬ

Пример:
Cookie: golden_key=3vjjfr7ka4whckevijz8t9epj2vwg215; ...


## Важные замечания

- Никогда не делитесь своим golden_key с другими
- Эта библиотека НЕ хранит и НЕ передает ваши данные
- Используйте на свой страх и риск
- Может нарушать Пользовательское соглашение FunPay


## Автор

DuckWithKnife404

GitHub: [\[ссылка на ваш GitHub\]](https://github.com/DuckWithKnife404)
