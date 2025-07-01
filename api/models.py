from datetime import datetime

from pydantic import BaseModel, Field


class ProductCreateModel(BaseModel):
    """商品作成リクエストモデル"""

    name: str = Field(..., min_length=1, description="商品名")
    price: float = Field(..., gt=0, description="単価")


class ProductModel(ProductCreateModel):
    """商品データモデル"""

    id: int = Field(..., description="商品ID")
    created_at: datetime = Field(default_factory=datetime.now, description="作成日時")
