from fastapi import APIRouter
from schemas import product
from services import productService
from adapters import convertor

productRouter = APIRouter()


@productRouter.post("/add-product")
def add_product(request: product.Product):
    productService.add_product(convertor._toProduct(request))
    return "Product with name: " + request.description + " added!!!"


@productRouter.get("/get-all-products")
def get_all_products():
    return productService.get_all_products()


@productRouter.get("/get-product-name/{name}")
def get_product_by_name(name: str):
    return productService.get_product_by_name(name)


@productRouter.get("/get-product/{id}")
def get_product_by_id(id: int):
    return productService.get_product_by_id(id)


@productRouter.get("/filter-product-by-category/{id}")
def filter_product_by_category(id: int):
    return productService.filter_product_by_category(id)


@productRouter.patch("/update-product-category")
def update_product_category(cat_id: int, product_id: int):
    return productService.update_product_category(cat_id, product_id)