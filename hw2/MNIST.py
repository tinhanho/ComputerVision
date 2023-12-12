import torchsummary
import torchvision

def ShowModelStructure():
    model = torchvision.models.vgg19(weights=None, num_classes=10)
    torchsummary.summary(model, (3, 224, 224))