import torch

print("PyTorch version:", torch.__version__)

# Check if CUDA is available
if torch.cuda.is_available():
    print("CUDA is available!")
    print("Device count:", torch.cuda.device_count())
    for i in range(torch.cuda.device_count()):
        print("Device", i, ":", torch.cuda.get_device_name(i))
        print("\tCUDA Compute Capability:", torch.cuda.get_device_capability(i))
        print("\tTotal Memory:", torch.cuda.get_device_properties(i).total_memory / (1024**3), "GB")
        print("\tCUDA Version:", torch.version.cuda)
        if torch.backends.cudnn.is_available():
            print("\tCuDNN Version:", torch.backends.cudnn.version())
        else:
            print("\tCuDNN is not available on this device.")
else:
    print("CUDA is not available!")


