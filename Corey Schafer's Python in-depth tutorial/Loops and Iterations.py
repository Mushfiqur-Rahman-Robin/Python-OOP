nums = [1,2,3,4,5]

for num in nums:
    if num == 3:
        print('Number found!')
        break
    print(num)

for num in nums:
    if num == 3:
        print('Number found!')
        continue
    print(num)

for num in nums:
    for letter in 'abc':
        print(num, letter)

for i in range(20):
    print(i)

for i in range(1, 21):
    print(i)

x = 0
while x < 10:
    print(x)
    x += 1

x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x = x + 1

x = 0
while True:
    if x == 5:
        break
    print(x)
    x = x + 1 