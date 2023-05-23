import csv
import os
from os import name

import pytest
from src.item import Item, InstantiateCSVError


#@pytest.fixture()

def test_calculate_total_price():
    item = Item('apple', 10.0, 5)
    assert item.calculate_total_price() == 50.0

def test_apply_discount():
    item = Item('apple', 10.0, 5)
    item.apply_discount()
    assert item.price == 10.0 * item.pay_rate

def test_name():
    assert name != "item1"


def test_item_creation():
    item = Item("Карандаш", 25.0, 50)
    assert item.name == "Карандаш"
    assert item.price == 25.0
    assert item.quantity == 50


def test_item_name_length():
    try:
        item = Item("Ноутбук Lenovo", 50000.0, 5)
    except ValueError as e:
        assert str(e) == "Наименование товара не может быть больше 10 символов"


def test_item_total_price():
    item = Item("Чайник", 2000.0, 10)
    assert item.calculate_total_price() == 20000.0


def test_item_discount():
    Item.pay_rate = 0.9
    item = Item("Кофеварка", 5000.0, 3)
    item.apply_discount()
    assert item.price == 4500.0

def test_instantiate_from_csv():
    open("items.csv", "w").close()
    with open("items.csv", "w") as f:
        csv.writer(f).writerows([["name", "price", "quantity"], ["item1", "10.0"]])

    try:
        Item.instantiate_from_csv()
    except FileNotFoundError as e:
        assert str(e) == "Отсутствует файл item.csv"

    try:
        Item.instantiate_from_csv()
    except InstantiateCSVError as e:
        assert str(e) == "Файл item.csv поврежден"

    os.remove("items.csv")

def test_string_to_number():
    assert Item.string_to_number('10') == 10
    assert Item.string_to_number('10.0') == 10.0


def test_repr():
    item = Item('Test Item', 10, 2)
    assert repr(item) == "Item('Test Item', 10, 2)"


def test_str():
    item = Item('Test Item', 10, 2)
    assert str(item) == "Test Item"
