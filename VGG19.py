import torchsummary
from torchvision import transforms
import matplotlib.pyplot as plt
import globals
import torchvision
import torch

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
    model = torchvision.models.vgg19(pretrained=False, num_classes=10)
    torchsummary.summary(model, (3, 224, 224))

def ShowAccAndLoss():
    model = torchvision.models.vgg19(pretrained=False, num_classes=10)
    device = torch.device("cpu")
    model = model.to(device)
    trans = transforms.Compose(
        [
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
        ]
    )
    trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=trans)
    trainloader = torch.utils.data.DataLoader(trainset, batch_size=8, shuffle=True)
    criterion = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

    for epoch in range(40):
        print(epoch)
        model.train()
        running_loss = 0.0
        for inputs, labels in trainloader:
            inputs, labels = inputs.to(device), labels.to(device)
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()
        print(f'Epoch {epoch + 1}, Loss: {running_loss / len(trainloader)}')
    torch.save(model.state_dict(), 'cifar10_vgg19_model.pth')
    print('Finished Training')


