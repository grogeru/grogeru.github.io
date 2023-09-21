"""Упражнение 1"""
#
# a = int(input())
# b = int(input())
# print(a + b)
# print(a - b)
# print(a * b)
#

"""упражнение 2"""

# a = input()
# print(a[-1])
# print(int(a) % 10)


"""упражнение 3"""

# a = list(map(int, input().split()))
# multi = 1
# for i in a:
#     multi *= i
# print(multi ** (len(a) ** -1))

"""упражнение 4"""


# def func(n, s):
#     if s == "-":
#         return n[0] - n[1]
#     elif s == "+":
#         return n[0] + n[1]
#     elif s == "*":
#         return n[0] * n[1]
#     else:
#         return "error"
#
#
# f = open('input.txt', 'r')
# lines = f.read().split('\n')
# nums = list(map(int, lines[0].split()))
# f.close()
# out = open("output.txt", "w")
# out.write(str(func(nums, lines[1])))
# out.close()

"""упражнение 5"""

# N = int(input())
# b = int(input())
# c = int(input())
#
#
# def f_to_10(n, base):
#     s = str(n)
#     res = 0
#     for i in range(len(s)):
#         res += base ** i * int(s[-i - 1])
#     return res
#
#
# def f_to_z(n, z):
#     list = []
#     while n // z > 0:
#         list.append(n % z)
#         n //= z
#     list.append(n)
#     answer = ""
#     list.reverse()
#     for i in list:
#         answer += str(i)
#     return int(answer)
#
# print(f_to_z(f_to_10(N, b), c))

"""упражнение 6"""

#
# def operation(n, s):
#     if s == "-":
#         return n[0] - n[1]
#     elif s == "+":
#         return n[0] + n[1]
#     elif s == "*":
#         return n[0] * n[1]
#     else:
#         return "error"
#
#
# def f_to_10(n, base):
#     s = str(n)
#     res = 0
#     for i in range(len(s)):
#         res += base ** i * int(s[-i - 1])
#     return res
#
#
# def f_to_z(n, z):
#     list = []
#     while n // z > 0:
#         list.append(n % z)
#         n //= z
#     list.append(n)
#     answer = ""
#     list.reverse()
#     for i in list:
#         answer += str(i)
#     return int(answer)
#
#
# f = open("input.txt", "r")
# lines = f.read().split("\n")
# numbers = list(map(int,lines[0]))
# s = lines[1]
# base = int(lines[2])
# f.close()
#
# answer = open("output.txt", "w")
# answer.write(str(f_to_z(operation(f_to_10(numbers[0], base), f_to_10(numbers[1], base)),base)))
# answer.close()



f = open('f')
d = []
for i in range(3301):
    d += [int(f.readline())]
k = 1
s = 0
for i in range(len(d)):
    if k < 80:
        s += d[i]
        k+=1
    else:
        s += d[i]
        print(s)
        k = 1
        s = 0
f.close()
answer = open('output.txt', 'w')
for item in d:
    answer.write(str(item))
answer.close()
