'''
Write a procedure called oddTuples,
which takes a tuple as input, and returns a new tuple as output,
where every other element of the input tuple is copied, starting with the first one.
So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'),
then evaluating oddTuples on this input would
return the tuple ('I', 'a', 'tuple').
'''


def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    # Your Code Here
    index = 1
    result = []
    for i in aTup:
        index += 1
        if index % 2 == 0:
            result.append(int(i))
    return tuple(result)

# Test Case #1 ((10, 9, 9, 6, 8))
# print(oddTuples((10, 11, 9, 9, 9, 6, 6, 20, 8)))

# Test Case #2 ((1, 5, 7, 0))
# print(oddTuples((1, 12, 5, 9, 7, 1, 0)))
