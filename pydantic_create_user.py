from pydantic import BaseModel, EmailStr, ConfigDict, constr
from pydantic.alias_generators import to_camel

PhoneNumber = constr(
    pattern=r'^\+7\d{10}$',  # Регулярное выражение для проверки формата
    strip_whitespace=True     # Удаляем пробелы
)


class UserSchema(BaseModel):
    """
    Схема модели данных пользователя.q
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str
    email: EmailStr
    last_name: str
    first_name: str
    middle_name: str
    phone_number: PhoneNumber


class CreateUserRequestSchema(BaseModel):
    """
    Схема данных запроса на создание пользователя.
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    email: EmailStr
    last_name: str
    first_name: str
    middle_name: str
    phone_number: PhoneNumber


class CreateUserResponseSchema(BaseModel):
    """
    Схема ответа с данными созданного пользователя.
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    user: UserSchema
