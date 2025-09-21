from pydantic import BaseModel, Field, ConfigDict
from enum import StrEnum

from tools.fakers import fake


class OperationType(StrEnum):
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    PURCHASE = "PURCHASE"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"

class OperationStatus(StrEnum):
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    UNSPECIFIED = "UNSPECIFIED"


class GetOperationsQuerySchema(BaseModel):
    """
    Структура данных для получения списка операций для определенного счета.
    """
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias="accountId")

class GetOperationsSummaryQuerySchema(BaseModel):
    """
    Структура данных для получения статистики по операциям для определенного счета.
    """
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias="accountId")

class MakeFeeOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции комиссии.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")

class MakeTopUpOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции пополнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")

class MakeCashbackOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции кэшбэка.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")

class MakeTransferOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции перевода.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")

class MakePurchaseOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции покупки.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")
    category: str = Field(default_factory=fake.category)

class MakeBillPaymentOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции оплаты по счету.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")

class MakeCashWithdrawalOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции снятия наличных денег.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")

class OperationSchema(BaseModel):
    """
    Описание структуры данных Операции
    """
    id: str
    type: OperationType
    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    category: str
    created_at: str = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")

class OperationReceiptSchema(BaseModel):
    """
    Описание структуры данных Чека операции
    """
    url: str
    document: str

class OperationsSummarySchema(BaseModel):
    """
    Описание структуры данных Суммы операций
    """
    spent_amount: float = Field(alias="spentAmount")
    received_amount: float = Field(alias="receivedAmount")
    cashback_amount: float = Field(alias="cashbackAmount")

class GetOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа получения одной операцией
    """
    operation: OperationSchema

class GetOperationsResponseSchema(BaseModel):
    """
    Описание структуры ответа получения списка операций
    """
    operations: list[OperationSchema]

class GetOperationReceiptResponseSchema(BaseModel):
    """
    Описание структуры ответа получения чека об операции.
    """
    receipt: OperationReceiptSchema

class GetOperationsSummaryResponseSchema(BaseModel):
    """
    Описание структуры ответа получения Суммы операций.
    """
    summary: OperationsSummarySchema

class MakeFeeOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа операции Оплаты.
    """
    operation: OperationSchema

class MakeTopUpOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа операции Пополнения.
    """
    operation: OperationSchema

class MakeCashbackOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа операции Кэшбэка.
    """
    operation: OperationSchema

class MakeTransferOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа операции Перевода.
    """
    operation: OperationSchema

class MakePurchaseOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа операции Покупка.
    """
    operation: OperationSchema

class MakeBillPaymentOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа операции Оплаты счета.
    """
    operation: OperationSchema

class MakeCashWithdrawalOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа операции Снятие наличных.
    """
    operation: OperationSchema
