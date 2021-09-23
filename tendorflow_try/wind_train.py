import tensorflow as tf
from tensorflow.keras.preprocessing import image_dataset_from_directory
import matplotlib.pyplot as plt
import os
import numpy as np
from tensorflow.keras import layers
# 设置使用GPU
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
gpu_device_name = tf.test.gpu_device_name()
print(gpu_device_name)


def train():
    data_dir = "F:\dataset\散热器"
    batch_size = 32
    image_size = 180
    learning_rate = 0.000001
    fine_tune_at = 16
    drop_rate = .2
    initial_epochs = 20

    train_dataset = tf.keras.preprocessing.image_dataset_from_directory(
                            data_dir,
                            validation_split=0.2,
                            subset="training",
                            seed=123,
                            image_size=(image_size, image_size),
                            batch_size=batch_size)

    validation_dataset = tf.keras.preprocessing.image_dataset_from_directory(
                            data_dir,
                            validation_split=0.2,
                            subset="validation",
                            seed=123,
                            image_size=(image_size, image_size),
                            batch_size=batch_size)

    # 设置数据增强模块
    data_augmentation = tf.keras.Sequential([
      layers.experimental.preprocessing.RandomFlip("horizontal_and_vertical"),
      layers.experimental.preprocessing.RandomRotation(0.2),
    ])
    # 对图像进行处理
    resize_and_rescale = tf.keras.Sequential([
        layers.experimental.preprocessing.Rescaling(1./255)
    ])

    # 下载模型
    base_model = tf.keras.applications.vgg16.VGG16(include_top=False, weights='imagenet')
    for layer in base_model.layers[:fine_tune_at]:
        layer.trainable = False
    base_model.summary()
    # 自定义输入输出层
    Input = tf.keras.Input(shape=(1, image_size, 3))
    # x = data_augmentation(Input)
    # x = resize_and_rescale(x)
    x = base_model(Input)
    x = tf.keras.layers.GlobalAveragePooling2D()(x)
    x = tf.keras.layers.Dropout(drop_rate)(x)
    Output = tf.keras.layers.Dense(1)(x)

    model = tf.keras.Model(Input, Output)

    loss = tf.keras.losses.BinaryCrossentropy(from_logits=True)
    opt = tf.keras.optimizers.Adam(learning_rate=learning_rate)
    model.compile(optimizer=opt,
                  loss=loss,
                  metrics=['accuracy'])

    history = model.fit(train_dataset,
                        epochs=initial_epochs,
                        validation_data=validation_dataset)
    loss, accuracy = model.evaluate(validation_dataset)

    image_batch, label_batch = validation_dataset.as_numpy_iterator().next()
    predictions = model.predict_on_batch(image_batch).flatten()

    # Apply a sigmoid since our model returns logits
    predictions = tf.nn.sigmoid(predictions)
    predictions = tf.where(predictions < 0.5, 0, 1)

    print('Predictions:\n', predictions.numpy())
    print('Labels:\n', label_batch)


if __name__ == '__main__':
    train()
