soma = 0
for i in range(500):
    if i % 3 == 0 and i % 2 != 0:
        soma += i
    else:
        continue

print(soma)

for i in range(9, -1, -1):
    for j in range(59, -1, -1):
        seg = j
        print("{0}:{1}".format(i, seg))

nums = []

nums = []
count = 0

while count < 10:
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        nums.append(num)
        count += 1

media = sum(nums) / len(nums)
print("A soma dos números pares é: {}".format(media))
