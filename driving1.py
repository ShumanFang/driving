country = input('which country are you from: ')
if country in ('Taiwan','US'):
	age = input('please enter your age:')
	age = int(age)
	if country == 'Taiwan' and age >= 18:
		print('yes you can take test')
	elif country == 'Taiwan' and age < 18:
		print('cannot take test')
	elif country == 'US' and age >= 16:
		print('can take test')
	else:
		print('cannot take test')
else:
	print('country has to be Taiwan or US')
