import pytest
from httpx import ASGITransport, AsyncClient

from api.main import app


@pytest.mark.anyio
async def test_health_check_returns_200():
    """/health エンドポイントはステータスコード 200 を返す"""
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.get("/health")
    assert response.status_code == 200


@pytest.mark.anyio
async def test_create_product_returns_201():
    """POST /items はステータスコード 201 を返す"""
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.post("/items", json={"name": "テスト商品", "price": 1000})
    assert response.status_code == 201
