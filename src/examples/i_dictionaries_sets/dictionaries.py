import pickle

def test_config():
    return True

def create_dictionary():
    prog_langs = {'C++':'1979', 'Java':'1992', 'Python':'1996', 'C#':'2001'} #4 pairs keys/values
    print(prog_langs)
    print(prog_langs['C++'])
    print(prog_langs['Python'])

    if 'C+++' in prog_langs:
        print(prog_langs['C+++'])

    prog_langs['Ada'] = '1980' #add key/value pair
    print(prog_langs)

    prog_langs['C++'] = '1980'
    print(prog_langs)

    if 'C#' in prog_langs:
        del prog_langs['C#']
        print(prog_langs)

    if 'C#' in prog_langs:
        del prog_langs['C#']
        print(prog_langs)

    prog_langs['C#'] = 2001
    print(prog_langs)

def use_for_loop_dictionary():
    prog_langs = {'C++':'1979', 'Java':'1992', 'Python':'1996', 'C#':'2001'} #4 pairs keys/values

    for current_key in prog_langs:
        print(current_key, prog_langs[current_key])

    for current_value in prog_langs.values():
        print(current_value)

    for keys, values in prog_langs.items():
        print(keys, values)

def use_while_loop_dictionary():
    prog_langs = {'C++':'1979', 'Java':'1992', 'Python':'1996', 'C#':'2001'} #4 pairs keys/values

    keys = prog_langs.keys()
    print(keys)
    keys_list = list(keys)
    print(keys_list)

    indx = 0

    while indx < len(keys_list):
        print(prog_langs[keys_list[indx]])
        indx += 1

def dictionary_built_in_methods():
    prog_langs = {'C++':'1979', 'Java':'1992', 'Python':'1996', 'C#':'2001'} #4 pairs keys/values

    prog_langs.clear()
    print(prog_langs)

    prog_langs = {'C++':'1979', 'Java':'1992', 'Python':'1996', 'C#':'2001'} #4 pairs keys/values

    value = prog_langs.get('c++', 'Key not found')
    print(value)

    value = prog_langs.get('C++', 'Key not found')
    print(value)

    item = prog_langs.popitem()
    print(prog_langs)
    print(item)

    item = prog_langs.popitem()
    print(prog_langs)
    print(item)

def output_a_dictionary_to_file():
    phone_book = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}

    file = open('phonebook.dat', 'wb')
    pickle.dump(phone_book, file)

    file.close()

def read_a_pickled_dictionary_file():
    file = open('phonebook.dat', 'rb')

    phone_book = pickle.load(file)

    print(phone_book)


