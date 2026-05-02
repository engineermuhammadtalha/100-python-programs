# 74) Enum example
from enum import Enum
class Color(Enum):
    RED = 1
    GREEN = 2
print(Color.RED, Color.RED.name, Color.RED.value)