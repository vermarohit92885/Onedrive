import base64
import firebase_admin
from firebase_admin import credentials,db
import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
import os

if not firebase_admin._apps:
    cred = credentials.Certificate("credentials.json")
    firebase_admin.initialize_app(cred,{"databaseURL":"https://onedrive-12e98-default-rtdb.firebaseio.com/"})

st.set_page_config(page_title='Onedrive',layout="wide",page_icon="https://iconarchive.com/download/i87068/graphicloads/colorful-long-shadow/Cloud.ico")

ref = db.reference("/")

hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                header {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def KBMBGB(filesize):
    return_val = str(round(filesize,2)) + " B"
    if (filesize >= 1000):
        filesize = filesize / 1024
        return_val =  str(round(filesize,2)) + " KB"
    if(filesize >= 1000):
        filesize = filesize/1024
        return_val = str(round(filesize,2)) + " MB"
    if (filesize >= 1000):
        filesize = filesize / 1024
        return_val = str(round(filesize,2)) + " GB"
    return return_val

def admin():
    for items in os.listdir():
        if(".idea" in items):
            st.write(os.getcwd() + '\\' + items  + " (" + f'{KBMBGB(os.stat(items).st_size)}' + ")")
        elif(".git" in items):
            st.write(os.getcwd() + '\\' + items  + " (" + f'{KBMBGB(os.stat(items).st_size)}' + ")")
        elif(".streamlit" in items):
            st.write(os.getcwd() + '\\' + items  + " (" + f'{KBMBGB(os.stat(items).st_size)}' + ")")
        elif ("Onedrive.py" in items):
            st.write(os.getcwd() + '\\' + items + " (" + f'{KBMBGB(os.stat(items).st_size)}' + ")")
        elif ("credentials.json" in items):
            st.write(os.getcwd() + '\\' + items + " (" + f'{KBMBGB(os.stat(items).st_size)}' + ")")
        elif(".mp4" in items or '.avi' in items):
            with open(items, "rb") as file:
                btn = st.download_button(
                    label=os.getcwd() + '\\' + items + " (" + f'{KBMBGB(os.stat(items).st_size)}' + ")",
                    data=file,
                    file_name=items,
                    mime="application/octet-stream"
                )
            st.video(items)
        elif (".mp3" in items or '.wav' in items):
            with open(items, "rb") as file:
                btn = st.download_button(
                    label=os.getcwd() + '\\' + items + " (" + f'{KBMBGB(os.stat(items).st_size)}' + ")",
                    data=file,
                    file_name=items,
                    mime="application/octet-stream"
                )
            st.audio(items)
        elif (".jpg" in items or '.jpeg' in items or '.png' in items):
            with open(items, "rb") as file:
                btn = st.download_button(
                    label=os.getcwd() + '\\' + items + " (" + f'{KBMBGB(os.stat(items).st_size)}' + ")",
                    data=file,
                    file_name=items,
                    mime="application/octet-stream"
                )
            st.image(items)
        elif (".txt" in items):
            with open(items, "rb") as file:
                btn = st.download_button(
                    label=os.getcwd() + '\\' + items + " (" + f'{KBMBGB(os.stat(items).st_size)}' + ")",
                    data=file,
                    file_name=items,
                    mime="application/octet-stream"
                )
            if(st.button("View " + items)):
                with open(items,'r') as contents:
                    st.code(contents.read())
        elif (".py" in items and 'Onedrive.py' not in items):
            with open(items, "rb") as file:
                btn = st.download_button(
                    label=os.getcwd() + '\\' + items + " (" + f'{KBMBGB(os.stat(items).st_size)}' + ")",
                    data=file,
                    file_name=items,
                    mime="application/octet-stream"
                )
            if(st.button("View " + items)):
                with open(items,'r') as contents:
                    st.code(contents.read(),language="py")
        elif (".json" in items and 'credentials.json' not in items):
            with open(items, "rb") as file:
                btn = st.download_button(
                    label=os.getcwd() + '\\' + items + " (" + f'{KBMBGB(os.stat(items).st_size)}' + ")",
                    data=file,
                    file_name=items,
                    mime="application/octet-stream"
                )
            if(st.button("View " + items)):
                with open(items,'r') as contents:
                    st.code(contents.read(),language="py")
        elif (".java" in items):
            with open(items, "rb") as file:
                btn = st.download_button(
                    label=os.getcwd() + '\\' + items + " (" + f'{KBMBGB(os.stat(items).st_size)}' + ")",
                    data=file,
                    file_name=items,
                    mime="application/octet-stream"
                )
            if(st.button("View " + items)):
                with open(items,'r') as contents:
                    st.code(contents.read(),language="java")
        elif (".c" in items or ".cpp" in items or ".ino" in items):
            with open(items, "rb") as file:
                btn = st.download_button(
                    label=os.getcwd() + '\\' + items + " (" + f'{KBMBGB(os.stat(items).st_size)}' + ")",
                    data=file,
                    file_name=items,
                    mime="application/octet-stream"
                )
            if (st.button("View " + items)):
                with open(items, 'r') as contents:
                    st.code(contents.read(), language="c")
        elif (".html" in items):
            with open(items, "rb") as file:
                btn = st.download_button(
                    label=os.getcwd() + '\\' + items + " (" + f'{KBMBGB(os.stat(items).st_size)}' + ")",
                    data=file,
                    file_name=items,
                    mime="application/octet-stream"
                )
            if(st.button("View " + items)):
                with open(items,'r') as contents:
                    st.code(contents.read(),language="html")
        elif (".pdf" in items):
            with open(items, "rb") as file:
                btn = st.download_button(
                    label=os.getcwd() + '\\' + items + " (" + f'{KBMBGB(os.stat(items).st_size)}' + ")",
                    data=file,
                    file_name=items,
                    mime="application/octet-stream"
                )
            if(st.button("View " + items)):
                pdf_viewer(items)
        else:
            with open(items, "rb") as file:
                btn = st.download_button(
                    label=os.getcwd() + '\\' + items  + " (" + f'{KBMBGB(os.stat(items).st_size)}' + ")",
                    data=file,
                    file_name=items,
                    mime="application/octet-stream"
                )
    files = ["--Select--"]
    for items in os.listdir():
        if (".idea" in items):
            pass
        elif ("Onedrive.py" in items):
            pass
        elif (".git" in items):
            pass
        elif (".streamlit" in items):
            pass
        elif ("requirements.txt" in items):
            pass
        elif ("credentials.json" in items):
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
    size += os.stat(item).st_size
remsize = 838860800-size
st.subheader(f'{KBMBGB(remsize)}' + " remaining")
st.write("---")
files = st.file_uploader("Upload your files to drive",accept_multiple_files=True)
file_size = 0
if(files):
    for file in files:
        if(file.size < (remsize-file_size)):
            with open(file.name,"wb") as f:
                f.write(file.read())
            file_size += file.size
        else:
            st.error("You have crossed your storage limit")
    st.write("Total Size: " + str(KBMBGB(file_size)))
    remsize = 838860800 - file_size
    st.subheader(f'{KBMBGB(remsize)}' + " remaining")
if(st.button("Show files in drive")):
    for items in os.listdir():
        st.write(os.getcwd() + "\\" + items)
st.sidebar.header("Admin Portal")
id = st.sidebar.text_input(label="Username")
password = hash(st.sidebar.text_input(label="Password",type="password"))
forget_password = st.sidebar.write("[Forget Password](https://onedrive-12e98-default-rtdb.firebaseio.com/)")
true_password = hash(ref.get()['Password'])
if(password and id):
    if(password == true_password and ref.get()['Id'].lower() in id.lower()):
        st.sidebar.success("Welcome "+ref.get()['Id'])
        with st.expander("Admin"):
            admin()
    else:
        st.sidebar.error("Incorrect password")
