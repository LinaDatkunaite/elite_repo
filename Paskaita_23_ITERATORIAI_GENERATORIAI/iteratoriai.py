# iteratorius - objektas kuris sukuria galimybe iteruoti
# iterables - list, string, tuple, dict, files, generators - visi masyvai/objektai kuriuos galim praiteruoti


# __iter__() ir __next__():
# iteratorius turi tureti __iter__() klases metoda BUTINAI!
# iteratoriai papildomai turi __next__() metoda, o paprasti masyvai __next__() neturi

# for loopas tam tikra prasme pasleptas iteratorius
# nums = [1, 2, 3]
# for num in nums:
#     print(num)

# galime pamatyti kokias funkcijas turi - matome kad listas turi iter f-ja
# print(dir(nums))

# -------------------------------------------

# is listo padarykime iteratoriu:
# nums = [1, 2, 3]
#
# # abu sie yra metodai sukurti iteri
# # i_nums = nums.__iter__()
# i_nums = iter(nums)
#
# print(dir(i_nums))
#
# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))
# # StopIteration po 3 nes nebera liste 4 duomens
# print(next(i_nums))

# -----------------------------------------------
# kad nereiktu rasyti next daug kartu
# nums = [1, 2, 3]
# i_nums = iter(nums)
#
# while True:
#     try:
#         item = next(i_nums)
#         print(item)
#     except StopIteration:
#         break


# -----------------------------------------------
# Class example - iterators

class MyRange:
    def  __init__(self, start, end):
        self.start=start
        self.end=end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        current_value = self.start
        self.start+=1
        return current_value

# Taip:
nums = MyRange(1,10)
for num in nums:
    print(num)

# Arba taip:
nums = MyRange(1,5)
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))





