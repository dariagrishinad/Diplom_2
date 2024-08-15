import allure

from constants import ResponseCodes, ResponseMessages
from data import UserData, OrderData
from order import Order
from user import User


class TestCreateOrder:
    @allure.step('Тестирование создания заказа с авторизованным пользователем и с ингредиентами')
    def test_create_order_with_login_user_and_with_ingredients(self):
        order = Order()
        user = User()
        response_registration = user.request_for_create_user(UserData.registration)
        header = {'Authorization': response_registration.json()['accessToken']}
        response_ingredients = order.request_for_get_ingredients()
        payload = {
            "ingredients": [
                response_ingredients.json()['data'][0]['_id'],
                response_ingredients.json()['data'][1]['_id']
            ]
        }
        response = order.request_for_create_order(payload, header)

        assert response.status_code == ResponseCodes.CODE_200 and response.json()['success'] == True
        user.request_for_delete_user(UserData.registration)

    @allure.step('Тестирование создания заказа с не авторизованным пользователем и с ингредиентами')
    def test_create_order_without_login_user_and_with_ingredients(self):
        order = Order()
        response_ingredients = order.request_for_get_ingredients()
        payload = {
            "ingredients": [
                response_ingredients.json()['data'][0]['_id'],
                response_ingredients.json()['data'][1]['_id']
            ]
        }
        response = order.request_for_create_order(payload, "")

        assert response.status_code == ResponseCodes.CODE_200 and response.json()['success'] == True

    @allure.step('Тестирование создания заказа с не авторизованным пользователем и без ингредиентов')
    def test_create_order_without_login_user_and_without_ingredients(self):
        order = Order()
        response = order.request_for_create_order({}, "")

        assert response.status_code == ResponseCodes.CODE_400 and response.json()['message'] == ResponseMessages.MESSAGE_CREATE_ORDER_WITHOUT_INGREDIENTS

    @allure.step('Тестирование создания заказа с несуществующими ингредиентами')
    def test_create_order_with_invalid_ingredients(self):
        order = Order()
        response = order.request_for_create_order(OrderData.invalid_ingredients_for_create_order, "")

        assert response.status_code == ResponseCodes.CODE_500 and ResponseMessages.MESSAGE_CREATE_ORDER_WITH_INVALID_INGREDIENTS in response.text
