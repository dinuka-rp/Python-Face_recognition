#This program compares an unkown face with a known face and identifies the person in the unknown image

import face_recognition

img_of_bill = face_recognition.load_image_file('./img/known/Bill_Gates.jpg')
bill_face_encoding = face_recognition.face_encodings(img_of_bill)[0]        #face_encodings return an array. Only the first item of the array is considered

unkown_img = face_recognition.load_image_file('./img/unknown/billyoung.jpg')
unkown_encoding = face_recognition.face_encodings(unkown_img)[0]        #face_encodings return an array. Only the first item of the array is considered

#comparing the 2 faces in the 2 images
results = face_recognition.compare_faces([bill_face_encoding],unkown_encoding)    #comparing one encoding each
                                        #multiple encodings of known images (array) can be used to compare one unknown image

if results[0]:
    print("This is Bill Gates")
else:
    print("This is NOT Bill Gates")