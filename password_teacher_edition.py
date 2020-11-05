password = 'a123456'
i = 3
while i > 0 :
	pwd = input('請輸入密碼:')
	if pwd == password :
		print('登入成功')
		break #沒有整個會沒辦法跳出迴圈
	else: 
		i = i - 1
		print('密碼錯誤! 還有',i ,'次機會')