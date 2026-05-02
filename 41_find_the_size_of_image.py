# 43) Image size (requires Pillow)
from plistlib import Image
img = Image.new("RGB", (640, 480))
print(img.size)  # Output: (640, 480)
