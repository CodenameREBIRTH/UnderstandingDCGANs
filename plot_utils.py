import numpy as np
import matplotlib.pyplot as plt

def show_image(image, num_cols=None):
    num_cols = num_cols or len(image)
    num_rows = (len(image) - 1) // num_cols + 1
    if image.shape[-1] == 1:
        image = np.squeeze(image, axis=-1)
    plt.figure(figsize=(num_cols, num_rows))
    for i, img in enumerate(image):
        plt.subplot(num_rows, num_cols, i+1)
        plt.imshow(img, cmap='binary')
        plt.axis('off')
