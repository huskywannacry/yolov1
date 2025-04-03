import torhcvision
import torch
import torch.nn as nn

class YOLO(nn.Module):
    def __init__(self:
        self, S=7, B=2, C=20, transform=None,
    ):
        self.S = S
        self.B = B
        self.C = C
        self.transform = transform
        self.annotations = pd.read_csv(csv_file)
