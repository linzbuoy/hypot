import numpy as np
import hypot.pythag 

def test_add_nums():
    '''Tests the function that adds two numbers'''

    # Arrange
    test_variable_a = 3
    test_variable_b = 4
    expected_output = 7

    # Act
    output = hypot.pythag.add_nums(test_variable_a, test_variable_b)

    # Assert
    assert output == expected_output
    
    


    # No cleanup needed
    
def test_add_nums_arrays():
    '''Tests the function that adds two numbers'''

    # Arrange
    test_array_a = np.array([2, 5.7, 8])
    test_array_b = np.array([1.0, 1.0, 1.0])
    expected_output = np.array([3, 6.7, 9])

    # Act
    output = hypot.pythag.add_nums(test_array_a, test_array_b)

    # Assert
    assert np.allclose(expected_output, output)
    
    
def test_square_num():
    '''Tests the function that adds two numbers'''

    # Arrange
    test_var_1 = 7
    expected_output = 49

    # Act
    output = hypot.pythag.square_number(test_var_1)

    # Assert
    assert output == expected_output
    
def test_square_root():
    '''Tests the function that adds two numbers'''

    # Arrange
    test_var_1 = 16
    expected_output = 4

    # Act
    output = hypot.pythag.square_root(test_var_1)

    # Assert
    assert output == expected_output
    
def test_square_root_array():
    '''Tests the function that adds two numbers'''

    # Arrange
    test_var_2 = np.array([16, 49, 64])
    expected_output = np.array([4, 7, 8])

    # Act
    output = hypot.pythag.square_root(test_var_2)

    # Assert
    assert np.allclose(expected_output, output)
    
def test_square_root():
    '''Tests the function that adds two numbers'''

    # Arrange
    test_var_1 = 16
    expected_output = np.sqrt(16)

    # Act
    output = hypot.pythag.square_root(test_var_1)

    # Assert
    assert output == expected_output
    
def test_calc_hypot():
    test_var_1 = 5.6
    test_var_2 = 7.8
    expected_output = 9.6
    
    output = hypot.pythag.calc_hypot(test_var_1,test_var_2 )
    
    assert np.allclose(expected_output, output, atol=1e-2)
    
def test_calc_hypot():
    test_var_1 = np.array([10, 30045, 6.9, 0.04])
    test_var_2 = np.array([23, 2400, 8.9, 0.34])
    expected_output = np.array([25.08, 30140.7, 11.26, 0.34])
    
    output = hypot.pythag.calc_hypot(test_var_1, test_var_2)
    
    assert np.allclose(expected_output, output, rtol=1e-1)