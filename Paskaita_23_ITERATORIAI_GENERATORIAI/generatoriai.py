# generatorius - tas pats kas iteratorius tik generatoriuose iter ir next yra integruoti
# vietoj return kvieciam yield. yield neisaufgo generuotos vertes atminty, issaugo tik viena cikla
# generatoriai labai veiksmingi nes atmintyje nesaugo - atminty lieka tik vienas yieldas

# sukurkime generatoriu:
# def my_range(start, end):
#     current_value = start
#     while current_value<end:
#         yield current_value
#         current_value+=1
#
# nums = my_range(1,10)
# # cia yra generatoriaus objektas
# print(nums)
# for i in nums:
#     print(i)


# infinite generator:
# def infinite(start):
#     current=start
#     while True:
#         yield current
#         current+=1
#
# nums = infinite(1)
# for num in nums:
#     print(num)


# ---------------------------------------------------------
# def counter(stop_at):
#     count = 1
#     while count < stop_at:
#         yield count
#         count +=1
# count = counter(20)
# print(next(count))
# print(next(count))
# needed_list = list(count)
# print(needed_list)


# ---------------------------------------------------------
# import time
# import itertools
#
# start_time = time.time()
# list_of_cubes = [x**3 for x in range(1_000_000)]
# delta_time = time.time() - start_time
# print(f"List of cubes created in {delta_time: .2f} seconds")
#
# start_time = time.time()
# cube_generator =(x**3 for x in range(1_000_000))
# delta_time = time.time() - start_time
# print(f"Generator of cubes created in {delta_time: .2f} seconds")
#
# print(list_of_cubes[:15])
# print(list(itertools.islice(cube_generator, 15)))


