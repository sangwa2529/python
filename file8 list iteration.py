l=[10,20,30,40,50,60,70,80,90]
print(l)

t=len(l)
print(t)

for a in range (t):
    print(l[a])
    
print("\n")
print("Reverse Method")

for a in range (t-1, -1, -1):
    print(l[a])