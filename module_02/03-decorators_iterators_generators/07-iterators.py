# in Python, an iterator is an object that contains a countable number of values ​​that can be iterated over, meaning you can traverse all the values
# the iterator protocol is a way for Python to iterate over an object, consisting of two special methods: "__iter__()" and "__next__()"

# most common use: reading large files; saves memory because it avoids loading all lines of the file, since it iterates line by line.

# EXAMPLE:
'''
class FileIterator():
    def __init__(self, filename):
        self.file = open(filename)

    def __iter__(self):
        return self
    
    def __next__(self):
        line = self.file.readline()
        if (line != ''):
            return line
        else:
            self.file.close()
            raise StopIteration

# using FileIterator
for line in FileIterator('larg_file.txt'):
    print(line)
'''

class MyIterator():
    def __init__(self, nums: list[int]):
        self.nums = nums
        self.couting = 0

    def __iter__(self):
        return(self)
    
    def __next__(self):
        try:
            num = self.nums[self.couting]
            self.couting += 1
            return num * 2
        except IndexError:
            raise StopIteration
            # "raise StopIteration": it signals the end of an iterator, interrupting a for loop or next() calls when there are no more items, it is fundamental in creating custom iterators to indicate the completion of the data sequence.

# using MyIterator:
my_numbers = MyIterator(nums=[4, 2, 18, 19])
for i in my_numbers:
    print(i)