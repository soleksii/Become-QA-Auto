import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    database = Database()
    database.test_connection()


@pytest.mark.database
def test_check_all_users():
    database = Database()
    result = database.get_all_users()
    print(result)


@pytest.mark.database
def test_check_user_sergii():
    database = Database()
    address = database.get_user_address_by_name('Sergii')

    assert address[0][0] == 'Maydan Nezalezhnosti 1'
    assert address[0][1] == 'Kyiv'
    assert address[0][2] == '3127'
    assert address[0][3] == 'Ukraine'


@pytest.mark.database
def test_product_qnt_update():
    database = Database()
    database.update_product_qnt_by_id(1, 25)
    qnt = database.select_product_qnt_by_id(1)

    assert qnt[0][0] == 25


@pytest.mark.database
def test_product_insert():
    database = Database()
    account_id = 4
    database.delete_product_by_id(account_id)
    database.insert_product(account_id, 'печиво', 'солодке', 30)
    qnt = database.select_product_qnt_by_id(account_id)

    assert qnt[0][0] == 30


@pytest.mark.database
def test_product_delete():
    database = Database()
    database.insert_product(99, 'тестові', 'дані', 999)
    database.delete_product_by_id(99)
    product = database.select_product_qnt_by_id(99)

    assert not product


@pytest.mark.database
def test_detailed_orders():
    database = Database()
    orders = database.get_detailed_orders()
    print("Замовлення", orders)

    assert len(orders) == 1

    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'
