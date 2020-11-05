password = 'a123456'
p = input('請輸入密碼:')
x = 1
while x <= 3 :
	if password != p :
		print('輸入錯誤請重新輸入''，剩餘', 3 - x ,'次機會')
		p = input('請重新輸入密碼:')
	x = x + 1
	if x > 3:
		print('帳號已鎖住請聯絡客服人員')
	if password == p :
		print('登入成功')