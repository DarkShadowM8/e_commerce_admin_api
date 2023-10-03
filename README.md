# e-commerce_admin_api
An E-commerce admin api based on python framework FastApi


## **Install before run:**
pip3 install fastapi\
pip3 isntall uvicorn\
pip3 install sqlalchemy\
pip3 install mysql-connector  

## to run
open command promt in e-commerce_admin_api\
run command `uvicorn main:app --reload`

## Endpoints:

### `/product`: for all product endpoints
`/add-product`  to add a product and requirements are \
    name: str\
    description: str\
    cost_rate: float\
    selling_rate: float
    
`/get-all-products`  it'll return all the products\
`/get-product-name/{name}`  to get a product by it's name\
`/get-product/{id}`  to get a product by it's id\
`/filter-product-by-category/{id}` to get a product by it's category require is an id\
`/update-product-category`  to add a category or update in product require a json object with:\
    category_id: int\
    product_id: int

### `/category`: for all category endpoint
`/add`  to add a category require a JSON object:\
    name: str\
    desc: str
    
`/get-by-name/{name}`  to get the category by it's name\
`/get-by-id/{id}`  to get the category by it's id\
`/get-all`  it'll return all the category

### `/inventory`: for all inventory endpoints
`/add-units-in-inventory`  it'll add product in inventory and update when new products with existing id add\
`/update-sold-units-in-inventory`  it'll update the inventory with sold units\
`/get-inventory`  it'll fetch the whole inventory\
`/get-inventory/{id}`  it'll fetch specific product's inventory\

### `/sale`: for all sale endpoint
`/add-a-sale`   to add a sale\
`/get-sales-by-category/{id}`   to get a sale by category requires an id in the parameter\
`/get-daily-sales`   to get daily total sale record\
`/get-monthly-sales`   to get monthly total sale record\
`/get-yearly-sales`   to get yearly sale record\
`/get-sale` to get record of any date require a JSON object of three int (day, month, year)

### `/revenue`
`/get-total-revenue`  it'll return total revenue\
`/get-product-revenue/{id}`  it'll return revenue generated by a specific product\
`/get-revenue-by-single-category`  it'll return revenue of a single category\
`/get-revenue-by-categories`  it'll return categories with there generated revenue\
