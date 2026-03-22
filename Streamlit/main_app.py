import numpy as np
import streamlit as st
import cv2
from keras.models import load_model
import tensorflow as tf

model = load_model('plant_disease_model.h5')

CLASS_NAMES = ['Tomato-Bacterial_spot', 'Potato-Early_blight', 'Corn-Common_rust']

st.title("Automated Plant disease detetction for Corn Maize, Tomato & Potato")
st.markdown("Upload / Submit an image of the plant leaf")

plant_image = st.file_uploader("Choose the image to be uploaded for detecting the plant disease", type="jpg")
submit = st.button('Predict the disease that the plant has been affected with')

if submit:
 
   if plant_image is not None:

      #Convert the file into an opencv image
      file_bytes = np.asarray(bytearray(plant_image.read()), dtype=np.uint8)
      opencv_image = cv2.imdecode(file_bytes, 1)

      #Displaying the image
      st.image(opencv_image, channels="BGR")
      st.write(opencv_image.shape)

      #Resizing the image
      opencv_image = cv2.resize(opencv_image, (256,256))

      #Convert image to 4D
      opencv_image.shape = (1,256,256,3)

      #Make Prediction
      y_pred = model.predict(opencv_image)
      result = CLASS_NAMES[np.argmax(y_pred)]
      st.title(str("This is "+result.split('-')[0]+ " leaf affected with " + result.split('-')[1]))
      