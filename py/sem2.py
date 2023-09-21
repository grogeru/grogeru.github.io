"""Задание №1"""

# data = list(map(int, input().split()))
# nema = 0
# summa = 0
# for i in range(data[0]):
#     summa += i + 1
# for i in range(1, data[0]):
#     nema += data[i]
# print(summa - nema)


"""Задание №2"""

# data = input().split()
# n = int(data[0])
# line = data[1]
#
# p = [line[i: i + n][::-1] for i in range(len(line)) if i % n == 0]
# answer = ""
# for item in p:
#     answer += item
# print(answer)

"""Задача №3"""

# a = input()
# def check_palindrome(a):
#     if a == a[::-1]:
#         print("Palindrome")
#     else:
#         print("Not palindrome")
# check_palindrome(a)
#
# def check_mirrored_str(a):
#     mirror_dict = {'A': 'A', 'H': 'H', 'I': 'I', 'M': 'M', 'O': 'O', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W','X': 'X', 'Y': 'Y', '1': '1', '8': '8', 'E': '3', 'J': 'L', 'S': '2', 'Z': '5', '3': 'E', '2': 'S', '5': 'Z',
#                            'L': 'J'}
#     for c in a:
#         if c not in mirror_dict:
#             print("Not mirrored_str")
#     mirror_s = ""
#     for c in a[::-1]:
#         mirror_s += mirror_dict[c]
#     if a == mirror_s:
#         print("Mirrored_str")
#     else:
#         print("Not a mirrored_str")
# check_mirrored_str(a)
#
# def check_mirr_palindrome(a):
#     mirror_dict = {'A': 'A', 'H': 'H', 'I': 'I', 'M': 'M', 'O': 'O', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W','X': 'X', 'Y': 'Y', '1': '1', '8': '8', 'E': '3', 'J': 'L', 'S': '2', 'Z': '5', '3': 'E', '2': 'S', '5': 'Z',
#                            'L': 'J'}
#     for c in a:
#         if c not in mirror_dict:
#             print("Not mirr_palindrome")
#     mirr_pal = ""
#     for c in a[::-1]:
#         mirr_pal +=mirror_dict[c]
#     if a == mirr_pal:
#         if a==a[::-1]:
#             print("Mirr_palindrome")
#     else:
#         print("Not mirr_palindrome")
# check_mirr_palindrome(a)

"""Задача №4"""
# a = input().split(" ")
# for i in range(1, len(a), 2):
#     a[i - 1], a[i] = a[i], a[i - 1]
# print(a)

"""Задача №5"""

# a = input().split(" ")
# a.insert(0, a.pop())
# print(a)


"""Задача №6"""

# data = input().split()
# answer = []
# for i in data:
#     if data.count(i) == 1:
#         answer.append(i)
# print(" ".join(answer))


"""Задача №7"""

# max_in = 0
# MAX_value = 0
# data = list(map(int, input().split()))
# for i in data:
#     s = data.count(i)
#     if s > max_in:
#         max_in = s
#         MAX_value = i
# print(MAX_value)

"""Задача №8"""

# a = input().split(" ")
# l = len(a)
# for i in range(len(a)):
#     for j in range(len(a)-i-1):
#         if a[j]>a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]
# print(a[len(a)//2])


"""Задача №9"""

# separator = [".", "...", "!", "?", "?!"]
# with open("input.txt", "r") as in_file:
#     data = in_file.read()
#     num1 = data.count("?!")
#     num2 = data.count("...")
#     num3 = data.count(".") - 3 * num2
#     num4 = data.count("!") - num1
#     num5 = data.count("?") - num1
#     sent = num1 + num2 + num3 + num4 + num5
# print(sent)
#


"""Задача №10"""

# n = ""
# gl = "а, у, о, ы, и, э, я, ю, ё, е"
# sogl = "б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ"
# with open("input_1.txt", "r") as f:
#     text = f.read()
# for i in range(len(text)):
#     if text[i] in gl:
#         if i< len(text)-1 and text[i+1] in sogl:
#             n += text[i] + "с" + text[i]
#         else:
#             n += text[i]
#     else:
#         n += text[i]
# print(n)