import os
os.system('sudo apt-get install python3-opencv -y')
import cv2

import warnings
import numpy as np
from PIL import Image
import streamlit as st
from user_func import extract_face, get_similarity

warnings.filterwarnings('ignore')


def main():
    
    st.header('Face Verification')

    column1, column2 = st.columns(2)
    with column1:
        image1 = st.file_uploader("Insert Image-1", type=["jpg","png",'jpeg'])
    with column2:
        image2 = st.file_uploader("Insert Image-2", type=["jpg","png",'jpeg'])

    if (image1 is not None) & (image2  is not None):
        col1, col2 = st.columns(2)
        image1 = Image.open(image1).convert('RGB')
        image2 = Image.open(image2).convert('RGB')
        with col1:
            st.image(image1, width=300)
        with col2:
            st.image(image2, width=300)
        filenames = [image1, image2]

        faces = [extract_face(image) for image in filenames]
        score, distance = get_similarity(faces)

        if (1 - score) > 0.60 and distance <= 100:
            st.success('Face Matched!!')
            st.write('Cosine Similarity--->', round((1 - score)*100, 2))
            st.write('Euclidean Distance-->', round(distance, 2))
        else:
            st.error('Face Not Matched!!')
            st.write('Cosine Similarity--->', round((1 - score)*100, 2))
            st.write('Euclidean Distance-->', round(distance, 2))
    else:
        pass

if __name__ == '__main__':
    main()