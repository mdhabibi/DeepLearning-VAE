import pandas as pd
import matplotlib.pyplot as plt

results = []
latent_dims = [5, 5, 5, 5]

for dim in latent_dims:
    df = pd.read_csv(f'/Volumes/D/GitHub-Portfolio/DeepLearning-MNIST-VAE/data/metrics_by_digit_latent_dim_{dim}.csv')
    df['latent_dim'] = dim
    results.append(df)

results_df = pd.concat(results)

# Example Plot for MSE
plt.figure(figsize=(10, 6))
plt.plot(results_df['latent_dim'], results_df['mse_vae'], label='MSE - VAE')
plt.plot(results_df['latent_dim'], results_df['mse_decoder'], label='MSE - Decoder')
plt.xlabel('Latent Dimension')
plt.ylabel('MSE')
plt.title('MSE Comparison Across Different Latent Dimensions')
plt.legend()
plt.show()

# Example Plot for PSNR
plt.figure(figsize=(10, 6))
plt.plot(results_df['latent_dim'], results_df['psnr_vae'], label='PSNR - VAE')
plt.plot(results_df['latent_dim'], results_df['psnr_decoder'], label='PNSR - Decoder')
plt.xlabel('Latent Dimension')
plt.ylabel('PNSR')
plt.title('PNSR Comparison Across Different Latent Dimensions')
plt.legend()
plt.show()
