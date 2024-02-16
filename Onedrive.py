import base64
import firebase_admin
from firebase_admin import credentials,db
import streamlit as st
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

def admin():
    for items in os.listdir():
        if(".idea" in items):
            st.write(os.getcwd() + '\\' + items  + " (" + f'{round(os.stat(items).st_size / 1024,2)}' + " KB)")
        elif(".git" in items):
            st.write(os.getcwd() + '\\' + items  + " (" + f'{round(os.stat(items).st_size / 1024,2)}' + " KB)")
        elif(".streamlit" in items):
            st.write(os.getcwd() + '\\' + items  + " (" + f'{round(os.stat(items).st_size / 1024,2)}' + " KB)")
        elif ("Onedrive.py" in items):
            st.write(os.getcwd() + '\\' + items + " (" + f'{round(os.stat(items).st_size / 1024, 2)}' + " KB)")
        elif ("credentials.json" in items):
            st.write(os.getcwd() + '\\' + items + " (" + f'{round(os.stat(items).st_size / 1024, 2)}' + " KB)")
        elif(".mp4" in items or '.avi' in items):
            with open(items, "rb") as file:
                btn = st.download_button(
                    label=os.getcwd() + '\\' + items + " (" + f'{round(os.stat(items).st_size / 1024, 2)}' + " KB)",
                    data=file,
                    file_name=items,
                    mime="application/octet-stream"
                )
            st.video(items)
        elif (".mp3" in items or '.wav' in items):
            with open(items, "rb") as file:
                btn = st.download_button(
                    label=os.getcwd() + '\\' + items + " (" + f'{round(os.stat(items).st_size / 1024, 2)}' + " KB)",
                    data=file,
                    file_name=items,
                    mime="application/octet-stream"
                )
            st.audio(items)
        elif (".jpg" in items or '.jpeg' in items or '.png' in items):
            with open(items, "rb") as file:
                btn = st.download_button(
                    label=os.getcwd() + '\\' + items + " (" + f'{round(os.stat(items).st_size / 1024, 2)}' + " KB)",
                    data=file,
                    file_name=items,
                    mime="application/octet-stream"
                )
            st.image(items)
        elif (".txt" in items):
            with open(items, "rb") as file:
                btn = st.download_button(
                    label=os.getcwd() + '\\' + items + " (" + f'{round(os.stat(items).st_size / 1024, 2)}' + " KB)",
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
                    label=os.getcwd() + '\\' + items + " (" + f'{round(os.stat(items).st_size / 1024, 2)}' + " KB)",
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
                    label=os.getcwd() + '\\' + items + " (" + f'{round(os.stat(items).st_size / 1024, 2)}' + " KB)",
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
                    label=os.getcwd() + '\\' + items + " (" + f'{round(os.stat(items).st_size / 1024, 2)}' + " KB)",
                    data=file,
                    file_name=items,
                    mime="application/octet-stream"
                )
            if(st.button("View " + items)):
                with open(items,'r') as contents:
                    st.code(contents.read(),language="java")
        elif (".html" in items):
            with open(items, "rb") as file:
                btn = st.download_button(
                    label=os.getcwd() + '\\' + items + " (" + f'{round(os.stat(items).st_size / 1024, 2)}' + " KB)",
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
                    label=os.getcwd() + '\\' + items + " (" + f'{round(os.stat(items).st_size / 1024, 2)}' + " KB)",
                    data=file,
                    file_name=items,
                    mime="application/octet-stream"
                )
            if(st.button("View " + items)):
                # Opening file from file path
                with open(items, "rb") as f:
                    base64_pdf = base64.b64encode(f.read()).decode('utf-8')

                # Embedding PDF in HTML
                pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'

                # Displaying File
                st.markdown(pdf_display, unsafe_allow_html=True)
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
true_password = hash(ref.get()['Password'])
if(password and id):
    if(password == true_password and id == ref.get()['Id']):
        st.sidebar.success("Welcome "+ref.get()['Id'])
        with st.expander("Admin"):
            admin()
    else:
        st.sidebar.error("Incorrect password")
