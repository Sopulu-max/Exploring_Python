nums = []

for i in nums:
    if i <= 4:
        nums.append(i)
        i += 1
print(nums)

def random_behaviour(a, b, c, d):
    e = a - b
    f = c + d
    g = a + c
    h = b + d
    arr = [e, f , g, h]
    for i in arr:
        print(i)
    return arr

print(random_behaviour(1, 2, 3, 4))

