print("Welcome to the Chicken Fitness Calculator! Based on the weights you enter, the calculator will determine how many chickens it would take to squat and pull that weight!")

option = input("Which calculator you want to use? ")


standard_chicken_weight = 5.0
standard_chicken_squat = 70.0
standard_chicken_cost = 20.0

def cost(standard_chicken_cost, chicken_amount):
    total = standard_chicken_cost * chicken_amount
    return total

if option.lower() == "squat":
    object_weight = input("How much does the object/person weight? (in pounds) ")
    chicken_weight = input("How much do the chickens weight? (in pounds)(average chicken is five pounds)(Average chicken is 5 pounds and the biggest chicken ever was 16 pounds) ")
    def squat_calculator(object_weight, chicken_weight, standard_chicken_weight):
        chicken_variable = float(chicken_weight) / standard_chicken_weight 
        noname = chicken_variable * standard_chicken_squat
        max_chicken_squat = float(object_weight) / noname
        return max_chicken_squat
    squat_chicken_count = squat_calculator(object_weight, chicken_weight, standard_chicken_weight)
    print("You need " + str(squat_chicken_count) + " chickens to squat the object!")
    print("It would cost on average $" + str(cost(standard_chicken_cost, squat_chicken_count)))

elif option.lower() == "pull":
    object_weight = input("How much does the object/person weight? (in pounds) ")
    chicken_weight = input("How much do the chickens weight? (in pounds)(Average chicken is 5 pounds and the biggest chicken ever was 16 pounds) ")
    standard_chicken_pull = 2.0513
    def pull_calculator(standard_chicken_weight,standard_chicken_pull):
        chicken_pull_variable = float(chicken_weight) / standard_chicken_weight
        noname_2 = standard_chicken_pull * chicken_pull_variable
        max_chicken_pull = float(object_weight) / noname_2
        return max_chicken_pull
    pull_chicken_count = pull_calculator(standard_chicken_weight,standard_chicken_pull)
    print("You need " + str(pull_chicken_count) + " chickens to pull the object!")
    print("It would cost $" + str(cost(standard_chicken_cost, pull_chicken_count)))
    
