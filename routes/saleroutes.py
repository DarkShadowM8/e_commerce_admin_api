import datetime

from services import saleService
from schemas import sales
from fastapi import APIRouter


saleRouter = APIRouter()

@saleRouter.post("/add-a-sale")
def add_a_sale(request: sales.Sale):
    return  saleService.add_a_sale(request)

@saleRouter.get("/get-sales-by-category/{id}")
async def get_sales_by_category(id: int):
    return saleService.get_sales_by_category(id)

@saleRouter.get("/get-daily-sales")
async def get_daily_sales():
    return saleService.get_daily_sales()

@saleRouter.get("/get-monthly-sales")
async def get_monthly_sales(month: int):
    return saleService.get_monthly_sales(month)

@saleRouter.get("/get-yearly-sales")
async def get_yearly_sales(year: int):
    return saleService.get_yearly_sales(year)

@saleRouter.get("/get-sale")
async def get_sale_on_date(day:int, month:int ,year: int):
    return saleService.get_sale_on_date(day, month, year)