import array

def test_config():
    return True

def create_array():
    nums = array.array('i', [6, 1, 3, 10])

    nums.append(4)
    nums.insert(2, 0)

    for n in range(0, len(nums)):
        print(nums[n])

def create_list():
    nums = [2, 4, 6, 8, 10]

    print(nums[0])
    print(nums[1])
    print("length of the list", len(nums))

    print("iterate w a loop")

    for i in range(0, len(nums)):
        print(nums[i])

def loop_list_w_while():
    nums = [2, 4, 6, 8, 10]
    indx = 0

    while(indx < len(nums)):
        print(nums[indx])
        indx += 1

def use_different_data_types_in_a_list():
    items = [1, 2.5, True, "python"]

    for i in items: #fastest way to code- iterate a list
        print(i)

    print(items)

def return_sum_of_items(nums):
    
    sum = 0

    for n in nums:
        sum += n
    
    return sum

def list_within_a_list():
    master_list = [[1,2,3], [4,5,6], [7,8,9]]
    sub_list = master_list[0]

    print(sub_list)
    print(master_list[1])
    print(master_list[2])

def mulitiplication_matrix(rows, cols):

    list = []

    for i in range(0, rows):
        row_list = []

        for j in range(0, cols):
            row_list.append((i+1) * (j+1))

        list.append(row_list)

    print(list)

def working_w_tuples():

    read_only_list = (1,2,3,4) #tuple
    print(read_only_list[1])

    if 4 in read_only_list:
        print('4 exists')

    index = read_only_list.index(3)
    print(index)

    print(len(read_only_list))









