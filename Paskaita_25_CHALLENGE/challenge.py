# class Target:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.target_dict = {"X": self.x, "Y": self.y}
#
#     def target_coordinates(self):
#         self.target_dict["X"] = self.x
#         self.target_dict["Y"] = self.y
#         return self.target_dict
#
#     def target_random_gen(self):
#         self.target_dict["X"] = random.randint(1, 10)
#         self.target_dict["Y"] = random.randint(1, 10)
#         return self.target_dict
#
# target = Target(1,0)

class Tank:
    def __init__(self, x=0, y=0, shoots=0):
        self.coordinates_dict = {"X": 0, "Y": 0, "Direction": ""}
        self.shoots_fired = {"North": 0, "South": 0, "East": 0, "West": 0}
        self.target_coordinates = {"X": -2, "Y": 3}
        self.x = x
        self.y = y
        self.shoots = shoots

    def forward(self, new_y):
        self.y = self.y + new_y
        self.coordinates_dict["X"] = self.x
        self.coordinates_dict["Y"] = self.y
        self.coordinates_dict["Direction"] = "North"

    def backwards(self, new_y):
        self.y = self.y - new_y
        self.coordinates_dict["X"] = self.x
        self.coordinates_dict["Y"] = self.y
        self.coordinates_dict["Direction"] = "South"

    def left(self, new_x):
        self.x = self.x - new_x
        self.coordinates_dict["X"] = self.x
        self.coordinates_dict["Y"] = self.y
        self.coordinates_dict["Direction"] = "West"

    def right(self, new_x):
        self.x = self.x + new_x
        self.coordinates_dict["X"] = self.x
        self.coordinates_dict["Y"] = self.y
        self.coordinates_dict["Direction"] = "East"

    def shoot(self):
        if self.coordinates_dict["Direction"] == ["North"]:
            new = self.shoots_fired["North"] + 1
            self.shoots_fired["North"] = new

        if self.coordinates_dict["Direction"] == ["South"]:
            new = self.shoots_fired["South"] + 1
            self.shoots_fired["South"] = new

        if self.coordinates_dict["Direction"] == ["West"]:
            new = self.shoots_fired["West"] + 1
            self.shoots_fired["West"] = new

        if self.coordinates_dict["Direction"] == ["East"]:
            new = self.shoots_fired["East"] + 1
            self.shoots_fired["East"] = new

    def shoot_result(self):

        if self.coordinates_dict["Y"] == self.target_coordinates["Y"]:
            if self.coordinates_dict["X"] < self.target_coordinates["X"] and self.coordinates_dict[
                "Direction"] == "East":
                return True
            elif self.coordinates_dict["X"] > self.target_coordinates["X"] and self.coordinates_dict[
                "Direction"] == "West":
                return True
            return False
        if self.coordinates_dict["X"] == self.target_coordinates["X"]:
            if self.coordinates_dict["Y"] < self.target_coordinates["Y"] and self.coordinates_dict[
                "Direction"] == "North":
                return True
            elif self.coordinates_dict["Y"] > self.target_coordinates["Y"] and self.coordinates_dict[
                "Direction"] == "South":
                return True
            return False

    def info(self):
        total_shoots = 0
        for i in self.shoots_fired.values():
            total_shoots += i

        return f'Your Coordinates: {self.coordinates_dict},\nTarget Coordinates: {self.target_coordinates}\nYour Shoots: {self.shoots_fired}, \nTotal shoots: {total_shoots}'


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
        print("-" * 3)
        print("Boom")
        print(tank.shoot_result())
        print("-" * 3)
    if choice == 5:
        print("End of game")
        break
