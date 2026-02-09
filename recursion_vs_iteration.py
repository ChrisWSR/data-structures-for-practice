def array_product(arr):
    total = 1
    for n in arr: 
        total *=n
    return total
array =[2,5,6]
print(array_product(array))
def array_product_recursive(arr):
    if not arr:
        return 1
    return arr[0] *   array_product_recursive(arr[1:])

print(array_product_recursive(array))
