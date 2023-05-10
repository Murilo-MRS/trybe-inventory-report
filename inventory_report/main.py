import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def importer_factory(file_path):
    file_extension = file_path.split(".")[-1]
    if file_extension not in ["csv", "json", "xml"]:
        raise ValueError("Arquivo inválido")

    if file_extension == "csv":
        return CsvImporter()
    elif file_extension == "json":
        return JsonImporter()
    elif file_extension == "xml":
        return XmlImporter()


def main():
    try:
        file_path = sys.argv[1]
        report_type = sys.argv[2]
        importer = importer_factory(file_path)
        inventory = InventoryRefactor(importer)
        new_report = inventory.import_data(file_path, report_type)
        sys.stdout.write(new_report)
    except IndexError:
        sys.stderr.write("Verifique os argumentos\n")
