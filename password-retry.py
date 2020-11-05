password = 'a123456'
p = input('請輸入密碼:')
x = 1
x = int(x)
while password != p and x < 3:
	print('密碼錯誤請重新輸入,你還剩餘',3 - x,'次機會')

	p = input('請輸入密碼:')
	x = x + 1
if x >= 3 :
		print('帳號已鎖定無法輸入')
if password == p and x <= 3:
	print('登入成功')
	