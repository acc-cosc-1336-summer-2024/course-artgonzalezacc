import array

def test_config():
    return True

def create_array():
    nums = array.array('i', [6, 1, 3, 10])

    nums.append(4)
    nums.insert(2, 0)

    for n in range(0, len(nums)):
        print(nums[n])

