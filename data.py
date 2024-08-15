from faker import Faker

from constants import Constants

faker = Faker()


class UserData:
    registration = {
        "email": faker.email(),
        "password": Constants.PASSWORD,
        "name": Constants.NAME
    }
    registration_exist_user = {
        "email": Constants.EMAIL,
        "password": Constants.PASSWORD,
        "name": Constants.NAME
    }
    registration_without_email = {
        "password": Constants.PASSWORD,
        "name": Constants.NAME
    }
    registration_without_password = {
        "email": faker.email(),
        "name": Constants.NAME
    }
    registration_without_name = {
        "email": faker.email(),
        "password": Constants.PASSWORD
    }
    login = {
        "email": Constants.EMAIL,
        "password": Constants.PASSWORD
    }
    login_with_invalid_email = {
        "email": Constants.INVALID_EMAIL,
        "password": Constants.PASSWORD
    }
    login_with_invalid_password = {
        "email": Constants.EMAIL,
        "password": Constants.INVALID_PASSWORD
    }
    login_with_invalid_email_and_password = {
        "email": Constants.INVALID_EMAIL,
        "password": Constants.INVALID_PASSWORD
    }
    change_all_user_data = {
        "email": faker.email(),
        "password": Constants.INVALID_PASSWORD,
        "name": Constants.CHANGED_NAME
    }


class OrderData:
    invalid_ingredients_for_create_order = {
        "ingredients": [
            "test",
            "test1"
        ]
    }
