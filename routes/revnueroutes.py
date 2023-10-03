from services import revnueService
from schemas import sales
from fastapi import APIRouter, Query

revenueRouter = APIRouter()

@revenueRouter.get("/get-total-revenue")
def total_revnue():
    return revnueService.total_revenue()

@revenueRouter.get("/get-product-revenue/{id}")
def single_product_revenue(id: int):
    return revnueService.single_product_revenue(id)

@revenueRouter.get("/get-revenue-by-single-category")
def get_revenue_by_category(name: str):
    return revnueService.get_revenue_for_category(name)

@revenueRouter.get("/get-revenue-by-categories")
def get_revenue_by_category():
    return revnueService.revenue_by_categories()