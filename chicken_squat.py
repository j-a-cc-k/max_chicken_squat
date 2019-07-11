print("Welcome to the Chicken Fitness Calculator! Based on the weights you enter, the calculator will determine how many chickens it would take to squat and pull that weight!")

object_weight = input("How much does the object/person weight? (in pounds) ")
chicken_weight = input("How much do the chickens weight? (in pounds) ")

standard_chicken_weight = 5.0
standard_chicken_squat = 70.0

def squat_calculator(object_weight, chicken_weight, standard_chicken_weight):
    chicken_variable = float(chicken_weight) / standard_chicken_weight 
    noname = chicken_variable * standard_chicken_squat
    max_chicken_squat = float(object_weight) / noname
    return max_chicken_squat

print("You need " + str(squat_calculator(object_weight, chicken_weight, standard_chicken_weight)) + " chickens to squat the object!")

standard_chicken_pull = 2.0513
def pull_calculator(standard_chicken_weight,standard_chicken_pull):
    chicken_pull_variable = float(chicken_weight) / standard_chicken_weight
    noname_2 = standard_chicken_pull * chicken_pull_variable
    max_chicken_pull = float(object_weight) / noname_2
    return max_chicken_pull
    
print("You need " + str(pull_calculator(standard_chicken_weight,standard_chicken_pull)) + " chickens to pull the object!")
    
    
    
    
    
    
