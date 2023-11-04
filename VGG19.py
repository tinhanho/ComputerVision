import cv2
from torchvision import transforms
import matplotlib.pyplot as plt
import globals
from PIL import Image
def ShowAugmentedImages():
    trans = transforms.Compose(
        [
            transforms.RandomHorizontalFlip(),
            transforms.RandomHorizontalFlip(),
            transforms.RandomRotation(30),
            transforms.ToTensor(),
        ]
    )

    i = 1
    plt.figure(figsize=(10, 10))
    for img in globals.images:
        name = img.filename
        name = name.split('/')[-1]
        name = name.replace(".png", "")
        img = trans(img)
        img = img.permute(1, 2, 0).numpy()
        plt.subplot(3, 3, i)
        plt.xlabel("", fontsize=6)
        plt.ylabel("", fontsize=6)
        plt.title(name, fontsize=10)
        plt.imshow(img)
        i += 1
    plt.show()
