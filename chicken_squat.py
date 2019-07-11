print("Welcome to the Chicken Squat Calculator! Based on the weights you enter, the calculator will determine how many chickens it would take to squat that weight!")

object_weight = input("How much does the object/person weight? (in pounds) ")
chicken_weight = input("How much does the chicken weight? (in pounds) ")

standard_chicken_weight = 5
standard_chicken_squat = 70

def calculator(object_weight, chicken_weight, standard_chicken_weight):
    chicken_variable = chicken_weight / standard_chicken_weight 
    max_chicken_squat = object_weight / chicken_variable
    return max_chicken_squat
print(max_chicken_squat)