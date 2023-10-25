import time

import numpy as np

import streamlit as st

from PIL import Image

import shutil
import requests

def save_file(url: str, filename: str) -> None:
    response = requests.get(url, stream=True)

    try:
        with open(f"cats/{filename}", 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
    except Exception as error:
        print("Save File Failed:".format(error))

def multicat_demo():
    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()

    for i in range(1, 11):
        # Get a cat
        save_file("https://cataas.com/cat", f"{i}.png")
        
        status_text.text(f"{i*10}% Complete")
        progress_bar.progress(i*10)
        time.sleep(0.05)

        image = Image.open(f"cats/{i}.png")
        st.image(image)
    
    progress_bar.empty()

    # Streamlit widgets automatically run the script from top to bottom. Since
    # this button is not connected to any other logic, it just causes a plain
    # rerun.
    st.button("Re-run")


st.set_page_config(page_title="MultiCat Demo", page_icon="📈")
st.markdown("# MultiCat Demo")
st.sidebar.header("MultiCat Demo")

multicat_demo()
