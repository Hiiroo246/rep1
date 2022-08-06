from cryptography.fernet import Fernet
import streamlit as st

st.write("Password atau kata sandi adalah mekanisme keamanan dasar yang terdiri dari frase tahap rahasia yang dibuat dengan menggunakan karakter alfabet, numerik, alfanumerik dan simbolik, atau kombinasi. \n\n Mekanisme keamanan yang digunakan pada password adalah dengan teknik enkripsi. \n\n Enkripsi adalah teknik merubah informasi awal (password) ke dalam bentuk yang tidak terbaca dan dapat dibaca kembali dengan bantuan key (kunci). Secara sederhana, yang mengetahui isi dari password hanyalah programmer yang membuat sistem key-enkripsi-dekripsi")

password = st.text_input("Password: ")

submit = st.button("Submit")
if submit:
    key = Fernet.generate_key()
    fernet = Fernet(key)

    encMessage = fernet.encrypt(password.encode())

    st.write("String yang dienkripsi: ", '\n', encMessage)

    decMessage = fernet.decrypt(encMessage).decode()

    st.write("String yang didekripsi: ", '\n', decMessage)
    
st.write("Pada demo app tersebut diperlihatkan bagaimana cara kerja sederhana dari teknik enkripsi password. Enkripsi dibuat untuk tujuan keamanan dan teknik enkripsi tidak hanya digunakan pada mekanisme password tetapi juga dapat digunakan untuk keperluan keamanan lainnya, seperti contoh yang biasa kita gunakan sehari-hari yaitu aplikasi chat WhatsApp, Telegram dsb \n\n Dengan adanya enkripsi, password yang digunakan akan menjadi lebih tinggi tingkat keamanannya, dan data yang di dalamnya akan tetap terlindungi")
