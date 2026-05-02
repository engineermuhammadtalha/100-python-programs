# create nested directory safely
import os
os.makedirs('parent/child/grandchild', exist_ok=True)
print("created")