print("Welcome to the Chicken Squat Calculator! Based on the weights you enter, the calculator will determine how many chickens it would take to squat that weight!")

object_weight = input("How much does the object/person weight? (in pounds) ")
chicken_weight = input("How much do the chickens weight? (in pounds) ")

standard_chicken_weight = 5.0
standard_chicken_squat = 70.0

def calculator(object_weight, chicken_weight, standard_chicken_weight):
    chicken_variable = float(chicken_weight) / standard_chicken_weight 
    noname = chicken_variable * standard_chicken_squat
    max_chicken_squat = float(object_weight) / noname
    return max_chicken_squat

print("You need " + str(calculator(object_weight, chicken_weight, standard_chicken_weight)) + " chickens!")

print("DISCLAMER: According to a quick google search chickens can jump ~6 ft (1.83 m) (depending on size and breed). Assuming that a 2.27 kg (5 lb) chicken can jump six feet that would mean that the initial speed at lift off would have to be roughly 6 ms-1. (Using eq. 8 from this website). The average chicken is 0.4 m tall. Assuming its legs account for ~1/3 of its height, then it accelerates from 0 ms-1 to 6 ms-1 in ~0.13 m. That's an acceleration of 138 ms-2. Using F = ma, that's an exertion of 313 newton(N). If the acceleration due to gravity is taken to be 9.81 ms-2, then a 1 kg weight is exerting 9.81 N of force downward so to squat this you would need to exert > 9.81 N of force. Using this we can assume that the 5 lb chicken has a 1-RM squat of ~31/32 kg (68/70 lb).")