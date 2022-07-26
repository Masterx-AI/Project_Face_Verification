import warnings
import numpy as np
from PIL import Image
from mtcnn.mtcnn import MTCNN
from keras_vggface.vggface import VGGFace
from keras_vggface.utils import preprocess_input
from scipy.spatial.distance import cosine, euclidean

warnings.filterwarnings('ignore')


def extract_face(image, resize=(224, 224)):
    pixcels = np.asarray(image)
    detector = MTCNN()
    faces = detector.detect_faces(pixcels)
    x1, y1, width, height = faces[0]['box']
    x2, y2 = x1+width, y1+height
    face_boundary = pixcels[y1:y2, x1:x2]
    image = Image.fromarray(face_boundary)
    image = image.resize((224, 224))
    face_array = np.asarray(image)
    return face_array

def get_embeddings(faces):
    face = np.asarray(faces, 'float32')
    face = preprocess_input(face, version=2)
    model = VGGFace(model='resnet50', include_top=False, input_shape=(224, 224, 3), pooling='avg')
    return model.predict(face)

def get_similarity(faces):
    embeddings = get_embeddings(faces)
    score = cosine(embeddings[0], embeddings[1])
    distance = euclidean(embeddings[0], embeddings[1])
    return(score, distance)
