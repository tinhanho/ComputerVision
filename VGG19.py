from torchvision import transforms
import matplotlib.pyplot as plt
import globals
import torchvision
import  torch

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

def ShowModelStructure():
    1
    # trans = transforms.Compose(
    #     [
    #         transforms.Resize((224, 224)),
    #         transforms.ToTensor(),
    #         transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))
    #     ]
    # )
    # trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
    # trainloader = torch.utils.data.DataLoader(trainset, batch_size=32, shuffle=True)
    #
    # model = torchvision.models.vgg19_bn(num_classes=10)
