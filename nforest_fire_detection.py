import cv2
import numpy as np
import smtplib
from email.message import EmailMessage
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

def email_alert():
    msg=EmailMessage()
    msg.set_content('Fire Detected')
    msg['Subject']='Fire alert'
    msg['From']='srk532895@gmail.com'
    msg['To']='ramananv770@gmail.com'

    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('srk532895@gmail.com','lnoo sgag rejl ttmz')

    server.send_message(msg)
    server.quit()

fire=False
url='https://192.168.117.113:8080/video'

model=load_model("best_fire_detection_model.keras")

img_height,img_weight=224,224

cap=cv2.VideoCapture(url)

while True:
    ret,frame=cap.read()
    if not ret:
        break

    frame_resize=cv2.resize(frame,(img_height,img_weight))

    img_arr=img_to_array(frame_resize)/255.0

    img_arr=np.expand_dims(img_arr,axis=0)

    pred=model.predict(img_arr)[0][0]

    if pred < 0.5 and not fire:
        email_alert()
        fire=True
    elif pred >= 0.5:
        fire=False

    cv2.putText(frame,f"{'Fire' if pred < 0.5 else 'no fire'} ({pred:.3f})",(10,30),cv2.FONT_HERSHEY_SIMPLEX,1, (0,0,255) if pred < 0.5 else (0,255,0),2)

    cv2.imshow('Fire Prediction',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release
cv2.destroyAllWindows




