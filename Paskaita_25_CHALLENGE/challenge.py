

import random

class Tank:
    def __init__(self, x=0, y=0, shoots=0):
        self.coordinates_list = []
        self.shoots_fired = {"North": 0, "South": 0, "East": 0, "West": 0}
        self.target_coordinates = {"X": [2], "Y": [1]}
        self.x = x
        self.y = y
        self.shoots = shoots


    def forward(self, new_y):
        self.coordinates_dict = {"X": [], "Y": [], "Direction": []}
        self.y=self.y+new_y
        self.coordinates_dict["X"].append(self.x)
        self.coordinates_dict["Y"].append(self.y)
        self.coordinates_dict["Direction"].append("North")
        self.coordinates_list.append(self.coordinates_dict)

    def backwards(self, new_y):
        self.coordinates_dict = {"X": [], "Y": [], "Direction": []}
        self.y=self.y-new_y
        self.coordinates_dict["X"].append(self.x)
        self.coordinates_dict["Y"].append(self.y)
        self.coordinates_dict["Direction"].append("South")
        self.coordinates_list.append(self.coordinates_dict)


    def left(self, new_x):
        self.coordinates_dict = {"X": [], "Y": [], "Direction": []}
        self.x = self.x - new_x
        self.coordinates_dict["X"].append(self.x)
        self.coordinates_dict["Y"].append(self.y)
        self.coordinates_dict["Direction"].append("West")
        self.coordinates_list.append(self.coordinates_dict)


    def right(self, new_x):
        self.coordinates_dict = {"X": [], "Y": [], "Direction": []}
        self.x = self.x + new_x
        self.coordinates_dict["X"].append(self.x)
        self.coordinates_dict["Y"].append(self.y)
        self.coordinates_dict["Direction"].append("East")
        self.coordinates_list.append(self.coordinates_dict)


    def shoot(self):
        if self.coordinates_dict["Direction"]==["North"]:
            new = self.shoots_fired["North"] + 1
            self.shoots_fired["North"] = new

        if self.coordinates_dict["Direction"]==["South"]:
            new = self.shoots_fired["South"] + 1
            self.shoots_fired["South"] = new

        if self.coordinates_dict["Direction"]==["West"]:
            new = self.shoots_fired["West"] + 1
            self.shoots_fired["West"] = new

        if self.coordinates_dict["Direction"] == ["East"]:
            new = self.shoots_fired["East"] + 1
            self.shoots_fired["East"] = new

    def shoot_result(self):
        coordinates = self.coordinates_list[-1]
        if coordinates["Y"] == self.target_coordinates["Y"]:
            if coordinates["X"] < self.target_coordinates["X"] and coordinates["Direction"] == ["East"]:
                # self.target_coordinates["X"] = random.randint(1, 5)
                # self.target_coordinates["Y"] = random.randint(1, 5)
                return True

            elif coordinates["X"] > self.target_coordinates["X"] and coordinates["Direction"] == ["West"]:
                # self.target_coordinates["X"] = random.randint(1, 5)
                # self.target_coordinates["Y"] = random.randint(1, 5)
                return True

            return False
        if coordinates["X"] == self.target_coordinates["X"]:
            if coordinates["Y"] < self.target_coordinates["Y"] and coordinates["Direction"] == ["North"]:
                # self.target_coordinates["X"] = random.randint(1, 5)
                # self.target_coordinates["Y"] = random.randint(1, 5)
                return True

            elif coordinates["Y"] > self.target_coordinates["Y"] and coordinates["Direction"] == ["South"]:
                # self.target_coordinates["Y"] = random.randint(1, 5)
                # self.target_coordinates["Y"] = random.randint(1, 5)
                return True

            return False



    def info(self):
        total_shoots=0
        for i in self.shoots_fired.values():
            total_shoots+=i

        return f'Your Coordinates: {self.coordinates_list[-1]},\nTarget Coordinates: {self.target_coordinates}\nYour Shoots: {self.shoots_fired}, \nTotal shoots: {total_shoots}'

tank = Tank()

while True:

    choice = int(input(
        "Choose\n1.Input move\n2.Info\n3.Shoots\n4.Shoot result\n5.Quit"))
    if choice == 1:
        move_choice = int(input("Choose your move: 1 - forward, 2 - backward, 3 - left, 4 - right "))
        if move_choice == 1:
            forward_y = int(input("How much forward? "))
            tank.forward(forward_y)
        if move_choice == 2:
            backward_y = int(input("How much backward? "))
            tank.backwards(backward_y)
        if move_choice == 3:
            left_x = int(input("How much left? "))
            tank.left(left_x)
        if move_choice == 4:
            right_x = int(input("How much right? "))
            tank.right(right_x)
    if choice == 2:
        print(tank.info())
    if choice == 3:
        tank.shoot()
        print("Boom")
        print(tank.shoot_result())
    if choice == 5:
        print("End of game")
        break




