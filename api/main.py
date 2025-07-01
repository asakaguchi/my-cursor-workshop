from fastapi import FastAPI, status

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
