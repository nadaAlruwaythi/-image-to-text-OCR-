
import streamlit as st
import easyocr as ocr  # OCR
import streamlit as st  # Web App
from PIL import Image  # Image Processing
import numpy as np  # Image Processing
import os

st.markdown("")
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.markdown("""
<style>
body {
  background: #eff3f4; 
  background: -webkit-linear-gradient(to right, #eedff1, #101212); 
  background: linear-gradient(to right, #eedff1, #101212); 
  text-align:center;
}
</style>
    """, unsafe_allow_html=True)

def app():
    st.title('English')
    st.caption('To Extract English Text From Images ')

    # image uploader
    image = st.file_uploader(label="Upload your image here", type=['png', 'jpg', 'jpeg'])
    reader = ocr.Reader(['en'], model_storage_directory='.')
    if image is not None:
        input_image = Image.open(image)  # read image
        st.image(input_image)  # display image
        result = reader.readtext(np.array(input_image))
        result_text = []  # empty list for results
        for text in result:
            result_text.append(text[1])
        with st.form("Result"):
            result = st.text_area("TEXT", value=result_text)
            d_btn = st.form_submit_button("Download")
            if d_btn:
                envir_var = os.environ
                usr_loc = envir_var.get('USERPROFILE')
                loc = usr_loc + "\Downloads\\transcript.txt"
                with open(loc, 'w') as file:
                    file.write(result)
        st.balloons()



    st.caption("Made with ❤️ by Nada")