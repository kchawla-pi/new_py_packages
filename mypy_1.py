from typing import *

# Shape = NewType('Shape', Text)

def area(length: float, shape: Text) -> Optional[float]:
	if shape == 'square':
		return length ** 2
	elif shape == 'circle':
		return (22 / 7) * (length ** 2)


ar_sq = area(5, 0)
ar_ci = area(5, 'suare')
ar_te = area(5, 'circle')

print(ar_sq)
print(ar_ci)
print(ar_te)
