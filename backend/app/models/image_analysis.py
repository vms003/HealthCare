# Medical image analysis models (CNNs)import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Example function to train and save the image classification model
def train_image_analysis_model(data_dir):
    # Define image data generator for data augmentation and preprocessing
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True
    )

    # Load training images from directory
    train_generator = train_datagen.flow_from_directory(
        data_dir,
        target_size=(150, 150),  # Adjust based on your image size requirements
        batch_size=32,
        class_mode='binary'  # Adjust based on your classification task
    )

    # Define convolutional neural network model
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(128, activation='relu'),
        Dense(1, activation='sigmoid')  # Adjust based on your output classes
    ])

    # Compile the model
    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    # Train the model
    model.fit(train_generator, epochs=10)

    # Save the trained model (optional)
    # model.save('image_analysis_model.h5')

    return model

# Example function for inference with the trained model
def analyze_image(image_path, model):
    # Example image analysis code using the trained model
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(150, 150))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create a batch

    predictions = model.predict(img_array)
    score = predictions[0][0]

    if score >= 0.5:
        result = 'Positive'
    else:
        result = 'Negative'

    return result

# Example usage (for training and testing)
if __name__ == '__main__':
    trained_model = train_image_analysis_model('path_to_your_image_data_directory')  # Provide your image data directory
