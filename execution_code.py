import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import tensorflow_addons as tfa

custom_objects = {'F1Score': tfa.metrics.F1Score}

# Load the trained VGG19 model with the custom_objects dictionary
best_model = load_model('ensemble_model.h5', custom_objects=custom_objects)

# Load and preprocess the input image (replace 'path/to/your/image.jpg' with the image path)
image_path = input("Provide the Image Path  : ")
img = image.load_img(image_path, target_size=(256, 256))
img = image.img_to_array(img)
img = np.expand_dims(img, axis=0)
img = img / 255.0  # Normalize pixel values, matching what you did during training

# Make predictions
predictions = best_model.predict(img)

# Decode the predictions and get the class label
predicted_class = np.argmax(predictions, axis=1)

# Map the class label to a human-readable category
# Define a dictionary to map class indices to class labels
label_dict = {
    0: 'bacterial_leaf_blight',
    1: 'bacterial_leaf_streak',
    2: 'bacterial_panicle_blight',
    3: 'blast',
    4: 'brown_spot',
    5: 'dead_heart',
    6: 'downey_mildew',
    7: 'hispa',
    8: 'normal',
    9: 'tungro',
    # Add more class labels as needed
}

predicted_category = label_dict[predicted_class[0]]

print(f'The predicted category is: {predicted_category}')
print("\nCauses for the Category is : ")
flag=1
for i in disease_cause[predicted_category]:
    print(flag,i)
    flag=flag+1