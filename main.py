from fastapi import FastAPI
from routes import productroutes, categoryroutes, inventoryroutes, saleroutes, revnueroutes
from services import enter_raw_data_service
from database import database
app = FastAPI()

enter_raw_data_service.generate_demo_data()

app.include_router(productroutes.productRouter, prefix="/product")
app.include_router(categoryroutes.categoryRouter, prefix="/category")
app.include_router(inventoryroutes.inventoryRouter, prefix="/inventory")
app.include_router(saleroutes.saleRouter, prefix="/sale")
app.include_router(revnueroutes.revenueRouter, prefix="/revenue")
