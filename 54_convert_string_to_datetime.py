# parse datetime
from datetime import datetime       
dt = datetime.strptime("2024-06-15 14:30:00", "%Y-%m-%d %H:%M:%S")
print(dt)  # Output: 2024-06-15 14:30: