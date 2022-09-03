import streamlit as st
from multiapp import MultiApp
from apps import English, Arabic # import your app modules here
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

app = MultiApp()


# st.markdown("""
# # Optical Character Recognition 'OCR'
#   OCR Web app with easyocr and streamlit
# """)
st.title("Optical Character Recognition")
st.write('Extract Text from Images🤖')
st.caption('OCR Web app with easyocr and streamlit')


# Add all your application here
app.add_app("English", English.app)
app.add_app("Arabic", Arabic.app)
# The main app
app.run()
