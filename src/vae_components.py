# vae_components.py

import keras
from keras import layers
from keras import backend as K


class VAELossLayer(layers.Layer):
    """
    Custom Keras layer that calculates the loss (reconstruction + KL divergence)
    of the Variational AutoEncoder (VAE)
    """

    def __init__(self, beta=0.0005, **kwargs):
        super().__init__(**kwargs)
        self.beta = beta
        
    def calculate_loss(self, original_input, reconstructed_output, mu, sigma):
        """
        Calculates VAE loss, which is the sum of the reconstruction loss and KL-divergence loss
        """
        original_input = K.flatten(original_input)
        reconstructed_output = K.flatten(reconstructed_output)
        reconstruction_loss = keras.metrics.binary_crossentropy(original_input, reconstructed_output)
        kl_loss = -self.beta * K.mean(1 + sigma - K.square(mu) - K.exp(sigma), axis=-1)
        
        self.add_metric(reconstruction_loss, name='reconstruction_loss')
        self.add_metric(kl_loss, name='kl_loss')

        return K.mean(reconstruction_loss + kl_loss)

    def call(self, inputs):
        """
        Computes the loss and adds it to the layer's losses
        """
        original_input, reconstructed_output, mu, sigma = inputs
        loss = self.calculate_loss(original_input, reconstructed_output, mu, sigma)
        self.add_loss(loss, inputs=inputs)
        return original_input