import streamlit as st
import datetime
import requests
import sys

BASE_URL = "http://localhost:8000" # Backend endpoints


st.set_page_config(
    page_title= "Tavel Planner Agentic Application",
    page_icon = "🌍",
    layout="centered",
    initial_sidebar_state="expanded",
)


st.title("🌍 Travel Planner Agentic Application")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messagess = []

# Display chat history
st.header("How can I help you in planning a trip? let me know where do you want to visit.")

# Chat input box at bottom
with st.form(key="query_form", clear_on_submit=True):
    user_input = st.text_input("User Input", placeholder="e.g. Plan a trip to Goa for 5 days")
    submit_button = st.form_submit_button("send")

if submit_button and user_input.strip():
    try:
        # Show user message
        # Show thinking spinner while backing processes
        with st.spinner("Bot is thinking..."):
            payload = {"question": user_input}
            response = requests.post(f"{BASE_URL}/query", json=payload)

        if response.status_code == 200:
            answer = response.json().get("answer", "No answer returned.")
            markdown_content = f"""# 🌍 AI Travel Plan

            # **Generated:** {datetime.datetime.now().strftime('%Y-%m-%d at %H:%M')}
            # **created by:** ATG


            ---

            {answer}


            ---

            *This travel plan was geenrated by AI. Please verify all information, especially prices, operatiing hours, and travel requirements before your trip.*
            """

            st.markdown(markdown_content)

        else:
            st.error("Bot failed to respond:" + response.text)

    
    except Exception as e:
        raise f"The response failed due to {e}"



