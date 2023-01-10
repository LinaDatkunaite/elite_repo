# class Target:
#     def __init__(self, x=1, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"{self.x}, {self.y}"
#
# a = Target()
# print(a)

coordinates = {'X': [-2], 'Y': [1], 'Direction': ['North']}
print(coordinates["X"])
print(coordinates["Direction"])
target_coordinates = {"X": [-2], "Y": [3]}
print(target_coordinates["X"])
if coordinates["X"] == target_coordinates["X"]:
    print(True)