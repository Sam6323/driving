country = input('請輸入你的國家: ')
age = int(input('請輸入你的年齡: '))
if country == 'Taiwan' :
	if age >= 18 :
		print('你可以考駕照')
	else:
		print('你還不能考駕照')
elif country == 'US' :
	if age >= 16 :
		print('你可以考駕照')
	else :
		print('你還不能考駕照')
#else :
#	input('請按Enter,重新輸入國家')