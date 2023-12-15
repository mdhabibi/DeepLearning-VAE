import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

results = []
latent_dims = [5, 10, 15, 20]

# A color palette with 10 colors for the digits 0-9
palette = sns.color_palette("tab10", n_colors=10)

for dim in latent_dims:
    df = pd.read_csv(f'/Volumes/D/GitHub-Portfolio/DeepLearning-MNIST-VAE/data/metrics_by_digit_latent_dim_{dim}.csv')
    df['latent_dim'] = dim
    results.append(df)

results_df = pd.concat(results)

# Plot for MSE for each digit
plt.figure(figsize=(14, 8))
for digit in range(10):
    subset = results_df[results_df['digit'] == digit]
    #plt.scatter(subset['latent_dim'], subset['mse_vae'], label=f'Digit {digit} - VAE', color=palette[digit])
    plt.scatter(subset['latent_dim'], subset['mse_decoder'], label=f'Digit {digit}', color=palette[digit], marker='o')

plt.xlabel('Latent Dimension')
plt.ylabel('MSE')
plt.title('MSE Comparison Across Different Latent Dimensions for Each Digit')
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0.)  
plt.show()

# Plot for PSNR for each digit
plt.figure(figsize=(14, 8))
for digit in range(10):
    subset = results_df[results_df['digit'] == digit]
    #plt.scatter(subset['latent_dim'], subset['psnr_vae'], label=f'Digit {digit} - VAE', color=palette[digit])
    plt.scatter(subset['latent_dim'], subset['psnr_decoder'], label=f'Digit {digit}', color=palette[digit], marker='o')

plt.xlabel('Latent Dimension')
plt.ylabel('PSNR')
plt.title('PSNR Comparison Across Different Latent Dimensions for Each Digit')
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0.)  
plt.show()

