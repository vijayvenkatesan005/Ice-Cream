#Vijay Venkatesan
#This program simulates an ice cream shop where scoops of ice cream
# are served to the customer until they are finished
#11/26/2022

import IceCreamShoppe
import Scoop

def main():
    scooper_1_radius = float(input("What is the radius of your first scooper? "))
    scooper_2_radius = float(input("What is the radius of your second scooper? "))

    carton_radius = float(input("What is the radius of your carton? "))
    carton_height = float(input("What is the height of your carton? "))

    scoop1 = Scoop.Scoop(scooper_1_radius)
    scoop2 = Scoop.Scoop(scooper_2_radius)

    shoppe1 = IceCreamShoppe.IceCreamShoppe(carton_radius, carton_height)

    shoppe1.serve(1, scoop1)
    shoppe1.serve(1, scoop2)

    more_ice_cream = int(input("Would you like more ice cream? "))

    while more_ice_cream != 0:

        number_first_scooper_radius_scoops = int(input("How many " + str(scooper_1_radius) + " scoops would you like? "))
        number_second_scooper_radius_scoops = int(input("How many " + str(scooper_2_radius) + " scoops would you like? "))

        shoppe1.serve(number_first_scooper_radius_scoops, scoop1)
        shoppe1.serve(number_second_scooper_radius_scoops, scoop2)

        more_ice_cream = int(input("Would you like more ice cream? "))
    
    if shoppe1.cartonsUsed() == 1:
        print("You used " + str(shoppe1.cartonsUsed()) + " carton of ice cream")
    
    else:
        print("You used " + str(shoppe1.cartonsUsed()) + " cartons of ice cream")
        
        
if __name__ == "__main__":
    main()