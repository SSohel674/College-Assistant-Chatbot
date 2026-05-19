import streamlit as st
from chatbot import get_response
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="College Assistant Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Title
st.title("🤖 AI-Powered College Assistant Chatbot")

st.caption("Powered by NLP and AI-based Query Processing")

# Sidebar
st.sidebar.header("📌 Features")

st.sidebar.info("""
- NLP-based chatbot
- Automated responses
- Student support system
- Real-time interaction
- AI-powered query handling
- Chat history with timestamps
""")

# Description
st.markdown("""
Ask questions related to:

- Admissions
- Attendance
- Exams
- Fees
- Departments
- Hostel
- Library
- Placement
- Sports
""")

# User Input
user_input = st.text_input("Enter your question")

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Ask Button
if st.button("Ask"):

    if user_input.strip() != "":

        response = get_response(user_input)

        # Current Time
        current_time = datetime.now().strftime("%H:%M:%S")

        # Store User Message
        st.session_state.messages.append(
            ("You", user_input, current_time)
        )

        # Store Bot Response
        st.session_state.messages.append(
            ("Bot", response, current_time)
        )

    else:
        st.warning("Please enter a question.")

# Display Chat History
st.subheader("💬 Conversation")

for sender, message, time in st.session_state.messages:

    if sender == "You":

        st.write(f"🧑 You ({time}): {message}")

    else:

        st.success(f"🤖 Bot ({time}): {message}")

# Future Enhancements
st.subheader("🔮 Future Enhancements")

st.markdown("""
Later versions of the project can include:

- 🎤 Voice input support
- 🤖 LLM integration
- 📄 PDF question answering
- 🗄 Database storage
- 💬 Advanced chat history
- 🔐 Login and authentication system
""")

# Footer
st.markdown("---")
st.markdown("### 🚀 Developed by Shaik Sohel")
st.markdown("M.Tech | Data Science & AI Enthusiast")