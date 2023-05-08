import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def load_csv(path):
        with open(path) as file:
            reader = csv.DictReader(file)
            return list(reader)

    @staticmethod
    def load_json(path):
        with open(path) as file:
            return json.load(file)

    @staticmethod
    def load_xml(path):
        tree = ET.parse(path)
        root = tree.getroot()
        data = []
        for product in root.findall("record"):
            product_dict = {}
            for child in product:
                product_dict[child.tag] = child.text
            data.append(product_dict)
        return data

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

    @staticmethod
    def get_loader(file_type):
        loaders = {
            "csv": Inventory.load_csv,
            "json": Inventory.load_json,
            "xml": Inventory.load_xml,
        }

        try:
            return loaders[file_type]
        except KeyError:
            raise ValueError("Formato de arquivo inválido")

    @classmethod
    def import_data(cls, path, report_type) -> str:
        file_extension = path.split(".")[-1]
        if file_extension not in ["csv", "json", "xml"]:
            raise ValueError("Arquivo inválido")

        loader = Inventory.get_loader(file_extension)(path)
        type_report = Inventory.get_report_type(report_type).generate(loader)
        print(type_report)

        return type_report
