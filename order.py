import allure
import requests

from constants import Urls


class Order:
    @allure.step('Запрос для получения списка ингредиентов')
    def request_for_get_ingredients(self):
        response = requests.get(Urls.INGREDIENTS_LIST_URL)
        return response

    @allure.step('Запрос для создания заказа')
    def request_for_create_order(self, payload, header):
        response = requests.post(Urls.CREATE_ORDER_URL, data=payload, headers=header)
        return response

    @allure.step('Запрос для получения списка заказов пользователя')
    def request_for_get_user_orders(self, header):
        response = requests.get(Urls.GET_USER_ORDERS, headers=header)
        return response
