class car:
    def __init__(self, model,velocity,fulel_rate):
        self.model = model
        if velocity > 0 and velocity < 200 and fulel_rate > 0 and fulel_rate < 100:
            self.velocity = velocity
            self.fulel_rate = fulel_rate
        else:
            raise ValueError("Invalid velocity or fuel rate")
        
    def set_owner(self, owner):
        self.owner = owner
        self.owner.car = self  # Set the car for the owner
        print(f"Car {self.model} is now owned by {owner.name}.\n")
    def __str__(self):
        return f"Car Model: {self.model}, Velocity: {self.velocity} km/h, Fuel Rate: {self.fulel_rate} L/100km, Owner: {self.owner.name if self.owner else 'No owner'}"
    