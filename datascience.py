import numpy as np

array = np.array([5, 1, 6, 3, 4, 7, 3, 8, 9])
array2 = np.array([9, 10, 51, 15, 13, 19, 15, 39, 59])

print(f"Array: {array}")
print(f"\nArray2: {array2}")

print(f"\nArray accessed by last element: {array[-1]}")
print(f"\nArray2 accessed by third element: {array2[2]}")

print(f"\nArray datatype: {array.dtype}")
print(f"\nArray2 datatype: {array2.dtype}")

print(f"\nFinding Array Elements bigger than 3: {np.where(array > 3)}")
print(f"\nFinding Array2 Elements bigger than 10: {np.where(array2 > 10)}")

print(f"\nArray Unique Elements: {np.unique(array)}")
print(f"\nArray2 Unique Elements: {np.unique(array2)}")

print(f"\nShape of Array: {np.shape(array)}")
print(f"\nShape of Array2: {np.shape(array2)}")

sorta = array
sorta2 = array2

sorta.sort()
sorta2.sort()

print(f"\nArray sorted: {sorta}")
print(f"\nArray2 sorted: {sorta2}")

print(f"\nArray reversed and sorted: {sorta[::-1]}")
print(f"\nArray2 reversed and sorted: {sorta2[::-1]}")

print(f"\nConcatenation Between Array and Array2: {(np.concatenate((array, array2)))}")

for e in array:
    print(f"\n{e}")

for e2 in array:
    print(f"\n{e2}")

addbmath = np.add(array, array2)
print(f"\nArray and Array2 added: {addbmath}")

submath = np.subtract(array, array2)
print(f"\nArray and Array2 subtracted: {submath}")

multmath = np.multiply(array, array2)
print(f"\nArray and Array2 multiplied: {multmath}")

divmath = np.divide(array, array2)
print(f"\nArray and Array2 divided: {divmath}")


print(f"\nArray Sum: {np.sum(array)}")
print(f"\nArray Max: {np.max(array)}")
print(f"\nArray Min: {np.min(array)}")
print(f"\nArray Standard Deviation: {np.std(array)}")

print(f"\nArray2 Sum: {np.sum(array2)}")
print(f"\nArray2 Max: {np.max(array2)}")
print(f"\nArray2 Min: {np.min(array2)}")
print(f"\nArray2 Standard Deviation: {np.std(array2)}")