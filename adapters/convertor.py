import datetime

from database import database
from schemas import product, category, sales


def _toProduct(p: product.Product):
    try:
        return database.Product(name=p.name, description=p.description, cost_rate=p.cost_rate, selling_rate=p.selling_rate,
                            created_at=datetime.datetime.now())
    except Exception as e:
        return e

def _toCategory(c: category.Category):
    try:
        return database.Category(name=c.name, desc=c.desc, created_at=datetime.datetime.now())
    except Exception as e:
        return e

def _toSale(s: sales.Sale):
    try:
        return database.Sales(units_sold=s.units_sold, cost_rate=s.cost_rate, selling_rate=s.selling_rate)
    except Exception as e:
        return e
