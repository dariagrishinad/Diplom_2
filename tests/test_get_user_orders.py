import allure

from constants import ResponseCodes, ResponseMessages
from data import UserData
from order import Order
from user import User


class TestGetUserOrders:
    @allure.step('Тестирование получения списка заказов авторизованного пользователя')
    def test_get_user_orders_with_login(self):
        user = User()
        order = Order()
        response_registration = user.request_for_create_user(UserData.registration)
        header = {'Authorization': response_registration.json()['accessToken']}
        response_ingredients = order.request_for_get_ingredients()
        payload = {
            "ingredients": [
                response_ingredients.json()['data'][0]['_id']
            ]
        }
        response_create_order = order.request_for_create_order(payload, header)
        response_get_data = order.request_for_get_user_orders(header)

        assert response_get_data.status_code == ResponseCodes.CODE_200 and response_create_order.json()['order']['ingredients'][0]['_id'] == response_get_data.json()['orders'][0]['ingredients'][0]
        user.request_for_delete_user(UserData.registration)

    @allure.step('Тестирование получения списка заказов не авторизованного пользователя')
    def test_get_user_orders_without_login(self):
        order = Order()
        response = order.request_for_get_user_orders("")

        assert response.status_code == ResponseCodes.CODE_401 and response.json()['message'] == ResponseMessages.MESSAGE_GET_ORDERS_WITHOUT_LOGIN
