from fastapi import FastAPI, Query
from services.products import get_all_products
from pyndatic.patient import Patient, patient_data

app = FastAPI()


@app.get("/")
def root():
    patient_info = {"name": "kalpesh", "age": 25}
    patient1 = Patient(**patient_info)
    return patient1 
    # return patient_data(patient=patient1)


@app.get("/products/{id}")
def get_products(id: int):
    products = ["Mouse", "Laptop", "Keyboard", "Pen"]
    return products[id]


@app.get("/products/")
def get_products_all():
    return get_all_products()


@app.get("/product_query")
def list_products(
    name: str = Query(default=None, min_length=1, max_length=50),
    sort_by_products: bool = Query(default=False, description="Sort products"),
    order: str = Query(default="asc"),
    limit: int = Query(default=10, ge=1, le=100),
):
    products = get_all_products()

    if name:
        needle = name.strip().lower()
        products = [p for p in products if needle in p.get("name", "").lower()]

    if sort_by_products:
        reverse = order == "desc"
        products = sorted(products, key=lambda p: p.get("price", 0), reverse=reverse)

    total = len(products)
    products = products[0:limit]
    return {"total": total, "limit": limit, "products": products}
