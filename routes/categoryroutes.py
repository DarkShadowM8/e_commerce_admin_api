from fastapi import APIRouter
from schemas import category
from services import categoryService
from adapters import convertor

categoryRouter = APIRouter()


@categoryRouter.post("/add")
def add_product(request: category.Category):
    categoryService.add_category(convertor._toCategory(request))
    return "Category with name: " + request.name + " added!!!"


@categoryRouter.get("/get-by-name/{name}")
def get_category_by_name(name: str):
    return categoryService.get_category_by_name(name)


@categoryRouter.get("/get-by-id/{id}")
def get_category_by_id(id: int):
    return categoryService.get_category_by_id(id)


@categoryRouter.get("/get-all")
def get_all_categories():
    return categoryService.get_all_categories();