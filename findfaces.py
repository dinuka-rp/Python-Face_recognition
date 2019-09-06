#This program identifies the cordinates of faces in an image with multiple people

import face_recognition

image = face_recognition.load_image_file('./img/groups/team.jpg')
face_locations = face_recognition.face_locations(image)     #get locations of faces in image

print(face_locations)       #gives an array of co-ordinates of each face in the image
print(f'There are {len(face_locations)} people in this image')         #identifying the number of people in an image