def sequentialSearch(List, s):
    for k in range(len(List)):
        if s == List[k]:
            return k
    return -1


l1 = []

while True:
    try:
        n = int(input("Enter a size of the list : "))
        print()
        break
    except ValueError:
        print("Invalid input, Enter again ")
        print()

print("Enter the elements in the list : ")

for i in range(n):
    val = input()
    l1.append(val)

print()

x = input("The element to be searched : ")

result = sequentialSearch(l1, x)
print()

if result == -1:
    print("Element is not present in list")
else:
    print("Element is present in list at index {} ".format(result))
