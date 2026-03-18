a = [12,5,27,3,18,9]

mn = a[0]
mx = a[0]

for i in a:
    if i < mn:
        mn = i
    if i > mx:
        mx = i

print(mn)
print(mx)