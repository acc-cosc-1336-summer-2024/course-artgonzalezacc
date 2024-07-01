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