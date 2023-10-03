from sqlalchemy import select
from database.database import Category
from config.contextmanagerservice import session_scope


def get_category_by_name(name: str):
    with session_scope() as session:
        category = session.execute(select(Category)
                                   .filter(Category.name == name)).scalar()

        if category is None:
            return "category name: " + name + " not found"

        return category.category_as_dict()


def get_category_by_id(id: int):
    with session_scope() as session:
        category = session.execute(select(Category)
                                   .filter(Category.category_id == id)).scalar()

        if category is None:
            return "category id: " + id + " not found"

        return category.category_as_dict()


def add_category(cat: Category):
    with session_scope() as session:
        existing_category = session.execute(select(Category)
                                            .filter(Category.name == cat.name)).scalar()
        if existing_category:
            return "Category with this name: " + cat.name
        try:
            session.add(cat)
            session.commit()
            return "Category " + cat.name + " is added!!!"
        except Exception as e:
            print(e)


def get_all_categories():
    with session_scope() as session:
        categories = session.query(Category).all()
        categories_list = [category.category_as_dict() for category in categories]
        return categories_list
