# vae_components.py

import keras
from keras import layers
from keras import backend as K


class VAELossLayer(layers.Layer):
    """
    Custom Keras layer that calculates the loss (reconstruction + KL divergence)
    of the Variational AutoEncoder (VAE)
    """

    def calculate_loss(self, original_input, reconstructed_output, mu, sigma):
        """
        Calculates VAE loss, which is the sum of the reconstruction loss and KL-divergence loss
        """
        original_input  = K.flatten(original_input)
        reconstructed_output = K.flatten(reconstructed_output)

        # Reconstruction loss - binary crossentropy is used as the final layer uses sigmoid activation
        reconstruction_loss = keras.metrics.binary_crossentropy(original_input, reconstructed_output)

        # KL divergence loss - acts as a regularizer- beta is changable
        #kl_loss = -0.5 * K.mean(1 + sigma - K.square(mu) - K.exp(sigma), axis=-1)
        #kl_loss = beta * K.mean(-0.5 * (1 + sigma - K.square(mu) - K.exp(sigma)), axis=-1)
        kl_loss = -5e-4 * K.mean(1 + sigma - K.square(mu) - K.exp(sigma), axis=-1)
        
        self.add_metric(reconstruction_loss, name='reconstruction_loss')
        self.add_metric(kl_loss, name='kl_loss')

        return K.mean(reconstruction_loss + kl_loss)

    def call(self, inputs):
        """
        Computes the loss and adds it to the layer's losses
        """
        original_input = inputs[0]
        reconstructed_output = inputs[1]
        mu = inputs[2]
        sigma = inputs[3]

        loss = self.calculate_loss(original_input, reconstructed_output, mu, sigma)
        self.add_loss(loss, inputs = inputs)

        # Returns the original layer inputs
        return original_input