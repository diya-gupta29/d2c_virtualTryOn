from flask import Flask, render_template, request
import json
from flask_cors import CORS
import numpy as np
import cv2                      
from math import floor

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/shirt.html')
def plot():
    return render_template('shirt.html')

@app.route('/Try', methods=['GET','POST'])
def Try():
    shirtno = int(request.form["shirt"])

    cv2.cv2.waitKey(1)
    cap=cv2.cv2.VideoCapture(0)
    ih=shirtno
    while True:
        imgarr=["shirt_1.png",'shirt_2.png','shirt_3.jpg']

        imgshirt = cv2.cv2.imread(imgarr[ih-1],1) 
        if ih==3:
            shirtgray = cv2.cv2.cvtColor(imgshirt,cv2.cv2.COLOR_BGR2GRAY) 
            ret, orig_masks_inv = cv2.cv2.threshold(shirtgray,200 , 255, cv2.cv2.THRESH_BINARY) 
            orig_masks = cv2.cv2.bitwise_not(orig_masks_inv)

        else:
            shirtgray = cv2.cv2.cvtColor(imgshirt,cv2.cv2.COLOR_BGR2GRAY) 
            ret, orig_masks = cv2.cv2.threshold(shirtgray,0 , 255, cv2.cv2.THRESH_BINARY) 
            orig_masks_inv = cv2.cv2.bitwise_not(orig_masks)
        origshirtHeight, origshirtWidth = imgshirt.shape[:2]
        face_cascade=cv2.cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        ret,img=cap.read()
       
        height = img.shape[0]
        width = img.shape[1]
        resizewidth = int(width*3/2)
        resizeheight = int(height*3/2)
        cv2.cv2.namedWindow("img",cv2.cv2.WINDOW_NORMAL)
        cv2.cv2.resizeWindow("img", (int(width*3/2), int(height*3/2)))
        gray=cv2.cv2.cvtColor(img,cv2.cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(gray,1.3,5)

        for (x,y,w,h) in faces:
            cv2.cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.cv2.rectangle(img,(100,200),(312,559),(255,255,255),2)

            shirtWidth =  3 * w  
            shirtHeight = shirtWidth * origshirtHeight / origshirtWidth 
            x1s = x-w
            x2s =x1s+3*w
            y1s = y+h
            y2s = y1s+h*4
            if x1s < 0:
                x1s = 0
            if x2s > img.shape[1]:
                x2s =img.shape[1]
            if y2s > img.shape[0] :
                y2s =img.shape[0]
            temp=0
            if y1s>y2s:
                temp=y1s
                y1s=y2s
                y2s=temp
            shirtWidth = int(abs(x2s - x1s))
            shirtHeight = int(abs(y2s - y1s))
            y1s = int(y1s)
            y2s = int(y2s)
            x1s = int(x1s)
            x2s = int(x2s)
            shirt = cv2.cv2.resize(imgshirt, (shirtWidth,shirtHeight), interpolation = cv2.cv2.INTER_AREA)
            mask = cv2.cv2.resize(orig_masks, (shirtWidth,shirtHeight), interpolation = cv2.cv2.INTER_AREA)
            masks_inv = cv2.cv2.resize(orig_masks_inv, (shirtWidth,shirtHeight), interpolation = cv2.cv2.INTER_AREA)
            rois = img[y1s:y2s, x1s:x2s]
            num=rois
            roi_bgs = cv2.cv2.bitwise_and(rois,num,mask = masks_inv)
            roi_fgs = cv2.cv2.bitwise_and(shirt,shirt,mask = mask)
            dsts = cv2.cv2.add(roi_bgs,roi_fgs)
            img[y1s:y2s, x1s:x2s] = dsts 
            
            break
        cv2.cv2.imshow("img",img)
        if cv2.cv2.waitKey(100) == ord('q'):
            break

    cap.release()                           
    cv2.cv2.destroyAllWindows()      

    return render_template('index.html')
if __name__ == '__main__':
    app.run(host='127.0.0.1',debug=True,port=5000)