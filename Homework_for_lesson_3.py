# task 1
word = input('Enter the word: ')
if word == word[::-1]:
    print('+')
else:
    print('-')

# task 2
user_text = input('Enter the sentence: ')
search_word = input('Enter the search word: ')
words = user_text.split()
if search_word in words:
    print('YES')
else:
    print('NO')

# task 3
custom_input = input('Enter the sentence: ')
if custom_input.startswith('abc'):
    custom_input = 'www' + custom_input[3:]
else:
    custom_input += 'zzz'
print(custom_input)

# task 4
email = input('Enter email:')
if email.count('@') == 1 and email.count('.') == 1:
    print('YES')
else:
    print('NO')

# task 5
users_input = input('Enter some text: ')
users_list = users_input.split()
if len(users_list) >= 3:
    print(users_list[-3:])
else:
    print(f'Number of characters is less than 3, actual number is: {len(users_list)}')