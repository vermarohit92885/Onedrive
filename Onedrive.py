import streamlit as st
import bcrypt
import os

st.set_page_config(page_title='Onedrive',layout="wide",page_icon="https://iconarchive.com/download/i87068/graphicloads/colorful-long-shadow/Cloud.ico")

hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                header {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
set_background = """
                <style>
                .stApp {
                     background-image: url("https://static.vecteezy.com/system/resources/previews/002/091/724/non_2x/abstract-technology-background-with-big-data-internet-connection-abstract-sense-of-science-and-technology-analytics-concept-graphic-design-illustration-vector.jpg");
                     background-size: cover;
                }
                </style>
                """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.markdown(set_background, unsafe_allow_html=True)
def admin():
    st.success("Successfully logged in as admin")
    for items in os.listdir():
        if(".idea" in items):
            st.write(items)
        else:
            with open(items, "rb") as file:
                btn = st.download_button(
                    label=os.getcwd() + '\\' + items,
                    data=file,
                    file_name=items,
                    mime="application/octet-stream"
                )
    files = ["--Select--"]
    for items in os.listdir():
        if (".idea" in items):
            pass
        elif ("requirements.txt" in items):
            pass
        elif (".py" in items):
            pass
        else:
            files.append(items)
    file = st.selectbox("Choose the file you want to delete",options=files)
    if(file != "--Select--"):
        os.remove(file)
        st.success("Deleted successully")

st.header("Onedrive")
st.write("---")
file = st.file_uploader("Upload your files to drive")
if(file):
    with open(file.name,"wb") as f:
        f.write(file.read())
if(st.button("Show files in drive")):
    for items in os.listdir():
        st.write(os.getcwd() + "\\" + items)
st.sidebar.header("Admin Portal")
id = st.sidebar.text_input(label="Username")
password = bytes(st.sidebar.text_input(label="Password",type="password"),"utf-8")
true_password = bytes("PassHash@2023","utf-8")
if(password and id):
    salt = bcrypt.gensalt()
    password = bcrypt.hashpw(password,salt)
    true_password = bcrypt.hashpw(true_password,salt)
    with st.expander("Admin"):
        if(password == true_password):
            admin()
        else:
            st.sidebar.error("Incorrect password!")