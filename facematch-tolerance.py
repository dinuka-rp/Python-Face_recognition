import face_recognition

img_of_bill = face_recognition.load_image_file('./img/known/Bill_Gates.jpg')
bill_face_encoding = face_recognition.face_encodings(img_of_bill)[0]        #face_encodings return an array. Only the first item of the array is considered

#comparing images with controlled tolerance
unknown_img = face_recognition.load_image_file('./img/unknown/bill_lookalike.jpg')
unknown_encoding = face_recognition.face_encodings(unknown_img)[0]        #face_encodings return an array. Only the first item of the array is considered

results = face_recognition.compare_faces([bill_face_encoding],unknown_encoding,0.5)    #comparing one encoding each
#lower the tolerance, higher the strictness

if results[0]:
    print("This is Bill Gates")
else:
    print("This is NOT Bill Gates")