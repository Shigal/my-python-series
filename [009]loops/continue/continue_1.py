# Print 1 to 10, but not 5
# when i=5, everything after continue is skipped


for i in range(1,10):
    if i == 5:
        continue
    print(i)

print('------------------------------------------------------')

n = 1
while n <= 10:
    if n == 5:
        n +=1
        continue
    print(n)
    n += 1
    
