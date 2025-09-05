from pydantic import BaseModel


class DocumentSchema(BaseModel):
    """
    Описание структуры документа.
    """
    url: str
    document: str

class GetTariffDocumentResponseSchema(BaseModel):
    """
    Описание структуры ответа получения документа тарифа.
    """
    tariff: DocumentSchema

class GetContractDocumentResponseSchema(BaseModel):
    """
    Описание структуры ответа получения документа контракта.
    """
    tariff: DocumentSchema
