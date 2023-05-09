from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.importer.importer import Importer
from inventory_report.reports.complete_report import CompleteReport
from collections.abc import Iterable


class InventoryRefactor(Iterable):
    def __init__(self, importer: Importer):
        self.data = []
        self.importer = importer

    @staticmethod
    def get_report_type(report_type):
        reports = {
            "simples": SimpleReport,
            "completo": CompleteReport,
        }
        try:
            return reports[report_type]
        except KeyError:
            raise ValueError("Formato de relatório inválido")

    def import_data(self, path, report_type):
        self.data += self.importer.import_data(path)
        report = InventoryRefactor.get_report_type(report_type).generate(
            self.data
        )
        return report

    def __iter__(self):
        return InventoryIterator(self.data)
