from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        1, "arroz", "marca", "10-10-10", "10-10-20", "123", "local seco"
    )
    assert (
        str(product)
        ==
        "O produto arroz fabricado em 10-10-10 por marca "
        "com validade até 10-10-20 precisa ser armazenado local seco."
    )
