# FunPayPlus

Библиотека для взаимодействия с FunPay


## Установка

git clone https://github.com/DuckWithKnife404/FunPayPlus.git
cd FunPayPlus
pip install -r requirements.txt


## Быстрый старт

from funpayplus import Account

account = Account("ваш_golden_key", "ваш_user_agent")
account.get()

print(account)


## Свойства аккаунта

После вызова метода get(), становятся доступны следующие свойства:

- username (str) - Имя пользователя
- balance (float) - Текущий баланс в рублях
- active_sell (int) - Количество активных продаж
- active_buy (int) - Количество активных покупок
- active_message (int) - Количество непрочитанных сообщений (из профиля)
- rating (float) - Рейтинг пользователя (0.0 - 5.0)
- data (str) - Дата регистрации
- id (int) - ID пользователя
- unread (int) - Количество непрочитанных сообщений (из чата)
- url (str) - Ссылка на профиль пользователя


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

account = Account("ваш_golden_key", "ваш_user_agent")
account.get()

print(f"Имя пользователя: {account.username}")
print(f"Баланс: {account.balance}₽")
print(f"Рейтинг: {account.rating}/5")
print(f"Активных продаж: {account.active_sell}")
print(f"Активных покупок: {account.active_buy}")
print(f"Сообщений: {account.active_message}")
print(f"ID: {account.id}")
print(f"Дата регистрации: {account.data}")
print(f"Ссылка на профиль: {account.url}")

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
5. Нажмите на запрос с названием "(Ваш ID)/" к funpay.com
   Пример: 123456/
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

GitHub: https://github.com/DuckWithKnife404