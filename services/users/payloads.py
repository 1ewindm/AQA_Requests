from faker import Faker

faker = Faker()


class Payloads:

    create_user = {
        "email": faker.email(),
        "password": faker.password(length=10),
        "name": faker.name(),
        "nickname": faker.user_name()
    }

