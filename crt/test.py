n = int(input("Enter number of elements: "))
a = []
for i in range(n):
    num = int(input("Enter element: "))
    a.append(num)
for i in range(n):
    for j in range(i + 1, n):
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
print("Array after sorting:", a)
target = int(input("Enter the value to search: "))
start = 0
end = n - 1
found = False

while start <= end:
    mid = (start + end) // 2

    if a[mid] == target:
        print("Target found at index:", mid)
        found = True
        break

    if target < a[mid]:
        end = mid - 1
    else:
        start = mid + 1

if found == False:
    print("Not found")


