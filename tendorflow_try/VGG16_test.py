import tensorflow as tf
from keras.applications import vgg16
import cv2
import os
from tensorflow.keras.preprocessing import image_dataset_from_directory
# 下载数据集

_URL = 'https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip'
path_to_zip = tf.keras.utils.get_file('cats_and_dogs.zip', origin=_URL, extract=True)
PATH = os.path.join(os.path.dirname(path_to_zip), 'cats_and_dogs_filtered')

train_dir = os.path.join(PATH, 'train')
validation_dir = os.path.join(PATH, 'validation')

BATCH_SIZE = 32
IMG_SIZE = (160, 160)

train_dataset = image_dataset_from_directory(train_dir,
                                             shuffle=True,
                                             batch_size=BATCH_SIZE,
                                             image_size=IMG_SIZE)

validation_dataset = image_dataset_from_directory(validation_dir,
                                                  shuffle=True,
                                                  batch_size=BATCH_SIZE,
                                                  image_size=IMG_SIZE)
class_names = train_dataset.class_names

# 加载预训练的模型
base_model = vgg16.VGG16(include_top=False, weights='imagenet')

base_model.summary()
# 冻结已经训练好的模型
base_model.trainable = False
global_average_layer = tf.keras.layers.GlobalAveragePooling2D()
predict_layel = tf.keras.layers.Dense(1)
input = tf.keras.Input(shape=(160, 160, 3))
x = base_model(input, training=False)
x = global_average_layer(x)
x = tf.keras.layers.Dropout(0.2)(x)
output = predict_layel(x)

model = tf.keras.Model(input, output)

base_learning_rate = 0.0001
model.compile(optimizer=tf.keras.optimizers.Adam(lr=base_learning_rate),
              loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
              metrics=['accuracy'])

initial_epochs = 10

loss0, accuracy0 = model.evaluate(validation_dataset)

history = model.fit(train_dataset,
                    epochs=initial_epochs,
                    validation_data=validation_dataset)

base_model.trainable = True
print("Number of layers in the base model: ", len(base_model.layers))
fine_tune_at = 100

for layer in base_model.layers[:fine_tune_at]:
  layer.trainable = False




