# image_path = os.path.abspath('ticket.jpeg')

import win32print
import win32ui
import win32con
from PIL import Image
import os
# Specify the path to the JPEG image you want to print
image_path = os.path.abspath('ticket.jpeg')

# Open the image using Pillow
image = Image.open(image_path)

# Get the default printer name
printer_name = win32print.GetDefaultPrinter()

# Create a device context (DC) for the printer
printer_dc = win32ui.CreateDC()

# Set the printer to the default printer
printer_dc.CreatePrinterDC(printer_name)

# Get the image dimensions (in pixels)
width, height = image.size

# Start printing
printer_dc.StartDoc('Image Printing')
printer_dc.StartPage()

# Set the orientation based on image dimensions
if width > height:
    # Landscape orientation
    printer_dc.SetMapMode(win32con.MM_ISOTROPIC)
    printer_dc.SetWindowExt((width, height))
    printer_dc.SetViewportExt((width, height))
else:
    # Portrait orientation
    printer_dc.SetMapMode(win32con.MM_ISOTROPIC)
    printer_dc.SetWindowExt((height, width))
    printer_dc.SetViewportExt((height, width))

# StretchBlt the image onto the printer's DC
printer_dc.StretchBlt(
    (0, 0, width, height),
    image,
    (0, 0, width, height),
    win32con.SRCCOPY
)

# End printing
printer_dc.EndPage()
printer_dc.EndDoc()

# Clean up resources
printer_dc.DeleteDC()
