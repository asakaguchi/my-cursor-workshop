import httpx
import streamlit as st

API_BASE_URL = "http://localhost:8000"

st.title("かんたん商品管理ツール")

# --- 商品登録機能 ---
st.header("商品の新規登録")
name = st.text_input("商品名")
price = st.number_input("価格（円）", min_value=1, step=1)
if st.button("登録する"):
    if name and price > 0:
        try:
            response = httpx.post(
                f"{API_BASE_URL}/items",
                json={"name": name, "price": price},
                timeout=5,
            )
            response.raise_for_status()  # HTTPエラーがあれば例外を発生させる
            product = response.json()
            st.success(f"商品を登録しました。商品ID: {product['id']}")
        except httpx.HTTPStatusError as e:
            st.error(f"APIエラー: {e.response.status_code} - {e.response.text}")
        except httpx.RequestError as e:
            st.error(f"リクエストエラー: {e}")
    else:
        st.warning("商品名と価格を入力してください。")

# --- 商品検索機能 ---
st.header("商品の情報検索")
product_id = st.number_input("商品ID", min_value=1, step=1)
if st.button("検索する"):
    try:
        response = httpx.get(f"{API_BASE_URL}/items/{product_id}", timeout=5)
        response.raise_for_status()
        product = response.json()
        st.subheader("検索結果")
        st.write(f"**ID:** {product['id']}")
        st.write(f"**商品名:** {product['name']}")
        st.write(f"**価格:** {product['price']} 円")
        st.write(f"**登録日時:** {product['created_at']}")
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            st.error(f"商品ID {product_id} は見つかりませんでした。")
        else:
            st.error(f"APIエラー: {e.response.status_code} - {e.response.text}")
    except httpx.RequestError as e:
        st.error(f"リクエストエラー: {e}")
