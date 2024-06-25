import unittest

from src.examples.g_lists_and_tuples.lists import return_sum_of_items, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_create_empty_list(self):
        list = []
        list.append(10)

        self.assertEqual(True, [10] == list)

    def test_find_item_in_a_list(self):
        nums = [2, 4, 6, 8, 10]
        found = 2 in nums

        self.assertEqual(True, found)

    def test_item_not_in_list(self):
        nums = [2, 4, 6, 8, 10]
        
        self.assertEqual(True, 11 not in nums)

    def test_list_append(self):
        nums = [2, 4, 6, 8, 10]
        nums.append(0)

        self.assertEqual(True, [2,4,6,8,10,0] == nums)

    def test_list_index(self):
        nums = [2, 4, 6, 8, 10]

        self.assertEqual(3, nums.index(8))
        self.assertEqual(True, nums[3] == 8)

    def test_copy_list(self):
        list1 = [1,2,3,4]
        list2 = list1 #list2 will point to the memory data of list1 

        list1[0] = 10

        self.assertEqual(True, list1 == list2) #list1 and list2 are the same list in memory
        self.assertEqual(True, list2[0] == 10)  #list1 and list2 are the same list in memory

    def test_create_new_list(self):
        list1 = [1,2,3,4]
        list2 = []

        for i in range(0, len(list1)):
            list2.append(i)

        list1[0] = 10

        self.assertEqual(False, list1 == list2)

    def test_sum_items_the_list(self):
        nums = [2, 4, 6, 8, 10]
        total = return_sum_of_items(nums)

        self.assertEqual(30, total)




    


    


