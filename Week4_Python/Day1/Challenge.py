str1 = input("Type some text: ")

if len(str1) < 10:
	print("string not long enough")
elif len(str1)> 10:
	print("string too long")

print(str1[0] + str1[-1])

str2=""
for element in str1:
	str2=element+1
	print(str2)
