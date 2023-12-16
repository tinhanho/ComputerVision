import torchsummary
import torchvision
import cv2
import torchvision.models as models
import torch
from torchsummary import summary
import torch.nn as nn
from torchvision import transforms,datasets
from torchvision.datasets import ImageFolder
import globals
import matplotlib.pyplot as plt
import numpy as np

class VGG19(nn.Module):
    def __init__(self):
        super(VGG19, self).__init__()
        self.features = nn.Sequential(
            nn.Conv2d(1, 64, kernel_size=3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
            nn.Conv2d(64, 64, kernel_size=3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),

            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(inplace=True),
            nn.Conv2d(128, 128, kernel_size=3, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),

            nn.Conv2d(128, 256, kernel_size=3, padding=1),
            nn.BatchNorm2d(256),
            nn.ReLU(inplace=True),
            nn.Conv2d(256, 256, kernel_size=3, padding=1),
            nn.BatchNorm2d(256),
            nn.ReLU(inplace=True),
            nn.Conv2d(256, 256, kernel_size=3, padding=1),
            nn.BatchNorm2d(256),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),

            nn.Conv2d(256, 512, kernel_size=3, padding=1),
            nn.BatchNorm2d(512),
            nn.ReLU(inplace=True),
            nn.Conv2d(512, 512, kernel_size=3, padding=1),
            nn.BatchNorm2d(512),
            nn.ReLU(inplace=True),
            nn.Conv2d(512, 512, kernel_size=3, padding=1),
            nn.BatchNorm2d(512),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),

            nn.Conv2d(512, 512, kernel_size=3, padding=1),
            nn.BatchNorm2d(512),
            nn.ReLU(inplace=True),
            nn.Conv2d(512, 512, kernel_size=3, padding=1),
            nn.BatchNorm2d(512),
            nn.ReLU(inplace=True),
            nn.Conv2d(512, 512, kernel_size=3, padding=1),
            nn.BatchNorm2d(512),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )
        self.avgpool = nn.AdaptiveAvgPool2d((7, 7))
        self.classifier = nn.Sequential(
            nn.Linear(512 * 7 * 7, 4096),
            nn.ReLU(inplace=True),
            nn.Dropout(),
            nn.Linear(4096, 4096),
            nn.ReLU(inplace=True),
            nn.Dropout(),
            nn.Linear(4096, 10)  # 10 classes for MNIST
        )

    def forward(self, x):
        x = self.features(x)
        x = self.avgpool(x)
        x = torch.flatten(x, 1)
        x = self.classifier(x)
        return x
def ShowModelStructure():
    model = torchvision.models.vgg19(weights=None, num_classes=10)
    torchsummary.summary(model, (3, 224, 224))
def ShowAccuracyAndLoss():
    res = cv2.imread("result.png")
    cv2.imshow('111', res)

def Predict():
    model = VGG19()
    model.load_state_dict(torch.load("./model/vgg19_mnist_model.pth", map_location=torch.device('cpu')))
    model.eval()
    model.to('cpu')
    with torch.no_grad():
        globals.preimage = globals.preimage.unsqueeze(0).to('cpu')
        output = model(globals.preimage)

    # Apply softmax to get probabilities
    probabilities = nn.functional.softmax(output[0], dim=0).cpu().numpy()
    digits = list(range(10))
    plt.bar(digits, probabilities, color='blue')
    plt.xlabel('Digit')
    plt.ylabel('Probability')
    plt.title('Digit Recognition Probabilities')
    plt.xticks(digits)
    plt.ylim(0, 1)
    globals.pdigit = str(np.argmax(probabilities))
    plt.show()
