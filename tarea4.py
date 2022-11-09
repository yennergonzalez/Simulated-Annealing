# imports

import random


# - - - - - - - - - - - - - - DEFINE CONSTANTS - - - - - - - - - - - - - -
# function domain
func_domain = [0,20]

# initial solutions
x1_solution = 7
x2_solution = 17

# initial temperature
curr_temp = 100

# improvement threshold required to keep iterating
improvement_threshold = 0.000001

# boolean variable to determine if new x values improved the solutions and should be kept or not
improved = True

# count consecutive non-improving iterations - if counter == 100 execution stops
counter = 0

# improvement achieved on the current iteration
iteration_improvement = 0

# evaluate the function
def EvalFunction (x1, x2):
    result = x1*(x1-5)+(x2**3)-x1*(x2+11)
    return result

# program keeps running while switches improve the result or during 99 consecutive non-improving iterations 
while ((((counter < 100) and (improved == False)) or (improved == True))):
    # evaluate current result
    current_result = EvalFunction(x1_solution, x2_solution)
    
    # get random increment (-0.1, +0.1) for x1,x2
    rand_x1_increment = 0.2*random.random()-0.1
    rand_x2_increment = 0.2*random.random()-0.1
    
    # evaluate new result
    new_result = EvalFunction(x1_solution+rand_x1_increment, x2_solution+rand_x2_increment)

    # if the new result improves it is kept  
    if (new_result + improvement_threshold < current_result):
        x1_solution = x1_solution+rand_x1_increment
        x2_solution = x2_solution+rand_x2_increment

        # if the new solutions exceed the domain limits they are forced to 0 or 20
        if x1_solution < 0:
            x1_solution = 0

        if x2_solution < 0:
            x2_solution = 0

        if x1_solution > 20:
            x1_solution = 20
        
        if x2_solution > 20:
            x2_solution = 20

        # boolean variable set as true since the change improved the previous result
        improved = True
        
        # non-improving iterations reset to zero
        counter = 0

    else:
        # non-improving iterations incremented by one
        counter = counter + 1
        
        # boolean variable set as false since the change did not improve the previous result
        improved = False

        # Evaluate if the change is kept even if it did not improve the result 
        
        # random temperature value to act as threshold with respect to current temperature  
        rand_temp = random.random()*100
        
        # compare random temperature with current temperature - if current temperature is greater, accept the change
        if (rand_temp < curr_temp):
            x1_solution = x1_solution+rand_x1_increment
            x2_solution = x2_solution+rand_x2_increment

            # if the new solutions exceed the domain limits they are forced to 0 or 20
            if x1_solution < 0:
                x1_solution = 0

            if x2_solution < 0:
                x2_solution = 0

            if x1_solution > 20:
                x1_solution = 20
            
            if x2_solution > 20:
                x2_solution = 20

            # evaluate new result
            new_result = EvalFunction(x1_solution, x2_solution)
        
        # if current temperature is lower and the temperature comparation is also lower, the change is not accepted
        else:
            pass
        
        # scale the current temperature by 0.99
        curr_temp = curr_temp*0.99

    # print the results
    print("\nCurrent result:  %f \n" %current_result)
    print("x1:              %f \n" %x1_solution)
    print("Δx1              %f \n" %rand_x1_increment)
    print("x2:              %f \n" %x2_solution)
    print("Δx2              %f \n" %rand_x2_increment)
    print("counter:         %d \n" %counter)
    print("Temperature:     %f \n" %curr_temp)
    print("----------------------------")
