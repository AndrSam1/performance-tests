from locust import User, between, task

from clients.http.gateway.locust import GatewayHTTPTaskSet
from clients.http.gateway.users.schema import CreateUserResponseSchema


class GetAccountsTaskSet(GatewayHTTPTaskSet):
    """
    Нагрузочный сценарий, который последовательно:
    1. Создаёт нового пользователя.
    2. Открывает депозитный счёт (только в случае создания пользователя).
    3. Получает все счета пользователя (только в случае создания пользователя).

    Использует базовый GatewayHTTPTaskSet и уже созданных в нём API клиентов.
    """

    create_user_response: CreateUserResponseSchema | None = None

    @task(2)
    def create_user(self):
        """
        Создаём нового пользователя и сохраняем результат для последующих шагов.
        """
        self.create_user_response = self.users_gateway_client.create_user()

    @task(2)
    def open_deposit_account(self):
        """
        Открывает депозитный счёт (только в случае создания пользователя).
        """
        if not self.create_user_response:
            return

        self.accounts_gateway_client.open_deposit_account(user_id=self.create_user_response.user.id)

    @task(6)
    def get_accounts(self):
        """
        Получает все счета пользователя (только в случае создания пользователя).
        """
        if not self.create_user_response:
            return

        self.accounts_gateway_client.get_accounts(user_id=self.create_user_response.user.id)


class GetAccountsScenarioUser(User):
    """
    Пользователь Locust, исполняющий последовательный сценарий получения всех счетов пользователя.
    """
    host = "localhost"
    tasks = [GetAccountsTaskSet]
    wait_time = between(1, 3)
