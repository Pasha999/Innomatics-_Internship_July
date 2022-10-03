# Task
# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
# Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

def is_leap(input_year):
    leap = False
    
    # Write your logic here 
    if (input_year % 4) == 0: 
        if (input_year % 100) == 0: 
            if (input_year % 400) == 0: 
                    return True
            else: 
                return False
        else: 
            return True
    else: 
        return False  
year = int(input())
print(is_leap(year))