import streamlit as st
from keras.models import load_model
from pathlib import Path
from PIL import Image,ImageOps
import numpy as np


@st.cache(allow_output_mutation=True)
def load_model_diseaes():
    model = load_model("../model/disease_model/keras_model.h5",compile=False)
    return model

@st.cache(allow_output_mutation=True)
def load_class_diseaes():
    class_names = open('../model/disease_model/labels.txt', 'r').readlines()
    return class_names

@st.cache(allow_output_mutation=True)
def load_model_pest():
    model = load_model('../model/pest_model/keras_model.h5')
    return model

@st.cache(allow_output_mutation=True)
def load_class_pest():
    class_names = open('../model/pest_model/labels.txt', 'r').readlines()
    return class_names

def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()


# def predict_class(img, model):

	# Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = img

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
    return np.argmax(prediction) # return position of the highest probability

def predict_class(img, model,class_names):
	# Disable scientific notation for clarity
    np.set_printoptions(suppress=True)
    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    # Replace this with the path to your image
    image = img
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
    return f"{class_name} is the name of the diseaes detected in the leaf, with a confidence score of {confidence_score} % "


