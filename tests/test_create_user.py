import allure
import pytest

from constants import ResponseCodes, ResponseMessages
from data import UserData
from user import User


class TestCreateUser:
    @allure.step('Тестирование успешного создания пользователя')
    def test_create_user_successfully(self):
        user = User()
        response = user.request_for_create_user(UserData.registration)

        assert response.status_code == ResponseCodes.CODE_200 and response.json()['success'] == True
        user.request_for_delete_user(UserData.registration)

    @allure.step('Тестирование создания существующего пользователя')
    def test_create_user_exist(self):
        user = User()
        response = user.request_for_create_user(UserData.registration_exist_user)

        assert response.status_code == ResponseCodes.CODE_403 and response.json()['message'] == ResponseMessages.MESSAGE_REGISTRATION_WITH_EXISTS_USER
        user.request_for_delete_user(UserData.registration)

    @allure.step('Тестирование создания пользователя с недостающими данными')
    @pytest.mark.parametrize('payload', [UserData.registration_without_email, UserData.registration_without_password, UserData.registration_without_name])
    def test_create_user_without_required_data(self, payload):
        user = User()
        response = user.request_for_create_user(payload)

        assert response.status_code == ResponseCodes.CODE_403 and response.json()['message'] == ResponseMessages.MESSAGE_REGISTRATION_WITHOUT_DATA
        user.request_for_delete_user(UserData.registration)
