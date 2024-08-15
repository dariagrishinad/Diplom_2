import allure
import pytest

from constants import ResponseCodes, ResponseMessages
from data import UserData
from user import User


class TestLoginUser:
    @allure.step('Тестирование успешной авторизации пользователя')
    def test_login_user_successfully(self):
        user = User()
        response = user.request_for_login_user(UserData.login)

        assert response.status_code == ResponseCodes.CODE_200 and response.json()['success'] == True

    @allure.step('Тестирование авторизации пользователя с некорректными данными')
    @pytest.mark.parametrize('payload', [UserData.login_with_invalid_email, UserData.login_with_invalid_password, UserData.login_with_invalid_email_and_password])
    def test_login_user_with_invalid_data(self, payload):
        user = User()
        response = user.request_for_login_user(payload)

        assert response.status_code == ResponseCodes.CODE_401 and response.json()['message'] == ResponseMessages.MESSAGE_LOGIN_WITH_INCORRECT_DATA
