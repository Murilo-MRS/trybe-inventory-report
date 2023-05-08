from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(data_list: list):
        response = SimpleReport.generate(data_list)

        most_productive_company = Counter(
            [product["nome_da_empresa"] for product in data_list]
        )

        response += "\nProdutos estocados por empresa:\n"
        for company, quantity in most_productive_company.items():
            response += "- {}: {}\n".format(company, quantity)

        return response
