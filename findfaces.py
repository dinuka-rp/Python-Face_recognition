import face_recognition

image = face_recognition.load_image_file('./img/groups/team.jpg')
face_locations = face_recognition.face_locations(image)     #get locations of faces in image
#gives an array of co-ordinates of each face in the image

print(face_locations)