#
def create_sets():
    my_set = (['a'], ['b'], ['c'])

    print(my_set)

    my_set1 = set() #empty set
    my_set1.add('a')
    my_set1.add('b')
    my_set1.add('c')
    print(my_set1)

    my_set1.remove('a')
    print(my_set1)