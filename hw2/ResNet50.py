import torchsummary
import torchvision
from torchvision import transforms
from torch.utils.data import DataLoader
from torchvision.datasets import ImageFolder

import torch
import matplotlib.pyplot as plt
def tensor_translate(image1, image2, titles=None):
    image1_np = image1.numpy()
    image2_np = image2.numpy()

    image1_np = image1_np.transpose((1, 2, 0))
    image2_np = image2_np.transpose((1, 2, 0))

    image1_np = (image1_np * 255).astype('uint8')
    image2_np = (image2_np * 255).astype('uint8')

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].imshow(image1_np)
    axes[0].set_title(titles[0] if titles else 'Image 1')
    axes[0].axis('off')

    axes[1].imshow(image2_np)
    axes[1].set_title(titles[1] if titles else 'Image 2')
    axes[1].axis('off')
    plt.show()
def ShowImages():
    folder_path = 'C:/Users/hotin/Desktop/dataset/inference_dataset'
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
    ])
    dataset = ImageFolder(root=folder_path, transform=transform)
    dataloader = torch.utils.data.DataLoader(dataset, batch_size=32, shuffle=True)
    print("inference pic read finish")
    if dataloader is not None:
        for inputs, labels in dataloader:
            cat_indices = (labels == 0).nonzero()[:, 0]
            dog_indices = (labels == 1).nonzero()[:, 0]

            # 選擇一張 cat 圖片和一張 dog 圖片
            cat_image = inputs[cat_indices[0]]
            dog_image = inputs[dog_indices[0]]
            break
        tensor_translate(cat_image, dog_image, titles=['Cat', 'Dog'])
    else:
        print("DataLoader is not initialized. Please load data first.")

def ShowModelStructureRN50():
    model = torchvision.models.resnet50(weights=None, num_classes=10)
    torchsummary.summary(model, (3, 224, 224))


