import streamlit as st
from helper import *
import streamlit.components.v1 as stc
menu_items = {
	'Get help': 'https://www.linkedin.com/in/---/',
	'Report a bug': 'https://www.linkedin.com/in/---/',
	'About': '''
	## My Custom App

	Some markdown to show in the About dialog.
	'''
}

st.set_page_config(page_title="debug", page_icon="./images/Favicon1.png", layout='centered',menu_items=menu_items)
st.set_option('deprecation.showfileUploaderEncoding', False)



def main():

    hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    # header of the app
    stc.html("""
            <div style="background-color:#76c14c;padding:10px;border-radius:30px">
            <h1 style="color:white;text-align:center;">A4A: AI 4 Agric Diagnostic Pests and Diseases Tool</h1>
            </div>""")
    
    # creating tabs for navigation
    tab1, tab2= st.tabs(["Home", "About"])
    with tab1:
        st.write("A4A is a, innovative tool to help farmers maximize their yields and make their pesticide use more effective.Farmers rely heavily on crop yields as their main source of income. However, many pests and disease can get in the way of optimal production yields.")

    with tab2:
        st.write("This is Masters project done by wendy")
        

if __name__=='__main__':
    main()
    