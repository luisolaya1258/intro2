import streamlit as st
from PIL import Image
st.title("mi primera app") 
image= Image.open('garaje.png')
st.image(image, caption='garaje')
         
