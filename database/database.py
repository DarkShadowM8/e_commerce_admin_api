from sqlalchemy.orm import registry, relationship
from sqlalchemy import Column, String, Integer, ForeignKey, Float, DateTime, create_engine, Boolean
from config.contextmanagerservice import engine

mapper_registry = registry()
Base = mapper_registry.generate_base()


class Product(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=25), index=True)
    description = Column(String(length=255))
    category_id = Column(Integer, ForeignKey("categories.category_id"), nullable=True)
    cost_rate = Column(Float)
    selling_rate = Column(Float)
    created_at = Column(DateTime)

    category = relationship("Category", back_populates="product")
    sales = relationship("Sales", back_populates="product")  # Define the 'sales' relationship
    inventory = relationship("Inventory", back_populates="product")

    def __repr__(self):
        return "id = '{0}', name = {1}, description = {2}, category = {3}, cost_rate = {4}, selling_rate = {5}, created_at = {6}" \
            .format(self.product_id, self.name, self.description, self.category_id, self.cost_rate, self.selling_rate,
                    self.created_at)

    def products_as_dict(self):
        return {
            "id": self.product_id,
            "name": self.name,
            "description": self.description,
            "category": self.category_id,
            "cost_rate": self.cost_rate,
            "selling_rate": self.selling_rate,
            "created_at": self.created_at.strftime("%Y-%m-%d"),
        }

    def update(self, name=None, description=None, cost_rate=None, selling_rate=None):
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if cost_rate is not None:
            self.cost_rate = cost_rate
        if selling_rate is not None:
            self.selling_rate = selling_rate


class Sales(Base):
    __tablename__ = "sales"

    sale_id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.product_id"))
    units_sold = Column(Integer)
    cost_rate = Column(Float)
    selling_rate = Column(Float)
    created_at = Column(DateTime)

    product = relationship("Product", back_populates="sales")

    def __repr__(self):
        return "id = '{0}', product_id = {1}, units_sold = {2}, cost_rate = {3}, selling_rate = {4}, created_at = {5}," \
            .format(self.sale_id, self.product_id, self.units_sold, self.cost_rate, self.selling_rate, self.created_at)

    def sales_as_dict(self):
        return {
            "id": self.sale_id,
            "product": self.product_id,
            "units_sold": self.units_sold,
            "cost_rate": self.cost_rate,
            "selling_rate": self.selling_rate,
            "created_at": self.created_at.strftime("%Y-%m-%d"),
        }

    def update(self, product=None, units_sold=None, cost_rate=None, selling_rate=None):
        if product is not None:
            self.product = product
        if units_sold is not None:
            self.units_sold = units_sold
        if cost_rate is not None:
            self.cost_rate = cost_rate
        if selling_rate is not None:
            self.selling_rate = selling_rate


class Category(Base):
    __tablename__ = "categories"

    category_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=25), index=True)
    desc = Column(String(length=255))
    created_at = Column(DateTime)

    product = relationship("Product", back_populates="category")

    def __repr__(self):
        return "id = '{0}', name = {1}, description = {2}, created_at = {3}" \
            .format(self.category_id, self.name, self.desc, self.created_at)

    def category_as_dict(self):
        return {
            "id": self.category_id,
            "name": self.name,
            "description": self.desc,
            "created_at": self.created_at,
        }

    def update(self, name=None, description=None):
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description


class Inventory(Base):
    __tablename__ = "inventories"

    inventory_id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.product_id"))
    total_units = Column(Integer)
    available_units = Column(Integer)
    sold_units = Column(Integer)

    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    product = relationship("Product", back_populates="inventory")

    def __repr__(self):
        return "id = '{0}', product_id = {1}, total_units = {2}, available_units = {3}, sold_units = {4}, created_at = {5}, created_at = {6}" \
            .format(self.inventory_id, self.product_id, self.total_units, self.available_units, self.sold_units,
                    self.created_at, self.updated_at)

    def Inventory_as_dict(self):
        return {
            "id": self.inventory_id,
            "product_id": self.product_id,
            "total_units": self.total_units,
            "available_units": self.available_units,
            "sold_units": self.sold_units,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    def update(self, product_id=None, total_units=None, available_units=None, sold_units=None):
        if product_id is not None:
            self.product_id = product_id
        if total_units is not None:
            self.total_units = total_units
        if available_units is not None:
            self.available_units = available_units
        if sold_units is not None:
            self.sold_units = sold_units

class demoFlag(Base):
    __tablename__ = "flag"

    flag_id = Column(Integer, primary_key=True, index=True)
    flag = Column(Boolean)

    def flag_as_dict(self):
        return {
            "id": self.flag_id,
            "flag": self.flag,
        }

Base.metadata.create_all(engine)
