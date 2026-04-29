import math

class Car:
    def __init__(self, manufacturer, model, unique_id, speed, x, y, events):
        self.manufacturer = manufacturer
        self.model = model
        self.unique_id = unique_id
        self.speed = speed
        self.x = x 
        self.y = y
        self.events = events
        self.received_information = []

    def display_info(self):
        print(f"Manufacturer:{self.manufacturer},\n Model:{self.model},\n ID:{self.unique_id},\n Speed:{self.speed},\n Location: ({self.x},{self.y}),\n Events:{self.events}\n")

    def set_current_speed(self, new_speed): 
        if new_speed < 0: 
            raise ValueError("Speed needs to be a positive number")
        self.speed = new_speed

    def calculate_distance(self, other_car):
        dx = other_car.x - self.x
        dy = other_car.y - self.y 
        distance = math.sqrt(dx ** 2 + dy ** 2)
        return distance

    def receive_information(self, other_car):
        self.received_information.append(other_car)

    def send_information(self, other_car):
        other_car.receive_information(self)

    def display_received_information(self):
        if not self.received_information:
            print(f"{self.manufacturer} hasn't received information.")
        
        else: 
            print(f"Information received by {self.manufacturer}")
            for car in self.received_information:
                print(f"Manufacturer:{car.manufacturer},\n Model:{car.model},\n ID:{car.unique_id},\n Speed:{car.speed},\n Location: ({car.x},{car.y}),\n Events:{car.events}\n")

    def pick_closest_car(self):
        if not self.received_information:
            return None
        closest_car = self.received_information[0]
        shortest_distance = self.calculate_distance(closest_car)

        for car in self.received_information:
            distance = self.calculate_distance(car)

            if distance < shortest_distance:
                closest_car = car 
                shortest_distance = distance 

        return closest_car
    
# Main function for testing the Car class and it's methods
    
if __name__ == "__main__":
    car1 = Car("Subaru", "Legacy", "CAR1", 50, 30, 40, ["accident"])
    car2 = Car("BMW", "M3", "CAR2", 90, 25, 35, ["icy road"] )
    car3 = Car("Mazda", "Miata", "CAR3", 80, 60, 70, ["closed road"])

    car1.display_info()

    car1.set_current_speed(100)
    car1.display_info()

    print(f"Distance from car1 to car2: {car1.calculate_distance(car2)}")
    print(f"Distance from car1 to car3: {car1.calculate_distance(car3)}")

    car2.send_information(car1) 
    car3.send_information(car1)

    car1.display_received_information()

    closest_car = car1.pick_closest_car()
    print(f"Closest car: {closest_car.manufacturer} {closest_car.model}, distance: {car1.calculate_distance(closest_car)}")

