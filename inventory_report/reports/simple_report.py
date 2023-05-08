from datetime import datetime
from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(data_list):
        oldest_date = min(
            [product["data_de_fabricacao"] for product in data_list]
        )

        nearest_expiration_date = min(
            [
                product["data_de_validade"]
                for product in data_list
                if product["data_de_validade"]
                >= datetime.now().strftime("%Y-%m-%d")
            ]
        )

        most_productive_company = Counter(
            [product["nome_da_empresa"] for product in data_list]
        ).most_common()[0][0]

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {nearest_expiration_date}\n"
            f"Empresa com mais produtos: {most_productive_company}"
        )
