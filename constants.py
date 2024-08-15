class Urls:
    REGISTRATION_URL = 'https://stellarburgers.nomoreparties.site/api/auth/register'
    LOGIN_URL = 'https://stellarburgers.nomoreparties.site/api/auth/login'
    CHANGE_DATA_URL = 'https://stellarburgers.nomoreparties.site/api/auth/user'
    CREATE_ORDER_URL = 'https://stellarburgers.nomoreparties.site/api/orders'
    INGREDIENTS_LIST_URL = 'https://stellarburgers.nomoreparties.site/api/ingredients'
    GET_USER_ORDERS = 'https://stellarburgers.nomoreparties.site/api/orders'


class Constants:
    EMAIL = 'dariagrishina10@ya.ru'
    PASSWORD = '123456'
    NAME = 'Daria'
    INVALID_EMAIL = 'dariagrishina10@ya.r'
    INVALID_PASSWORD = '12345'
    CHANGED_NAME = 'Daria1'


class ResponseCodes:
    CODE_200 = 200
    CODE_400 = 400
    CODE_401 = 401
    CODE_403 = 403
    CODE_500 = 500


class ResponseMessages:
    MESSAGE_REGISTRATION_WITH_EXISTS_USER = 'User already exists'
    MESSAGE_REGISTRATION_WITHOUT_DATA = 'Email, password and name are required fields'
    MESSAGE_LOGIN_WITH_INCORRECT_DATA = 'email or password are incorrect'
    MESSAGE_CHANGE_DATA_WITHOUT_AUTH = 'You should be authorised'
    MESSAGE_CREATE_ORDER_WITHOUT_INGREDIENTS = 'Ingredient ids must be provided'
    MESSAGE_CREATE_ORDER_WITH_INVALID_INGREDIENTS = 'Internal Server Error'
    MESSAGE_GET_ORDERS_WITHOUT_LOGIN = 'You should be authorised'

