#Author: Rudra Shah
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np

# Load the model path here
model = load_model("flowers.h5")
flowers = ['Daisy', 'Dandelion', 'Rose' ,'Sunflower', 'Tulip']

#Enter path for the sample image
path = "sampleflowers/test6.jpg"

test_image = image.load_img(path, target_size = (150,150)) #Keep the size constant as per the training session
test_image = image.img_to_array(test_image)
test_image=test_image/255
test_image = np.expand_dims(test_image, axis = 0)
result = model.predict(test_image)
result = result.flatten().tolist()
lindx = np.argmax(result)
print(flowers[lindx])