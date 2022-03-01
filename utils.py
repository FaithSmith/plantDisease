# re-size all the images to this
import numpy as np
IMAGE_SIZE = [256, 256]
train_path = 'dataset/train'
valid_path = 'dataset/val'
model_path = 'resnet9.h5'
def return_string(predicted_class):
   # classes = [x[0].split('\\')[-1] for x in os.walk('data')][1:]
   classes = ['Pepper__bell___Bacterial_spot',
   'Pepper__bell___healthy',
   'Potato___Early_blight',
   'Potato___Late_blight',
   'Potato___healthy',
   'Tomato_Bacterial_spot',
   'Tomato_Early_blight',
   'Tomato_Late_blight',
   'Tomato_Leaf_Mold',
   'Tomato_Septoria_leaf_spot',
   'Tomato_Spider_mites_Two_spotted_spider_mite',
   'Tomato__Target_Spot',
   'Tomato__Tomato_YellowLeaf__Curl_Virus',
   'Tomato__Tomato_mosaic_virus',
   'Tomato_healthy']
   print(int(predicted_class))
   predicted = sorted(np.array(classes))[int(predicted_class)]
   return ' '.join(predicted.split('_') )+ '!'

