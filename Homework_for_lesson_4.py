# task 1
#print(str(["john", "marta", "james", "amanda", "marianna"]).title())
user_list = ["john", "marta", "james", "amanda", "marianna"]
user_str = ' '.join(user_list).title()
print(user_str)

print('------------------------------------------------')
# task 2
friends = ["John", "Marta", "James", "Amanda", "Marianna"]
print(f"{'NAME'.center(20, '*')}")
for friend in friends:
    print(f"{friend.rjust(20)}")

print('------------------------------------------------')
# task 3
import re

camel_case = ["FirstItem", "FriendsList", "MyTuple"]
snace_case = []
for name in camel_case:
    snace_case_names = re.sub('([a-z0-9])([A-Z])', r'\1_\2', name)
    snace_case.append(snace_case_names.lower())
print(snace_case)

print('------------------------------------------------')
# task 4
programing_languages = {'Python': 'Guido van Rossum',
                        'Java': 'James Gosling',
                        'C++': 'Bjarne Stroustrup',
                        'PHP': 'Rasmus Lerdorf'}
print(f'My favorite programming language is Python. It was created by {programing_languages.get("Python")}.',
      f'My favorite programming language is Java. It was created by {programing_languages.get("Java")}.',
      f'My favorite programming language is C++. It was created by {programing_languages.get("C++")}.',
      f'My favorite programming language is PHP. It was created by {programing_languages.get("PHP")}.', sep='\n')
programing_languages.pop('Java')
print(programing_languages)

print('------------------------------------------------')
# task 5
e2g = {'stork': 'storch',
       'hawk': 'falke',
       'woodpecker': 'specht',
       'owl': 'eule'}
print(e2g.get('owl'))
e2g['dog'] = 'hund'
e2g['cat'] = 'katze'
print(e2g)
print(list(e2g.keys()))
print(list(e2g.values()))

print('------------------------------------------------')
# task 6
subjects = {'science': {'physics': ['nuclear physics', 'optics', 'thermodynamics'], 'computer science': {}, 'biology': {}},
            'humanities': {},
            'public': {}}
print(subjects['science'].keys())
print()
print(subjects['science']['physics'])

print('------------------------------------------------')
# task 7
my_dict = {}
for i in range(1, 16):
    my_dict[i] = i ** 2
print(my_dict)