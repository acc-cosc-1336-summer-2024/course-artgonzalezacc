def test_config():
    return True

def create_string():
    lang = "Python" #create the string
    print(lang)

def access_characters_in_a_string():
    lang = "Python"
    print(lang[0])
    print(lang[5])

def cannot_change_string_characters():
    lang = "Python"

    lang[0] = 'P' #can't change characters in a string

def loop_string_w_while():
    lang = "Python"
    indx = 0

    while(indx < len(lang)):
        print(lang[indx])
        indx += 1 #statement that eventually stops the loop

def loop_string_w_for():#function header
    lang = "Python is great"

    for i in range(0, len(lang)):
        print(lang[i])

