import streamlit as st
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
    for items in os.listdir():
        if(".idea" in items):
            st.write(os.getcwd() + '\\' + items  + " (" + f'{os.stat(items).st_size / (1024 * 1024)}' + " MB)")
        elif(".git" in items):
            st.write(os.getcwd() + '\\' + items  + " (" + f'{os.stat(items).st_size / (1024 * 1024)}' + " MB)")
        elif(".streamlit" in items):
            st.write(os.getcwd() + '\\' + items  + " (" + f'{os.stat(items).st_size / (1024 * 1024)}' + " MB)")
        else:
            with open(items, "rb") as file:
                btn = st.download_button(
                    label=os.getcwd() + '\\' + items  + " (" + f'{os.stat(items).st_size / (1024 * 1024)}' + " MB)",
                    data=file,
                    file_name=items,
                    mime="application/octet-stream"
                )
    files = ["--Select--"]
    for items in os.listdir():
        if (".idea" in items):
            pass
        elif (".py" in items):
            pass
        elif (".git" in items):
            pass
        elif (".streamlit" in items):
            pass
        else:
            files.append(items)
    file = st.selectbox("Choose the file you want to delete",options=files)
    if(file != "--Select--"):
        os.remove(file)
        st.success("Deleted successully")

st.header("Onedrive")
size = 0
for item in os.listdir():
    size += os.stat(item).st_size / (1024 * 1024)
st.subheader(f'{round(800 - size,1)}' + " MB remaining")
st.write("---")
file = st.file_uploader("Upload your files to drive")
if(file):
    if(file.size / (1024*1024) < round(800-size)):
        with open(file.name,"wb") as f:
            f.write(file.read())
    else:
        st.error("You have crossed your storage limit")
if(st.button("Show files in drive")):
    for items in os.listdir():
        st.write(os.getcwd() + "\\" + items)
st.sidebar.header("Admin Portal")
id = st.sidebar.text_input(label="Username")
password = hash(st.sidebar.text_input(label="Password",type="password"))
true_password = hash("PassFile@2023#")
if(password and id):
    if(password == true_password):
        st.sidebar.success("Logged in as admin")
        with st.expander("Admin"):
            admin()
    else:
        st.sidebar.error("Incorrect password")
