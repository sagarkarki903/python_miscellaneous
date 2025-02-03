# import random
#
# # ans = random.randint(1, 10)
#
#
# def checker(guess):
#     ans = 2
#     if guess == ans:
#         return 2
#     return "None"
# if __name__ == "__main__":
#     while True:
#         try:
#             user = int(input("Guess the input between 1 and 10: "))
#             result = checker(user)
#             if result != "None":
#                 print(result)
#                 break
#         except ValueError:
#             print("Please enter a number")
#             continue
#
# Rough................................

hashed_pass = "F0F1C5D980C0250FDF423520A4A2921B20A:1"
print(hashed_pass.split(":"))