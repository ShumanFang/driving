country = input('which country are you from: ')
age = input('please enter your age:')
age = int(age)
if country == 'Taiwan':
	if age >= 18:
		print('can take drivers test')
	else:
		print('cannot take drivers test')