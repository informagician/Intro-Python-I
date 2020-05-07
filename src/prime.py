import sys

arg = sys.argv

num = int(arg[1])

div = []

for i in range(1,num):
    if num % i == 0:
        div.append(i)

print(div)
if len(div) == 1:
    print(f"{num} is prime!")
else:
    print(f"{num} is not prime!")