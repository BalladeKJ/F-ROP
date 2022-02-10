# 深度学习模型
import tensorflow as tf

def CNN_1D(input_length):
    model = tf.keras.models.Sequential([
    tf.keras.Input([input_length, 1]),
    tf.keras.layers.Conv1D(32,kernel_size=8,padding='SAME',activation=tf.nn.relu),
    tf.keras.layers.MaxPool1D(pool_size=2, strides=2),
    tf.keras.layers.Conv1D(64,kernel_size=8,padding='SAME',activation=tf.nn.relu),
    tf.keras.layers.MaxPool1D(pool_size=2, strides=2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512,activation=tf.nn.relu),
    tf.keras.layers.Dropout(0.6),
    tf.keras.layers.Dense(1,activation=tf.nn.sigmoid)
    ])
    model.compile(optimizer=tf.optimizers.Adam(1e-3),
    loss=tf.losses.binary_crossentropy,
    metrics=['accuracy', 'TruePositives', 'TrueNegatives', 'FalsePositives', 'FalseNegatives'])
    return model


def LSTM(input_length):
    model = tf.keras.models.Sequential([
    tf.keras.Input([input_length, 1]),
    tf.keras.layers.LSTM(128, activation='relu'),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(1, activation=tf.nn.sigmoid)]
    )
    model.compile(metrics=['accuracy', 'TruePositives', 'TrueNegatives', 'FalsePositives', 'FalseNegatives'],
                  loss=tf.losses.binary_crossentropy,
                  optimizer=tf.optimizers.Adam(1e-3, lr=0.00001))
    model.summary()
    return model

def use_model(model_name, args):
    """使用模型
    Args:
        model_name: 模型的名字
        args: 模型应用参数
    """
    if(model_name == "CNN_1D"):
        return CNN_1D(args)
    if(model_name == "LSTM"):
        return LSTM(args)