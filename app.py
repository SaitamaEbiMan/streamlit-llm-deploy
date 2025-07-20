import streamlit as st
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage


load_dotenv()


st.title("LLMサンプルアプリ")
st.write("### 使用方法")
st.write("以下の専門家の中から一人を選び、その専門家から回答を得ることができます。")
st.write("##### 専門家1: プログラミングの専門家")
st.write("##### 専門家2: 健康とフィットネスの専門家")
expert_type = st.radio(
    "専門家の種類を選択してください",
    options=["A: プログラミングの専門家", "B: 健康とフィットネスの専門家"]
)

input_message = st.text_input(label="専門家に聞きたいことを入力してください")


if expert_type == "A: プログラミングの専門家":
    system_message = "あなたはプログラミングの専門家です。"
elif expert_type == "B: 健康とフィットネスの専門家":
    system_message = "あなたは健康とフィットネスの専門家です。"


# LLM用関数
def get_llm_response(input_msg, system_msg):
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

    messages = [
        SystemMessage(content=system_msg),
        HumanMessage(content=input_msg)
    ]

    result = llm(messages)
    print(result.content)
    return result.content


if st.button("実行"):
    st.write(f"LLM返答: **{get_llm_response(input_message, system_message)}**")