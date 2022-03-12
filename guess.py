import random

r = random.randint(1, 100)
count = 0

while True:
	print('你已經猜', count, '次了')
	user = input('猜猜數字是多少 ')
	count = count + 1
	if r == int(user):
		print('你猜對惹')
		break
	elif r > int(user):
		print('比答案小唷')
	elif r < int(user):
		print('比答案大唷')