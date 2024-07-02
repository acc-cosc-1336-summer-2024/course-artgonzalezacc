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
