import matplotlib.pyplot as plt
import globals
import cv2
import numpy as np
from sklearn.decomposition import PCA

def DimensionReduction():
    img = globals.images[0]
    gryimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    norgryimg = np.float32(gryimg)/255
    w, h = gryimg.shape
    n = min(w, h)
    while 1:
        pca = PCA(n_components=n)
        pca_rest = pca.fit_transform(norgryimg)
        recon_img = pca.inverse_transform(pca_rest)
        recon_err = 0
        for i in range(w):
            for j in range(h):
                recon_err += (norgryimg[i][j]-recon_img[i][j])*(norgryimg[i][j]-recon_img[i][j])
        recon_err = recon_err ** 0.5
        print(n, " error:")
        print(recon_err)
        if recon_err > 3:
            print("Minimum components for reconstruction error <= 3.0:", n + 1)
            n = n + 1
            break
        n -= 1

    pca = PCA(n_components=n)
    pca_rest = pca.fit_transform(norgryimg)
    recon_img = pca.inverse_transform(pca_rest)

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(gryimg, cmap='gray')
    plt.title('Original Gray Image')

    plt.subplot(1, 2, 2)
    plt.imshow(recon_img, cmap='gray')
    plt.title(f'Reconstructed Image with {n} Components')

    plt.show()
    cv2.waitKey(0)
