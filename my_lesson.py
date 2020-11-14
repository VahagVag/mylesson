# names = ["Artur","Jon","Ani"]
# for name in names:
# 	if name == "Jon":
# 		pass	
# 	print(name)

# for x in range(1,30,2):
# 	print(x)

# color = "123"
# fruit = "123456"
# for x in color:
# 	for y in fruit:
# 		print(x,y)

# i = 1
# while i<6:
# 	print(i)
# 	if i == 3:
# 		break
# 	i += 1
# 	

# import random
# pc = random.randint(1,10)
# while True:
# 	user = int(input("write the number "))
# 	if user == pc:
# 		print(pc)
# 		print(user)
# 		print("you are win")
# 		break
# 	elif user > 10 or user < 1:
# 		print("no correct")

# import random
# ch = ['qar','tuxt','mkrat']
# user_poit = 0
# pc_point = 0
# rounds = int(input("Qanisiceq uzum xax@ lini?"))
# while True:
# 	pc = random.choice(ch)
# 	user = input("dzer xax@ ")
# 	print(pc)
# 	if pc == user:
# 		pass
# 	elif (user == "qar" and pc == "mkrat") or (user == "tuxt" and pc == "qar") or (user == "mkrat" and pc == "tuxt"):
# 		user_poit += 1
# 	else:
# 		pc_point += 1

# 	if user_poit == rounds:
# 		print(user_poit,pc_point)
# 		print("You are win")
# 		break
# 	elif pc_point == rounds:
# 		print(user_poit,pc_point)
# 		print("you lose")
# 		break	

# n = 1
# while True:
# 	if n % 12 == 0 and n % 15 == 0:
# 		print(n)
# 		break
# 	n += 1
# even = 0
# odd = 0
# for x in range(1,100):
# 	if x % 2 == 0:
# 		even += 1
# 	else:
# 		odd += 1
# print(even,odd)	

# x = 0
# y = 1
# while y < 40:
# 	print(y)
# 	x,y = y,x+y

# string = "python 3.9"
# number_count = 0
# letter_count = 0
# simbol_count = 0
# for x in string:
# 	if x.isdigit():
# 		number_count += 1
# 	elif x.isalpha():
# 		letter_count += 1
# 	else:
# 		simbol_count += 1	
# print(number_count,letter_count,simbol_count)


# number = "734"
# result = 0
# for x in number:
# 	result += int(x)
# print(result)		

# number = int(input("Write the number"  ))
# result = 1
# if number == 0:
# 	print(1)
# else:
# 	for x in range(number,0,-1):
# 		result *= x 
# 	print(result)

# sex = input("Your gender? ")
# age = int(input("Your age? "))
# errors = 0
# if sex != "male":
# 	print("your sex is not valid")
# 	errors+=1
# if age < 18 or age > 20:
# 	print("your age is not valid")
# 	errors+=1
# if errors == 0:
# 	print("Thank you")







	



	
