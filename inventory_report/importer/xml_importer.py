import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path) -> list:
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")

        tree = ET.parse(path)
        root = tree.getroot()
        product_list = []

        for product in root.findall("record"):
            product_dict = {}
            for child in product:
                product_dict[child.tag] = child.text
            product_list.append(product_dict)

        return product_list
