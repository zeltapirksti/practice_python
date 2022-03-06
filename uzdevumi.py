# p = 0
# while p < 10:
#     print(p)
#     p = p + 1

# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#         j += 1
#     print("")

# number = int(input("Please input integer: "))
# total_sum = 0
# for i in range(1, number):
#     total_sum += i
#     print(i, end=' + ')
# total_sum += number
# print(number, end=' = ')
# print(total_sum)

is_prime = False
a = int(input("Please input number to check whether it's prime: "))
for i in range(a - 1, 2, -1):
    print(i)
    if a % i == 0:
        is_prime = True
        break
if is_prime == True:
    print(a, "is a prime number :)")
else:
    print(a, "is not a prime number :(")

