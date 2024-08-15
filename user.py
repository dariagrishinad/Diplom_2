import allure
import requests

from constants import Urls


class User:
    @allure.step('Запрос для создания пользователя')
    def request_for_create_user(self, payload):
        response = requests.post(Urls.REGISTRATION_URL, data=payload)
        return response

    @allure.step('Запрос авторизации пользователя')
    def request_for_login_user(self, payload):
        response = requests.post(Urls.LOGIN_URL, data=payload)
        return response

    @allure.step('Запрос для смены данных пользователя')
    def request_for_change_user_data(self, payload, header):
        response = requests.patch(Urls.CHANGE_DATA_URL, data=payload, headers=header)
        return response

    @allure.step('Запрос для удаления пользователя')
    def request_for_delete_user(self, payload):
        response = requests.delete(Urls.CHANGE_DATA_URL, data=payload)
        return response

