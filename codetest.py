passward = 'a123456'
i = 0
while i < 3:
	answer = input('請輸入密碼:(最多輸入三次密碼)')
	i = i + 1
	j = 3 - i
	if answer == passward:
		print('登入成功!')
		break
		else:
		print('密碼錯誤,您還有',j,'次機會')
		if j ==0:
		print ('您登入失敗了，跳出!!')
		break