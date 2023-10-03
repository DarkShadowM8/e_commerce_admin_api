from services import inventoryService
from schemas import inventory
from fastapi import APIRouter


inventoryRouter = APIRouter()

@inventoryRouter.post("/add-units-in-inventory")
def add_inventory(request: inventory.Inventory):
    return inventoryService.add_inventory(request)


@inventoryRouter.post("/update-sold-units-in-inventory")
def add_sold_units_to_inventory(request: inventory.Inventory):
    return inventoryService.add_sold_units_to_inventory(request)

@inventoryRouter.get("/get-inventory")
def get_inventory():
    return inventoryService.get_all_inventory()

@inventoryRouter.get("/get-inventory/{id}")
def get_single_product_inventory(id: int):
    return inventoryService.get_single_product_inventory(id)