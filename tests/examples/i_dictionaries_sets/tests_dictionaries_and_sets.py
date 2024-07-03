import unittest

from src.examples.i_dictionaries_sets.dictionaries import test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_set_union(self):
        set1 = set([1,2,3,4])
        set2 = set([3,4,5,6])

        union_set = set1.union(set2)
        expected_set = set([1,2,3,4,5,6])
        
        self.assertEqual(union_set, expected_set)

    def test_set_intersection(self):
        set1 = set([1,2,3,4])
        set2 = set([3,4,5,6])

        intersection_set = set1.intersection(set2)
        expected_set = set([3, 4])

        self.assertEqual(intersection_set, expected_set)


    def test_set_difference_set1(self):
        set1 = set([1,2,3,4])
        set2 = set([3,4,5,6])

        difference_set = set1.difference(set2)
        expected_set = set([1,2])

        self.assertEqual(difference_set, expected_set)

    def test_set_difference_set2(self):
        set1 = set([1,2,3,4])
        set2 = set([3,4,5,6])

        difference_set = set2.difference(set1)
        expected_set = set([5,6])

        self.assertEqual(difference_set, expected_set)

    def test_symmetric_difference(self):
        set1 = set([1,2,3,4])
        set2 = set([3,4,5,6])

        sym_dif_set = set1.symmetric_difference(set2)
        expected_set = set([1,2,5,6])

        self.assertEqual(sym_dif_set, expected_set)

    def test_set_subset(self):
        set1 = set([1,2,3,4])
        set2 = set([2,3])

        self.assertEqual(set2.issubset(set1), True)

    def test_set_superset(self):
        set1 = set([1,2,3,4])
        set2 = set([2,3])

        self.assertEqual(set1.issuperset(set2), True)

    def test_students_in_baseball_and_basketball(self):
        baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
        basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])
        expected_set = set(['Jodi', 'Carmen', 'Aida', 'Alicia', 'Eva', 'Sarah'])

        both_sports = baseball.union(basketball)

        self.assertEqual(both_sports, expected_set)

    def test_students_in_baseball_not_in_basketball(self):
        baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
        basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])
        expected_set = set(['Jodi', 'Aida'])

        only_in_baseball_set = baseball.difference(basketball)

        self.assertEqual(expected_set, only_in_baseball_set)

    def test_students_who_play_only_one_sport(self):
        baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
        basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])
        expected_set = set(['Jodi', 'Aida', "Eva", "Sarah"])

        both_sports_set = baseball.symmetric_difference(basketball)

        self.assertEqual(expected_set, both_sports_set)


        



    







