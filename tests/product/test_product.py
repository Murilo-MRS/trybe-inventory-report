from inventory_report.inventory.product import Product
from tests.factories.product_factory import ProductFactory


def test_cria_produto():
    product_factory = ProductFactory()
    product = Product(
        product_factory.id,
        product_factory.nome_do_produto,
        product_factory.nome_da_empresa,
        product_factory.data_de_fabricacao,
        product_factory.data_de_validade,
        product_factory.numero_de_serie,
        product_factory.instrucoes_de_armazenamento,
    )

    assert product.id == product_factory.id
    assert product.nome_do_produto == product_factory.nome_do_produto
    assert product.nome_da_empresa == product_factory.nome_da_empresa
    assert product.data_de_fabricacao == str(
        product_factory.data_de_fabricacao
    )
    assert product.data_de_validade == str(product_factory.data_de_validade)
    assert product.numero_de_serie == product_factory.numero_de_serie
    assert (
        product.instrucoes_de_armazenamento
        == product_factory.instrucoes_de_armazenamento
    )
