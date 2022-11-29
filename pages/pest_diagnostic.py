import streamlit as st
import time
from helper import (
    # predict_class,
    load_class_pest,
    load_model_pest,
    read_markdown_file
)
import streamlit.components.v1 as stc
from PIL import Image,ImageOps
import numpy as np
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


def main():
    #loading the model
    model=load_model_pest()
    class_names=load_class_pest()
    # hiding the footer text
    hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    
    # header of the app
    stc.html("""
            <div style="background-color:#76c14c;padding:10px;border-radius:30px">
            <h1 style="color:white;text-align:center;">A4A: Pest Diagnostic Tool</h1>
            </div>""")
    
    
    file = st.file_uploader("Upload an image of a pest 😃", type=["jpg", "png"])
    if file is None:
        st.markdown("<h5 style='text-align: left; color: black;'>Please upload an image for processing ⏳</h3>",unsafe_allow_html=True)
    else:
        slot = st.empty()
        with st.spinner('Your image is being processed. ⏳⏳⏳⏳'):
            time.sleep(2)

        test_image = Image.open(file).convert('RGB')
        st.image(test_image, caption="Pest Image", width = 400)
        # Disable scientific notation for clarity
        np.set_printoptions(suppress=True)
        # Create the array of the right shape to feed into the keras model
        # The 'length' or number of images you can put into the array is
        # determined by the first position in the shape tuple, in this case 1.
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        # Replace this with the path to your image
        image = test_image
        #resize the image to a 224x224 with the same strategy as in TM2:
        #resizing the image to be at least 224x224 and then cropping from the center
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)
        #turn the image into a numpy array
        image_array = np.asarray(image)
        # Normalize the image
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        # Load the image into the array
        data[0] = normalized_image_array  
        # run the inference
        prediction = model.predict(data)
        index = np.argmax(prediction)
        class_name = class_names[index]
        confidence_score = prediction[0][index]
        st.write(f"{class_name} is the name of the diseaes detected in the leaf, with a confidence score of {round(confidence_score,3)}")
        # pred = predict_class(test_image, load_model_pest(),load_class_pest())
        # st.write(index)
        
        if index == 0:
            markdown = read_markdown_file("./treatment/aphids.md")
            st.markdown(markdown, unsafe_allow_html=True)
            image = Image.open('./images/aphids/banzo.jpg')
            st.image(image, caption='Banzo',width = 400)
        
        elif index  == 1:
            markdown = read_markdown_file("./treatment/armyworm.md")
            st.markdown(markdown, unsafe_allow_html=True)
            image = Image.open('./images/armyworm/perfek-315-ec.jpg')
            st.image(image, caption='Perfek-315-ec',width = 400)
        
        
        elif index  == 2:
            markdown = read_markdown_file("./treatment/beetle.md")
            st.markdown(markdown, unsafe_allow_html=True)
            image = Image.open('./images/beetle/smash.jpg')
            st.image(image, caption='Smash',width = 400)
        
        
        elif index  == 3:
            markdown = read_markdown_file("./treatment/bollworm.md")
            st.markdown(markdown, unsafe_allow_html=True)
            image = Image.open('./images/bollworm/auzar-25-ec.jpg')
            st.image(image, caption='Auzar-25-ec',width = 400)
        
        
        elif index  == 4:
            markdown = read_markdown_file("./treatment/grasshopper.md")
            st.markdown(markdown, unsafe_allow_html=True)
            image = Image.open('./images/grasshopper/biostadt-malathion-57-ec.jpg')
            st.image(image, caption='Biostadt-malathion-57-ec',width = 400)
        
        
        elif index  == 5:
            markdown = read_markdown_file("./treatment/mites.md")
            st.markdown(markdown, unsafe_allow_html=True)
            image = Image.open('./images/mites/bioclaim.jpg')
            st.image(image, caption='Bioclaim',width = 400)
        
        
        elif index  == 6:
            markdown = read_markdown_file("./treatment/sawfly.md")
            st.markdown(markdown, unsafe_allow_html=True)
            image = Image.open('./images/sawfly/krush.jpg')
            st.image(image, caption='krush',width = 400)
        
        
        elif index  == 7:
            markdown = read_markdown_file("./treatment/stem_borer.md")
            st.markdown(markdown, unsafe_allow_html=True)
            image = Image.open('./images/stem_borer/cartop.jpg')
            st.image(image, caption='Cartop',width = 400)
        
        
        elif index  == 8:
            markdown = read_markdown_file("./treatment/thrips.md")
            st.markdown(markdown, unsafe_allow_html=True)
            image = Image.open('./images/thrips/Eagle-Thripan-Bio-Miticide.jpg')
            st.image(image, caption='Eagle-Thripan-Bio-Miticide',width = 400)
        
        
        elif index == 9:
            markdown = read_markdown_file("./treatment/whitefly.md")
            st.markdown(markdown, unsafe_allow_html=True)
            image = Image.open('./images/whitefly/reno.jpg')
            st.image(image, caption='Reno',width = 400)
        
        
        else:
            st.markdown("<h3 style='text-align: center; color: black;'>Sorry Debug does not currently have this pest in database'</h3>",unsafe_allow_html=True)



if __name__=='__main__':
    main()
    