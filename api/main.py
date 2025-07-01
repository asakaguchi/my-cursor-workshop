from fastapi import FastAPI, status, HTTPException

from .models import ProductCreateModel, ProductModel
from .storage import InMemoryStorage

app = FastAPI(title="商品管理API")
storage = InMemoryStorage()

@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check() -> dict[str, str]:
    """ヘルスチェック用エンドポイント"""
    return {"status": "ok"}

@app.post(
    "/items", response_model=ProductModel, status_code=status.HTTP_201_CREATED
)
async def create_product(product: ProductCreateModel) -> ProductModel:
    """商品作成エンドポイント"""
    return storage.create_product(product)

@app.get("/items/{product_id}", response_model=ProductModel)
async def get_product(product_id: int) -> ProductModel:
    """商品取得エンドポイント"""
    product = storage.get_product_by_id(product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )
    return product
