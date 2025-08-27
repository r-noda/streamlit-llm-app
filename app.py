
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

load_dotenv()

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

st.title("AI相談アプリ")
st.write("相談内容とカテゴリを選択するとAIが回答します。")

selected_item = st.radio(
    "相談内容のカテゴリを選択してください。",
    ["英語", "数学", "音楽", "プログラミング"]
)

st.divider()

def get_llm_response(input_text, category):
    system_messages = {
        "英語": "あなたは英語の専門家です.",
        "数学": "あなたは数学の専門家です.",
        "音楽": "あなたは音楽の専門家です.",
        "プログラミング": "あなたはプログラミングの専門家です."
    }
    messages = [
        SystemMessage(content=system_messages[category]),
        HumanMessage(content=input_text),
    ]
    return llm(messages)

input_message = st.text_input(label="相談内容を入力してください。")
if selected_item == "英語":
    result = get_llm_response(input_message, selected_item)

elif selected_item == "数学":
    result = get_llm_response(input_message, selected_item)

elif selected_item == "音楽":
    result = get_llm_response(input_message, selected_item)

elif selected_item == "プログラミング":
    result = get_llm_response(input_message, selected_item)


if st.button("回答"):
    result = get_llm_response(input_message, selected_item)
    st.divider()
    st.write(f"回答: **{result}**")