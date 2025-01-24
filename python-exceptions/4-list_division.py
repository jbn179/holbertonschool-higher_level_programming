#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    Divide elements of two lists element by element.

    Parameters:
    my_list_1 (list): The first list of numbers (numerators).
    my_list_2 (list): The second list of numbers (denominators).
    list_length (int): The number of elements to divide.

    Returns:
    list: A new list containing the results of the division. If an error occurs, the result is 0.
    """
    new_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)
    return new_list
