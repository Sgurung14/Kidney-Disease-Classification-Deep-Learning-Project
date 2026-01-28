import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        # load model
        model = load_model(os.path.join("model", "model.h5"))

        # image preprocessing
        img = image.load_img(self.filename, target_size=(224, 224))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        img = img/255.0 #normalize values

        # prediction
        result = np.argmax(model.predict(img), axis=1)
        print(result)

        # return result
        if result[0] == 0:
            prediction = 'Cyst'
        elif result[0] == 1:
            prediction = 'Normal'
        elif result[0] == 2:
            prediction = 'Stone'
        else:
            prediction = 'Tumor'
        
        return [{"image": prediction}]