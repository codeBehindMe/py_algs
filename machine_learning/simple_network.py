import tensorflow as tf

# Create a simple neural network architecture with one input layer one hidden
# layer and one output layer.
# The network should take 2 inputs and have single binary classifier output.


if __name__ == '__main__':
    input_layer = tf.placeholder()

    hidden_layer = tf.get_variable([2, 3], dtype=tf.float32)
    hidden_activation = tf.nn.relu()
