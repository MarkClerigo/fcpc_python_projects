print("Multiplication Table\n")

print("By 2")
for x in range(2,13,2):
    print(x)

print("\nBy 3")
for x in range(3,34,3):
    print(x)
print("\nBy 4")
for y in range(4,49,4):
    print(y)
print("\nBy 12")
for z in range(12,121,12):
    print(z)
 
#nested loop sample
print("\nMultiplication Table By 10 to 20")
for a in range(10,21):
    for b in range(1,11):
        print(a*b,end='\t')
    print()
