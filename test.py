from cryptography.fernet import Fernet
import streamlit as st

password = st.text_input("Password: ")

submit = st.button("Submit")
if submit:
    key = Fernet.generate_key()
    fernet = Fernet(key)

    encMessage = fernet.encrypt(password.encode())

    st.write("String yang dienkripsi: ", '\n', encMessage)

    decMessage = fernet.decrypt(encMessage).decode()

    st.write("String yang didekripsi: ", '\n', decMessage)
