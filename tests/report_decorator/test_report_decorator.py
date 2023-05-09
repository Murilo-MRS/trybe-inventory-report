from inventory_report.reports.colored_report import ColoredReport
from tests.factories.product_factory import ProductFactory
from inventory_report.reports.simple_report import SimpleReport


def test_decorar_relatorio():
    mock = []

    new_product = ProductFactory()
    mock.append(vars(new_product))

    colored_report = ColoredReport(SimpleReport)
    result = colored_report.generate(mock)

    assert (
        "\033[32mData de fabricação mais antiga:\033[0m "
        f"\033[36m{new_product.data_de_fabricacao}\033[0m" in result
    )
    assert (
        "\033[32mData de validade mais próxima:\033[0m "
        f"\033[36m{str(new_product.data_de_validade)}\033[0m" in result
    )
    assert (
        "\033[32mEmpresa com mais produtos:\033[0m "
        f"\033[31m{new_product.nome_da_empresa}\033[0m" in result
    )
