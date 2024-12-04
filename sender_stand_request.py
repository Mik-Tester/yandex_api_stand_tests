# Импорт настроек из модуля configuration, который содержит параметры конфигурации, такие как URL сервиса
import configuration
# Импорт библиотеки requests для выполнения HTTP-запросов
import requests
# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data

# GET-ЗАПРОСЫ
# Функция get_docs, которая не принимает параметров
def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)
response = get_docs()
print(response.status_code)

# Функция для отправки GET-запроса, для получения логов
def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH,
                        params={"count":20})
response = get_logs()
print(response.status_code)
print(response.headers)

# Функция для отправки GET-запроса, для получения данных из таблицы пользователей
def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)
response = get_users_table()
print(response.status_code)


# POST-ЗАПРОСЫ
# Функция для отправки POST-запроса, для создания нового пользователя
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)
response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())

#Функция для отправки POST-запроса, для поиска наборов по продуктам
def post_products_kits(products_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                         json=products_ids,
                         headers=data.headers)
response = post_products_kits(data.products_ids)
print(response.status_code)
print(response.json())