import ctypes
from ctypes import byref, c_int, c_void_p, create_string_buffer
from PIL import Image
import numpy as np

# Load the DLL
sgfplib = ctypes.WinDLL(r"C:\Users\pavan\Downloads\FDx_SDK_Pro_Windows_v4.3.1_J1.12\FDx SDK Pro for Windows v4.3.1_J1.12\FDx SDK Pro for Windows v4.3.1\bin\x64\sgfplib.dll")

# Constants
MAX_IMAGE_WIDTH = 300
MAX_IMAGE_HEIGHT = 400
IMAGE_SIZE = MAX_IMAGE_WIDTH * MAX_IMAGE_HEIGHT

# Initialize the library
hDevice = c_void_p()
result = sgfplib.CreateSGFPMObject(byref(hDevice))
print("CreateSGFPMObject:", result)

# Init the device
result = sgfplib.Init(500)  # 500 is image DPI
print("Init:", result)

# Open device
result = sgfplib.OpenDevice(0)
print("OpenDevice:", result)

# Allocate buffer for image
imageBuffer = create_string_buffer(IMAGE_SIZE)

# Capture single image
result = sgfplib.GetImage(imageBuffer)
print("GetImage:", result)

# Convert to numpy array and save using Pillow
img_array = np.frombuffer(imageBuffer, dtype=np.uint8).reshape((MAX_IMAGE_HEIGHT, MAX_IMAGE_WIDTH))
image = Image.fromarray(img_array)
image.save("fingerprint.png")
print("Fingerprint image saved as fingerprint.png")

# Close device
sgfplib.CloseDevice()
