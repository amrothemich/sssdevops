"""
Main python file for the sssdevops example
"""

#import statements go here


def mean(num_lst):
    """
	Calculates the mean of a list of numbers

	Parameters
	----------
	num_list : list
	List of numbers to calculate the average of
	
	Returns
	-------
	The average/mean of num_lst
	"""
    Sum = sum(num_lst)
    count = 0

    for num in num_lst:
        count += 1

    return Sum / count
