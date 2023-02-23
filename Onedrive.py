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

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def admin():
    for items in os.listdir():
        if(".idea" in items):
            st.write(os.getcwd() + '\\' + items  + " (" + f'{round(os.stat(items).st_size / 1024,2)}' + " KB)")
        elif(".git" in items):
            st.write(os.getcwd() + '\\' + items  + " (" + f'{round(os.stat(items).st_size / 1024,2)}' + " KB)")
        elif(".streamlit" in items):
            st.write(os.getcwd() + '\\' + items  + " (" + f'{round(os.stat(items).st_size / 1024,2)}' + " KB)")
        else:
            with open(items, "rb") as file:
                btn = st.download_button(
                    label=os.getcwd() + '\\' + items  + " (" + f'{round(os.stat(items).st_size / 1024,2)}' + " KB)",
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
    file = st.multiselect("Choose the file you want to delete",options=files)
    if(st.button("Delete")):
        if(file):
            if("--Select--" not in file):
                for element in file:
                    os.remove(element)
                    st.warning(element + " Deleted Successfully")

st.header("Onedrive")
size = 0
for item in os.listdir():
    size += os.stat(item).st_size / (1024 * 1024)
st.subheader(f'{round(800 - size,2)}' + " MB remaining")
st.write("---")
files = st.file_uploader("Upload your files to drive",accept_multiple_files=True)
if(files):
    for file in files:
        if(file.size / (1024*1024) < round(800-size,2)):
            with open(file.name,"wb") as f:
                f.write(file.read())
            size += file.size / (1024*1024)
        else:
            st.error("You have crossed your storage limit")
    st.write("Total Size: " + str(size))
    st.subheader(f'{round(800 - size, 2)}' + " MB remaining")
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
