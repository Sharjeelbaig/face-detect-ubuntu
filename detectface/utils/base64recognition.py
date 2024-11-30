import base64
import face_recognition
import numpy as np
from io import BytesIO
from PIL import Image

def base64recognition(base64_image1, base64_image2):
        # Decode the Base64 strings into image data
        image1_data = base64.b64decode(base64_image1)
        image2_data = base64.b64decode(base64_image2)
        # Open the binary data as images using PIL
        image1 = Image.open(BytesIO(image1_data))
        image2 = Image.open(BytesIO(image2_data))
        # Convert images to RGB if not already in that mode
        if image1.mode != "RGB":
            image1 = image1.convert("RGB")
        if image2.mode != "RGB":
            image2 = image2.convert("RGB")
        # Convert PIL images to numpy arrays
        image1 = np.array(image1)
        image2 = np.array(image2)
        # Process the images with face_recognition
        face_locations1 = face_recognition.face_locations(image1)
        face_encodings1 = face_recognition.face_encodings(image1, face_locations1)
        face_locations2 = face_recognition.face_locations(image2)
        face_encodings2 = face_recognition.face_encodings(image2, face_locations2)
        # Compare faces if encodings are found
        if face_encodings1 and face_encodings2:
            match = face_recognition.compare_faces([face_encodings1[0]], face_encodings2[0])
            if match[0]:
                print("The person in both photos is the same.")
                return "The person in both photos is the same."
            else:
                print("The person in both photos is different.")
                return "The person in both photos is different."
        else:
            print("No faces found in one or both images.")
            return "No faces found in one or both images."