from locust import HttpUser, between, task

from tools.fakers import fake


class OpenDebitCardAccountScenarioUser(HttpUser):
    wait_time = between(1, 3)

    user_data: dict

    def on_start(self) -> None:
        """
        Метод on_start вызывается один раз при запуске каждой сессии виртуального пользователя.
        Здесь мы создаем нового пользователя, отправляя POST-запрос к /api/v1/users.
        """
        request = {
            "email": fake.email(),
            "lastName": fake.last_name(),
            "firstName": fake.first_name(),
            "middleName": fake.middle_name(),
            "phoneNumber": fake.phone_number()
        }
        response = self.client.post("/api/v1/users", json=request)

        self.user_data = response.json()

    @task
    def open_debit_card_account(self):
        """
        Основная нагрузочная задача: открытие дебетового счета.
        Здесь мы выполняем POST-запрос к /api/v1/accounts/open-deposit-account.
        """
        request = {"userId": self.user_data['user']['id']}

        self.client.post("/api/v1/accounts/open-deposit-account", json=request)
