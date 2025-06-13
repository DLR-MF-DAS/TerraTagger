import streamlit as st

if __name__ == '__main__':
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    user_input = st.text_input("Say something:")
    if st.button("Send") and user_input:
        st.session_state.messages.append(user_input)
    st.write("Chat history:")
    for msg in st.session_state.messages:
        st.write(f"👤 {msg}")

