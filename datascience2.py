import numpy as np
datatype = [('name', 'S20'), ('age', int)]
names = [("Sam", 14), ("Mi", 400), ("Broco", 4)]

structray = np.array(names, dtype=datatype)

print(f"Structured Array: {structray}")

print(f"\nSorted by Name: {np.sort(structray, order='name')}")

print(f"\nSorted by Age: {np.sort(structray, order='age')}")

for n in structray:
    print(f"\n{n}")