list_ = ['python', 'c++', 'c', 'scala', 'java']
letter = 'c'

def count_letters(list, letter):
    i = 0
    for l in list:
        if letter in l:
            i += 1
    if i > 0:
        print(f'В списке {list} буква "{letter}" повторяется {i} раз')
    else:
        print(f'В списке {list} буквы "{letter}" нет')

count_letters(list_, letter)