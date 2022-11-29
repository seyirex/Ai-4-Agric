import streamlit as st
import time
from helper import *
import streamlit.components.v1 as stc
# from keras.models import load_model

# model = load_model('keras_model.h5', compile=False)
# class_names = open('../model/disease_model/labels.txt', 'r').readlines()
menu_items = {
	'Get help': 'https://www.linkedin.com/in/---/',
	'Report a bug': 'https://www.linkedin.com/in/---/',
	'About': '''
	## My Custom App

	Some markdown to show in the About dialog.
	'''
}

st.set_page_config(page_title="A4A", page_icon="./images/Favicon1.png", layout='centered',menu_items=menu_items)
st.set_option('deprecation.showfileUploaderEncoding', False)



# rule=pred()
def main():
    #loading the model
    # model=load_model_diseaes()
    # class_names=load_class_diseaes()
    # hiding the footer text
    hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    
    # header of the app
    # st.markdown("<h3 style='text-align: center; color: black;'>A4A: Disease Diagnostic Tool</h3>",unsafe_allow_html=True)
    
    stc.html("""
            <div style="background-color:#76c14c;padding:10px;border-radius:30px">
            <h1 style="color:white;text-align:center;">A4A: Disease Diagnostic Tool</h1>
            </div>""")
    file = st.file_uploader("Upload an image of a Disease", type=["jpg", "png"])
    if file is None:
        st.markdown("<h5 style='text-align: left; color: black;'>Please upload your image for processing ⏳</h3>",unsafe_allow_html=True)
    else:
        slot = st.empty()
        with st.spinner('Your image is being processed. ⏳⏳⏳⏳'):
            time.sleep(2)

        test_image = Image.open(file).convert('RGB')
        st.image(test_image, caption="Image", width = 400)
        pred = predict_class( test_image, load_model_diseaes(),load_class_diseaes())
        st.write(pred)


if __name__=='__main__':
    main()
    