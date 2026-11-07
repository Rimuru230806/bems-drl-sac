import torch
import gymnasium
import numpy

print("PyTorch  :", torch.__version__)
print("Gymnasium:", gymnasium.__version__)
print("NumPy    :", numpy.__version__)
print("CUDA     :", torch.cuda.is_available())