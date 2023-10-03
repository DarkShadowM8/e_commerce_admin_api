import datetime

from sqlalchemy import select
from database.database import Inventory, Product
from config.contextmanagerservice import session_scope
from schemas import inventory


def add_units_to_inventory(inv: inventory.Inventory, inventory: Inventory):
    with session_scope() as session:
        inventory.total_units = inventory.total_units + inv.units
        inventory.available_units = inventory.available_units + inv.units
        inventory.updated_at = datetime.datetime.now()
        session.commit()
    return "Units added in inventory"


def add_inventory(inv: inventory.Inventory):
    with session_scope() as session:
        try:
            product = session.execute(select(Product)
                                      .filter(Product.product_id == inv.product_id)).scalar()
            if product:
                existing_inventory = session.execute(select(Inventory)
                                                     .filter(Inventory.product_id == inv.product_id)).scalar()
                if existing_inventory:
                    return add_units_to_inventory(inv, existing_inventory)
                else:
                    session.add(
                        Inventory(product=product, total_units=inv.units, available_units=inv.units, sold_units=0,
                                  created_at=datetime.datetime.now()))
                    session.commit()
                return "Inventory added!!!"
        except Exception as e:
            print(e)


def add_sold_units_to_inventory(inv: inventory.Inventory):
    with session_scope() as session:
        try:
            existing_inventory: Inventory = session.execute(select(Inventory)
                                                            .filter(Inventory.product_id == inv.product_id)).scalar()
            if existing_inventory is None:
                return "Inventory doesn't exist first add the inventory!!!"
            if existing_inventory.available_units - inv.units < 0:
                units: int = existing_inventory.available_units
                return "Sorry! there are only " + units.__str__() + " units available"
            existing_inventory.available_units = existing_inventory.available_units - inv.units
            existing_inventory.sold_units = existing_inventory.sold_units + inv.units
            existing_inventory.updated_at = datetime.datetime.now()
            session.commit()
            return "Inventory added!!!"
        except Exception as e:
            return e.__str__()


def get_all_inventory():
    with session_scope() as session:
        inventories = session.query(Inventory).all()
        inventories_list = [inventory.Inventory_as_dict() for inventory in inventories]
        return inventories_list


def get_single_product_inventory(product_id: int):
    with session_scope() as session:
        existing_inventory = session.execute(select(Inventory)
                                             .filter(Inventory.product_id == product_id)).scalar()
        if existing_inventory:
            return existing_inventory.Inventory_as_dict()


def check_inventory(product_id: int, units: int):
    with session_scope() as session:
        existing_inventory: Inventory = session.execute(select(Inventory)
                                                        .filter(Inventory.product_id == product_id)).scalar()
        if existing_inventory:
            if existing_inventory.available_units > units:
                return True
            else:
                return False
