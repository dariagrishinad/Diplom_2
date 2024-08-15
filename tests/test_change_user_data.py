import allure

from constants import ResponseCodes, ResponseMessages
from data import UserData
from user import User


class TestChangeUserData:
    @allure.step('Тестирование изменения данных авторизованного пользователя')
    def test_change_user_data_with_login(self):
        user = User()
        response_registration = user.request_for_create_user(UserData.registration)
        header = {'Authorization': response_registration.json()['accessToken']}
        response_change = user.request_for_change_user_data(UserData.change_all_user_data, header)

        assert response_change.status_code == ResponseCodes.CODE_200 and response_change.json()['success'] == True and response_change.json()['user']['email'] == UserData.change_all_user_data['email']
        user.request_for_delete_user(UserData.change_all_user_data)

    @allure.step('Тестирование изменения данных не авторизованного пользователя')
    def test_change_user_data_without_login(self):
        user = User()
        user.request_for_create_user(UserData.registration)
        response = user.request_for_change_user_data(UserData.change_all_user_data, "")

        assert response.status_code == ResponseCodes.CODE_401 and response.json()['message'] == ResponseMessages.MESSAGE_CHANGE_DATA_WITHOUT_AUTH
        user.request_for_delete_user(UserData.registration)
