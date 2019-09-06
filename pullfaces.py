from PIL import Image       #implementing the Pillow library (Imaging library)
import face_recognition

image = face_recognition.load_image_file('./img/groups/team.jpg')
face_locations = face_recognition.face_locations(image)     #get locations of faces in image

for face_location in face_locations:
    top, right, bottom, left = face_location        #assigning co-ordinates of one face location to seperate variables

    face_image = image[top:bottom,left:right]       #gives a face image in a form of an array

    pil_image = Image.fromarray(face_image)
    pil_image.show()
