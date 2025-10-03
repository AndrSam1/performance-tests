import os

from seeds.schema.result import SeedsResult
from tools.logger import get_logger

logger = get_logger("SEEDS_DUMPS")


def save_seeds_result(result: SeedsResult, scenario: str):
    """
    Сохраняет результат сидинга (SeedsResult) в JSON-файл.

    :param result: Результат сидинга, сгенерированный билдером.
    :param scenario: Название сценария нагрузки, для которого создаются данные.
                     Используется для генерации имени файла (например, "credit_card_test").
    """
    # Убедимся, что папка dumps существует
    if not os.path.exists("dumps"):
        os.mkdir("dumps")

    seed_file = f"./dumps/{scenario}_seeds.json"

    # Сохраняем результат сидинга в файл с именем {scenario}_seeds.json
    with open(seed_file, 'w+', encoding="utf-8") as file:
        file.write(result.model_dump_json())

    logger.debug(f"Seeding result saved to file: {seed_file}.")


def load_seeds_result(scenario: str) -> SeedsResult:
    """
    Загружает результат сидинга из JSON-файла.

    :param scenario: Название сценария нагрузки, данные которого нужно загрузить.
    :return: Объект SeedsResult, восстановленный из файла.
    """
    seed_file = f"./dumps/{scenario}_seeds.json"

    # Открываем файл и валидируем его как объект SeedsResult
    with open(seed_file, 'r', encoding="utf-8") as file:
        seed_result = SeedsResult.model_validate_json(file.read())

    logger.debug(f"Seeding result loaded from file: {seed_file}.")

    return seed_result
