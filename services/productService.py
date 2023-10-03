from sqlalchemy import select
from database.database import Product, Category
from config.contextmanagerservice import session_scope


def add_product(product: Product):
    with session_scope() as session:
        existing_product = session.execute(select(Product)
                                           .filter(Product.product_id == product.product_id)).scalar()
        if existing_product:
            return "Product already exist please just update it's inventory!!!"
        try:
            session.add(product)
            session.commit()
            return "Product " + product.name + " is added!!!"
        except Exception as e:
            print(e)
            return e


def get_all_products():
    with session_scope() as session:
        products = session.query(Product).all()
        print(products)
        products_list = [product.products_as_dict() for product in products]
        return products_list


def get_product_by_name(name: str):
    with session_scope() as session:
        print(name)
        products = session.execute(select(Product)
                                   .filter(Product.name == name)).all()
        print("////////////////////////////////////////////////////")
        print(products)
        if not products:
            return "Product name: " + name + " not found"
        try:
            products_list = [product.products_as_dict() for product, in products]
            return products_list
        except Exception as e:
            return "Exception: " + e.__str__()


def get_product_by_id(product_id: int):
    with session_scope() as session:
        product = session.execute(select(Product)
                                  .filter(Product.product_id == product_id)).scalar()

        if product is None:
            return "Product id: " + product_id.__str__() + " not found"
        return product.products_as_dict()


def filter_product_by_category(id: int):
    with session_scope() as session:
        # category = get_category_by_name(name)
        # if category is None:
        #     return None

        products = session.execute(select(Product)
                                   .filter(Product.category_id == id)).all()

        if products is None:
            return "No product is added in this category"

        products_list = [product.products_as_dict() for product in products]
        return products_list


def update_product_category(category_id: int, product_id: int):
    with session_scope() as session:
        category = session.execute(select(Category)
                                   .filter(Category.category_id == category_id)).scalar()
        product = session.execute(select(Product)
                                  .filter(Product.product_id == product_id)).scalar()
        if category is None:
            return "Category doesn't exist"
        if product is None:
            return "No Product found"
        product.category = category
        session.commit()
        return "category updated!!!"
