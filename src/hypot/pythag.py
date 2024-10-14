# Module to calculate the hypotenuse of a right angle triangle

# Function to add numbers together
# input: floats or int or list/array of int/floats
def add_nums(a, b):
    """_summary_

    Args:
        a (float, int, array): A number to add
        b (float, int, array): A number to add

    Returns:
        float, int, array: The sum of a and b
    """
    sum_of_nums = a + b
    return sum_of_nums 


# Function to calculate the square of a number
# input: floats or int or list/array of int/floats
def square_number(a):
    """Return the square of a number

    Args:
        a (float, int, array): Number(s) to be squared

    Returns:
        float, int, array: squared number
    """
    squared = a**2
    return squared
# function to calc the square root of the number
# input: floats or int or list/array of int/floats

#function to calculate the hypotenuse using all of the above
 # a^2 + b^2 = c^2
 # c = sqrt(a^2 + b^2)
 # input: floats or int or list/array of int/floats
def square_root(a):
    sq_rt_num = a**0.5
    return sq_rt_num
     
def calc_hypot(opposite, adjacent):
    """_summary_

    Args:
        opposite (_type_): _description_
        adjacent (_type_): _description_

    Returns:
        _type_: _description_
    """
    opp_sqrd = square_number(opposite)
    adj_sqrd = square_number(adjacent)
    summed_nums = add_nums(opp_sqrd, adj_sqrd)
    hypotenuse = square_root(summed_nums)
    return hypotenuse

    