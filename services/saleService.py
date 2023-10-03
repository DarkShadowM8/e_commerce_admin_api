import datetime

from sqlalchemy import select, and_, func
from database.database import Product, Sales
from config.contextmanagerservice import session_scope
from schemas import sales, inventory
from services import inventoryService


def add_a_sale(sale: sales.Sale):
    with session_scope() as session:
        existing_product = session.execute(select(Product)
                                           .filter(Product.product_id == sale.product_id)).scalar()
        if existing_product:
            if inventoryService.check_inventory(sale.product_id, sale.units_sold):
                sold = Sales(product=existing_product,
                             units_sold=sale.units_sold,
                             cost_rate=sale.units_sold * existing_product.cost_rate,
                             selling_rate=sale.units_sold * existing_product.selling_rate,
                             created_at=datetime.datetime.now())
                inventoryService.add_sold_units_to_inventory(inventory.Inventory(
                    product_id=sale.product_id, units=sale.units_sold, date=datetime.datetime.now()
                ))
                session.add(sold)
                session.commit()
                return "Inventory updated with sold items!!!"
            return "Out of Stock!!!"
        return "Product is not registerd!!!"


def get_sales_by_category(id: int):
    with session_scope() as session:
        sales_data = session.query(Sales).join(Product).filter(Product.category_id == id).all()
        sales = [sale.sales_as_dict() for sale in sales_data]
        return sales


def get_daily_sales():
    with session_scope() as session:
        sales_data = session.query(Sales).filter(
            func.DAY(Sales.created_at) == datetime.datetime.now().day
        ).all()
        sales = [sale.sales_as_dict() for sale in sales_data]
        return sales


def get_monthly_sales(month: int):
    with session_scope() as session:
        sales_data = session.query(Sales).filter(
            func.MONTH(Sales.created_at) == month
        ).all()
        sales = [sale.sales_as_dict() for sale in sales_data]
        return sales


def get_yearly_sales(year: int):
    with session_scope() as session:
        sales_data = session.query(Sales).filter(
            func.YEAR(Sales.created_at) == year
        ).all()
        sales = [sale.sales_as_dict() for sale in sales_data]
        return sales


def get_sale_on_date(day: int, month: int, year: int):
    with session_scope() as session:
        if day and month and year:
            sales_data = session.query(Sales).filter(
                func.YEAR(Sales.created_at) == year,
                func.MONTH(Sales.created_at) == month,
                func.DAY(Sales.created_at) == day
            ).all()
            sales = [sale.sales_as_dict() for sale in sales_data]
            return sales
        return "no record found on this date!!!"
