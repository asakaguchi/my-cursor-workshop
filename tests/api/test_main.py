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


@pytest.mark.anyio
async def test_get_product_with_existing_id_returns_200():
    """GET /items/{id} は存在するIDの場合、ステータスコード 200 を返す"""
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        # 準備: テスト用の商品を作成
        create_response = await client.post(
            "/items", json={"name": "テスト商品", "price": 1000}
        )
        product_id = create_response.json()["id"]

        # 実行
        get_response = await client.get(f"/items/{product_id}")

    # 検証
    assert get_response.status_code == 200
    assert get_response.json()["id"] == product_id
    assert get_response.json()["name"] == "テスト商品"


@pytest.mark.anyio
async def test_get_product_with_non_existing_id_returns_404():
    """GET /items/{id} は存在しないIDの場合、ステータスコード 404 を返す"""
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.get("/items/999")  # 存在しないID
    assert response.status_code == 404
