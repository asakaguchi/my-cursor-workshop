import streamlit as st

st.title("かんたん商品管理ツール")

# --- 商品登録機能 ---
st.header("商品の新規登録")
name = st.text_input("商品名")
price = st.number_input("価格（円）", min_value=1, step=1)
if st.button("登録する"):
    # TODO: API連携を実装
    st.info(f"（開発中）商品名: {name}, 価格: {price}")
