from collections import OrderedDict
from typing import Optional

from .models import ProductCreateModel, ProductModel


class InMemoryStorage:
    """インメモリデータストレージ"""

    def __init__(self) -> None:
        self._products: OrderedDict[int, ProductModel] = OrderedDict()
        self._next_id = 1

    def create_product(self, product_create: ProductCreateModel) -> ProductModel:
        """新しい商品を保存する"""
        new_product = ProductModel(
            id=self._next_id, **product_create.model_dump()
        )
        self._products[self._next_id] = new_product
        self._next_id += 1
        return new_product

    def get_product_by_id(self, product_id: int) -> Optional[ProductModel]:
        """IDで商品を検索する"""
        return self._products.get(product_id)
