def test_config():
    return True

def is_number_in_range(value1, min_range, max_range):
    return value1 >= min_range and value1 <= max_range

def is_number_not_in_range(value1, min_range, max_range):
    return value1 <= min_range or value1 >= max_range

def get_generation(year):

    result = ''

    if(year >= 1996 and year <= 2014):
        result = 'Centennial'
    elif(year >= 1977 and year <= 1995):
        result = 'Millenial'
    elif(year >= 1965 and year <= 1976):
        result = 'Generation X'
    elif(year >= 1946 and year <= 1964):
        result = 'Baby Boomer'
    elif(year >= 1925 and year <= 1945):
        result = 'Silent Generation'
    else:
        result = 'Invalid Option'

    return result