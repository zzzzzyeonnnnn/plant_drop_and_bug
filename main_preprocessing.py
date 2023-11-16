import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
import os

def getPrediction(filename):
    #클래스 레이블 정의
    classes = ['Bemisia tabaci', 'Sclerotinia minor', 'Bremia lactucae', 'Myzus persicae']
    num_classes = len(classes)

    for idx, cat in enumerate(classes):

        label = [0 for i in range(num_classes)]
        label[idx] = 1

    #load model
    my_model=load_model("model/model_2.h5")

    SIZE = 224 #크기 정의
    #img_path = 'static/images/' + filename #이미지 경우, 사용자가 업로드 하는 경로
    img_path = os.path.join(script_dir, 'static/images/', filename)
    img = np.asarray(Image.open(img_path).resize((SIZE, SIZE))) #넘파이 배열로 반환
    img = np.expand_dims(img, axis=0) #치수를 오른쪽으로 확장

    pred = my_model.predict(img) #모델을 사용해서 이미지 진단 예측
    pred_num = np.argmax(pred)
    pred_class = classes[pred_num] #예측 결과를 역변환해서 클래스를 가져옴
    print('Predict is: ', pred_class) #에측 진단값
    return pred_class

#test = getPrediction('993829994.jpg')
