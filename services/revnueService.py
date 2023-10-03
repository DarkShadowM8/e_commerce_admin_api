import datetime

from _decimal import Decimal
from sqlalchemy import select, func
from config.contextmanagerservice import session_scope
from database.database import Sales, Product, Category


def total_revenue():
    with session_scope() as session:
        total_selling_rates = session.execute(func.sum(Sales.selling_rate)).scalar()
        # total_revenue = sum(selling_rate for (selling_rate,) in total_selling_rates)
        print(total_selling_rates)
        revenue = Decimal(total_selling_rates).quantize(Decimal('0.00'))
        return revenue


def single_product_revenue(product_id: int):
    with session_scope() as session:
        product = session.execute(select(Product).filter(Product.product_id == product_id)).scalar()
        if product is None:
            return "Product id not found!!!"

        product_revenue = session.execute(
            select(func.sum(Sales.units_sold * Sales.selling_rate))
            .filter(Sales.product_id == product_id)
            ).scalar()
        if product_revenue is None:
            return 0.0
        revenue = Decimal(product_revenue).quantize(Decimal('0.00'))
        return revenue


def revenue_by_categories():
    with session_scope() as session:
        query = (
            session.query(Category.name, func.sum(Sales.selling_rate).label('revenue'))
            .join(Product, Category.category_id == Product.category_id)
            .join(Sales, Product.product_id == Sales.product_id)
            .group_by(Category.name)
            .all()
        )
        revenue_by_category = [{'category': category_name, 'revenue': Decimal(revenue ).quantize(Decimal('0.00'))} for category_name, revenue in query]

        return revenue_by_category


from sqlalchemy import func


def get_revenue_for_category(category_name):
    with session_scope() as session:
        # Join the Sales and Product tables on the product_id column
        query = (
            session.query(Category.name, func.sum(Sales.units_sold * Sales.selling_rate).label('revenue'))
            .join(Product, Category.category_id == Product.category_id)
            .join(Sales, Product.product_id == Sales.product_id)
            .filter(Category.name == category_name)  # Filter by the specified category_name
            .group_by(Category.name)
            .first()  # Use first() to get a single result
        )

        if query:
            # If a result is found, return the revenue
            revenue = Decimal(query.revenue).quantize(Decimal('0.00'))
            return {'category': query.name, 'revenue': revenue}
        else:
            # If no result is found, return None or raise an exception as needed
            return None
