import PIL.Image
import PIL.ImageDraw
import face_recognition

# load the image into numpy array
img = face_recognition.load_image_file('img.png')
# find the faces in the image
faces = face_recognition.face_locations(img)
total_faces = len(faces)
print("total number of faces in the image: {} ".format(total_faces))
# load the image into PIL object to draw box
pil_img = PIL.Image.fromarray(img)
for face_location in faces:
    top, right, bottom, left = face_location

    draw = PIL.ImageDraw.Draw(pil_img)
    draw.rectangle([left, top, right, bottom], outline="black")

pil_img.show()

