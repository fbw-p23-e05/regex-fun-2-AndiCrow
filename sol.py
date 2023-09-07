import re
# #Task 1

# pattern = r"\d$"

# print(re.search(pattern, "lol 156 does works 9"))


# #Task 2

# # pattern2 = "[0-9]{1,3}"

# # print(re.findall(pattern2, input("Enter your numbers here:")))

# #Task 3

# text = 'The quick brown fox jumps over the lazy dog.'

# pattern3 = r"\bfox\b|\bdog\b|\bhorse\b"

# print(re.findall(pattern3, text))


# #Task 4

# text2 ='The quick brown fox jumps over the lazy dog.' 
# pattern4 = r'\bfox\b'

# found =(re.search(pattern4, text2))
# print(re.search(pattern4, text2))
# if found:
#     start = found.start()
#     end = found.end()
#     print(start, end)
# else:
#     print("not found")


# #Task 5
# text3 = 'Python exercises, PHP exercises, C# exercises'

# pattern5 = 'exercises'

# print(re.findall(pattern5, text3))



# #Task 6

# pattern6 = r'y'

# print(re.search(pattern6, text3))


#Task 7
text4 = 'Python_exercises, PHP_exercises, C#_exercises'
# pattern7 = r'\s'
# replaced_ch = r"_"


# result = re.sub(pattern7, lambda match: replaced_ch if match.group() == ' ' else '_', text4)
# print(text4)
# print(result) not try regex anymore on this. still not going to 



#Task 8

# url = input(("Here your url: "))
# pattern8 = r'\d{2,4} \d{2} \d{2}'

# print(re.search(pattern8, url))


# #Task 9 
# url2 = (input(("yyyy mm dd: ")))
# pattern9 = r'(\d{2,4}) (\d{2}) (\d{2})'

# print(re.sub(pattern9, r'\3 \2 \1', url2))


#Task 10

# text5 = 'Python_exercises, PH_exercises, C#_exercises'

# pattern = r'(\bP)'

# print(re.findall(pattern, text5))

# counter = 0

# for P in text5:
#     if re.match(pattern,text5):
#         counter += 1

# if counter>= 2:
#     print("found 2")
# else:
#     print("found nothing")


#Task 11

# text6 = "1566 62 qwd 561q 51 d66 65"

# pattern11= r'\d+\.?\d*'

# found_num= re.findall(pattern11, text6)

# for num in found_num:
#     print(num)

#Task 12

text5 = 'Python exercises, PH exercises, C# exercises'

patern12 = r'\be|\ba'

print(re.findall(patern12, text5))

# Task 13

text6 = "1566 62 qwd 561q 51 d66 65"
pattern13= r'\d+\.?\d*'
num_pos= list(re.finditer(pattern13, text6))

for found in num_pos:
    number = found.group()
    start = found.start()
    end = found.end()
    print("nummber:",number,"from:",start,"to:", end)


#Task 14

text7 = 'Road to Python_exercises, PH_exercises, C#_exercises'
pattern14= r'\bRoad\b' 

print(re.sub(pattern14,r'Rd', text7))

#Task 15
text7 = 'Road to Python_exercises, PH_exercises, C#_exercises'

pattern15= r'\s|,|\.'

print(re.sub(pattern15, ':', text7))

#Task 16
text7 = 'Road to Python_exercises, PH_exercises, C#_exercises'

pattern15= r'\s|,|\.'

print(re.sub(pattern15, ':', text7, count=2))