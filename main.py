from employee import employee
from office import office
from car import car

def main():
    iti = office("ITI")  
    Samy=employee('123',"Samy",iti,20)

    samy_car = car("Fiat 128", 120, 50)
    samy_car.set_owner(Samy)

    print(f"samy takes {Samy.calculate_time_to_work():.2f} hours to reach work")

if __name__ == "__main__":
    main()