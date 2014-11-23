#import scipy.stats
#scipy.stats.ttest_ind(list_1, list_2, equal_var = False)
#indicates whether or not variance of two samples is equal
#returns tuple (t-value, p-value for two-tailed test )

import numpy
import scipy.stats
import pandas

def compare_averages(filename):
    """
    Performs a t-test on two sets of baseball data (left-handed and right-handed hitters).

    You will be given a csv file that has three columns.  A player's
    name, handedness (L for lefthanded or R for righthanded) and their
    career batting average (called 'avg'). You can look at the csv
    file via the following link:
    https://www.dropbox.com/s/xcn0u2uxm8c4n6l/baseball_data.csv
    
    Write a function that will read that the csv file into a pandas data frame,
    and run Welch's t-test on the two cohorts defined by handedness.
    
    One cohort should be a data frame of right-handed batters. And the other
    cohort should be a data frame of left-handed batters.
    
    We have included the scipy.stats library to help you write
    or implement Welch's t-test:
    http://docs.scipy.org/doc/scipy/reference/stats.html
    
    With a significance level of 95%, if there is no difference
    between the two cohorts, return a tuple consisting of
    True, and then the tuple returned by scipy.stats.ttest.  
    
    If there is a difference, return a tuple consisting of
    False, and then the tuple returned by scipy.stats.ttest.
    
    For example, the tuple that you return may look like:
    (True, (9.93570222, 0.000023))
    """
    
    #read the file
    data = pandas.read_csv(filename) 
    
    #spit data
    data_left = data[data['handedness'] == 'L']
    data_right = data[data['handedness'] == 'R']
    #run t-test
    t_result = scipy.stats.ttest_ind(data_left['avg'], data_right['avg'], equal_var = False)
    #Produce desired output
    if t_result[1] <= 0.05:
        return False, t_result
    else:
        return True, t_result
print compare_averages('baseball_data.csv')

u,p = scipy.stats.mannwhitneyu(x,y)
#Mann-Whitney u test, for not normal distributions
#returns u - mannwhitney test statistic and p - one sided p value

w,p =scipy.stats.shapiro(data)
#Shapiro-Wilk Test which let us define if distribution is normal
#data == array or list containing data points
#returns w - shapiro test statistic and p - one sided p value




import numpy
import pandas

def compute_cost(features, values, theta):
    """
    Compute the cost of a list of parameters, theta, given a list of features (input 
data points) and values (output data points).
    """
    m = len(values)
    sum_of_square_errors = numpy.square(numpy.dot(features, theta) - values).sum()
    cost = sum_of_square_errors / (2*m)

    return cost

def gradient_descent(features, values, theta, alpha, num_iterations):
    """
    Perform gradient descent given a data set with an arbitrary number of features.
    """

    # Write code here that performs num_iterations updates to the elements of theta.
    # times. Every time you compute the cost for a given list of thetas, append it 
    # to cost_history.
    m = len(values)
    cost_history = []
    for i in range(num_iterations):
        predicted_values = numpy.dot(features, theta)
        theta = theta - alpha/m *numpy.dot((predicted_values - values), features)
        cost = compute_cost(features, values, theta) 
        cost_history.append(cost)
    ###########################
    ### YOUR CODE GOES HERE ###
    ###########################

    return theta, pandas.Series(cost_history) # leave this line for the grader



