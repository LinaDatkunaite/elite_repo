import random
class Tank:
    def __init__(self, x=0, y=0, shoots=0):
        self.coordinates_dict = {"X": 0, "Y": 0, "Direction": ""}
        self.shoots_fired = {"North": 0, "South": 0, "East": 0, "West": 0}
        self.target_coordinates = {"X": -2, "Y": 3}
        self.x = x
        self.y = y
        self.shoots = shoots
        self.points = 100
        self.succesful_shoots = 0

    def forward(self, new_y):
        self.y = self.y + new_y
        self.coordinates_dict["X"] = self.x
        self.coordinates_dict["Y"] = self.y
        self.coordinates_dict["Direction"] = "North"
        self.points-=new_y*10

    def backwards(self, new_y):
        self.y = self.y - new_y
        self.coordinates_dict["X"] = self.x
        self.coordinates_dict["Y"] = self.y
        self.coordinates_dict["Direction"] = "South"
        self.points -= new_y * 10

    def left(self, new_x):
        self.x = self.x - new_x
        self.coordinates_dict["X"] = self.x
        self.coordinates_dict["Y"] = self.y
        self.coordinates_dict["Direction"] = "West"
        self.points -= new_x * 10

    def right(self, new_x):
        self.x = self.x + new_x
        self.coordinates_dict["X"] = self.x
        self.coordinates_dict["Y"] = self.y
        self.coordinates_dict["Direction"] = "East"
        self.points -= new_x * 10

    def shoot(self):
        if self.coordinates_dict["Direction"] == "North":
            new = self.shoots_fired["North"] + 1
            self.shoots_fired["North"] = new

        if self.coordinates_dict["Direction"] == "South":
            new = self.shoots_fired["South"] + 1
            self.shoots_fired["South"] = new

        if self.coordinates_dict["Direction"] == "West":
            new = self.shoots_fired["West"] + 1
            self.shoots_fired["West"] = new

        if self.coordinates_dict["Direction"] == "East":
            new = self.shoots_fired["East"] + 1
            self.shoots_fired["East"] = new

    def shoot_result(self):

        if self.coordinates_dict["Y"] == self.target_coordinates["Y"]:
            if self.coordinates_dict["X"] < self.target_coordinates["X"] and self.coordinates_dict[
                "Direction"] == "East":
                self.target_coordinates["X"] = random.randint(1, 5)
                self.target_coordinates["Y"] = random.randint(1, 5)
                self.points+=50
                self.succesful_shoots += 1
                return True
            elif self.coordinates_dict["X"] > self.target_coordinates["X"] and self.coordinates_dict[
                "Direction"] == "West":
                self.target_coordinates["X"] = random.randint(1, 5)
                self.target_coordinates["Y"] = random.randint(1, 5)
                self.points += 50
                self.succesful_shoots += 1
                return True
            return False
        if self.coordinates_dict["X"] == self.target_coordinates["X"]:
            if self.coordinates_dict["Y"] < self.target_coordinates["Y"] and self.coordinates_dict[
                "Direction"] == "North":
                self.target_coordinates["X"] = random.randint(1, 5)
                self.target_coordinates["Y"] = random.randint(1, 5)
                self.points += 50
                self.succesful_shoots += 1
                return True
            elif self.coordinates_dict["Y"] > self.target_coordinates["Y"] and self.coordinates_dict[
                "Direction"] == "South":
                self.target_coordinates["X"] = random.randint(1, 5)
                self.target_coordinates["Y"] = random.randint(1, 5)
                self.points += 50
                self.succesful_shoots += 1
                return True
            return False

    def info(self):
        total_shoots = 0
        for i in self.shoots_fired.values():
            total_shoots += i

        return f'Your Coordinates: {self.coordinates_dict},\nTarget Coordinates: {self.target_coordinates}\nTotal shoots: {total_shoots} {self.shoots_fired}, \nTotal score: {self.points}, \nSuccessful shoots: {self.succesful_shoots}'


tank = Tank()

while True:
    choice = int(input(
        "Choose\n1.Input move\n2.Info\n3.Shoot\n4.Quit"))
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
        print("-" * 30)
        print(tank.info())
        print("-" * 30)
    if choice == 3:
        tank.shoot()
        print("-" * 30)
        print("Boom!")
        if tank.shoot_result():
            print("Success!")
        else:
            print("Failed..")
        print("-" * 30)
    if choice == 4:
        print("-" * 30)
        print("End of game")
        print("-" * 30)
        break
    if choice == '':
        print("-" * 30)
        print("No choice made - program closed")
        print("-" * 30)
        break

