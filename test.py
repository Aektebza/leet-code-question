from collections import Counter

arr = [5,4,7,8,4,8,8,3,7,7,6,3,7,6,5,6,8,4,5,7,4,7,7,5,2,5,6,6,8,1,6,8,8,8,9,3,2,9]
freq = Counter(arr)
print(freq)
print(freq.items())
for item,value in freq.items():
    print(item, value)