class person:
    def __init__(self, name):
        self.name = name
    
class employee(person):
    car = None  # Class variable to hold the car object
    def __init__(self,id, name,works_at,distance_to_work):
        super().__init__(name)
        self.id = id
        self.distance_to_work = distance_to_work
        self.works_at = works_at
        self.works_at.add_employee(self)  # Automatically add employee to office
    def calculate_time_to_work(self):
        if self.car is None:
            raise ValueError("Employee does not have a car.")
        time = self.distance_to_work / self.car.velocity  
        return time
    def __buy_car(self, car):
        self.car = car
        car.set_owner(self)
        print(f"{self.name} bought a {car.model}.")
    def __get_car(self):
        return self.car
    def __str__(self):
        return f"Employee Name: {self.name}, Works at: {self.works_at.name}"



