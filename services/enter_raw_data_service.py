import random

from sqlalchemy import select

import schemas.sales, schemas.inventory
from config.contextmanagerservice import session_scope
from database import database
from database.database import Product, Sales, Category, Inventory, demoFlag
from schemas import inventory, sales
from services import productService, categoryService, saleService, inventoryService

def create_products(product_data: list[database.Product]):
    with session_scope() as session:
        try:
            for item in product_data:
                session.add(item)
            session.commit()
            return {"message": "Products created successfully"}
        except Exception as e:
            return e.__str__()


def generate_demo_products(num_products=10):
    products = []
    for _ in range(num_products):
        product = Product(
            name="Product" + (random.randint(0,100).__str__()),
            description=f"Description for Product {_}",
            cost_rate=random.uniform(1.0, 50.0),
            selling_rate=random.uniform(50.0, 100.0),
            created_at="2023-10-01",  # Set your desired date here
        )
        products.append(product)
    return products

def insert_demo_products(products):
    with session_scope() as session:
        try:
            count:int= 1
            for product in products:
                productService.add_product(product)
                category_id:int = random.randint(1, 5)
                productService.update_product_category(category_id,count)
                count+=1
        except Exception as e:
            session.rollback()
            raise e



def generate_demo_sales(num_sales=20):
    sales_data = []  # Rename the variable to avoid the conflict
    for _ in range(num_sales):
        sale = sales.Sale(
            product_id=random.randint(1, 10),  # Replace with your product IDs
            units_sold=random.randint(1, 100),
        )
        sales_data.append(sale)
    return sales_data


# Insert demo sales data into the database
def insert_demo_sales(sales):
    with session_scope() as session:
        try:
            for sale in sales:
                saleService.add_a_sale(sale)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e


def generate_demo_categories(num_categories=5):
    categories = []
    for _ in range(num_categories):
        category = Category(
            name=f"Category {_}",
            desc=f"Description for Category {_}",
        )
        categories.append(category)
    return categories


# Insert demo category data into the database
def insert_demo_categories(categories):
    with session_scope() as session:
        try:
            for category in categories:
                categoryService.add_category(category)
        except Exception as e:
            session.rollback()
            raise e


def generate_demo_inventory(num_items=20):
    inventory_items = []
    for _ in range(num_items):
        inventory_item = inventory.Inventory(
            product_id=random.randint(1, 10),  # Replace with your product IDs
            units=random.randint(50, 200),
        )
        inventory_items.append(inventory_item)
    return inventory_items


# Insert demo inventory data into the database
def insert_demo_inventory(inventory_items):
    with session_scope() as session:
        try:
            for inventory_item in inventory_items:
                inventoryService.add_inventory(inventory_item)
        except Exception as e:
            session.rollback()
            raise e

def flag_meth():
    with session_scope() as s:
        d = database.demoFlag(flag=False)
        s.add(d)
        s.commit()

def generate_demo_data():
    with session_scope() as session:
        flag_meth()
        flag_obj = session.execute(select(demoFlag).filter(demoFlag.flag_id==1)).scalar()
        if not flag_obj.flag:
            demo_categories = generate_demo_categories()
            insert_demo_categories(demo_categories)
            demo_products = generate_demo_products()
            insert_demo_products(demo_products)
            demo_inventory = generate_demo_inventory()
            insert_demo_inventory(demo_inventory)
            demo_sales = generate_demo_sales()
            insert_demo_sales(demo_sales)
        flag_obj.flag = True
        session.commit()

