from pandas import *
import numpy



    predictions = {}
    df = pandas.read_csv(file_path)
    for passenger_index, passenger in df.iterrows():
  
        passenger_id = passenger['PassengerId']
        if passenger['Sex'] == "female":
            predictions[passenger_id] = 1
        #if passenger['Pclass'] ==1 and passenger['Age'] <= 18:    
        #    predictions[passenger_id] = 1
        elif passenger['SibSp'] > 1 and passenger['Parch'] > 1:
            predictions[passenger_id] = 1
        else:
            predictions[passenger_id] = 0
    return predictions



#Add another comment

#Adding a comment


def numpy_dot():
    '''
    Imagine a point system in which each country is awarded 4 points for each
    gold medal,  2 points for each silver medal, and one point for each
    bronze medal.

    Using the numpy.dot function, create a new dataframe called
    'olympic_points_df' that includes:
        a) a column called 'country_name' with the country name
        b) a column called 'points' with the total number of points the country
           earned at the Sochi olympics.
    '''

    countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                 'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                 'Austria', 'France', 'Poland', 'China', 'Korea',
                 'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                 'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                 'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

    all_medals = [[13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],[11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0], [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]]

    points = [4,2,1]
    total_sc = numpy.dot(points,all_medals)

    d = {'country_name': Series(countries), 'points': Series(total_sc)}
    olympic_points_df = DataFrame(d)
    print olympic_points_df

    #return olympic_points_df

numpy_dot()





# a = [1,2,3,4,5]
# b = [2,3,4,5,6]
# print numpy.dot(a,b)


# def avg_medal_count():
#     '''
#     Compute the average number of bronze medals earned by countries who
#     earned at least one gold medal.
#
#     Save this to a variable named avg_bronze_at_least_one_gold.
#
#     HINT-1:
#     You can retrieve all of the values of a Pandas column from a
#     data frame, "df", as follows:
#     df['column_name']
#
#     HINT-2:
#     The numpy.mean function can accept as an argument a single
#     Pandas column.
#
#     For example, numpy.mean(df["col_name"]) would return the
#     mean of the values located in "col_name" of a dataframe df.
#     '''

    #
    # countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
    #              'Netherlands', 'Germany', 'Switzerland', 'Belarus',
    #              'Austria', 'France', 'Poland', 'China', 'Korea',
    #              'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
    #              'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
    #              'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']
    #
    # gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    # silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
    # bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]
    #
    # d = {'country_name': Series(countries), 'gold': Series(gold), 'silver': Series(silver), 'bronze': Series(bronze)}
    # df = DataFrame(d)

    #avg_bronze_at_least_one_gold = numpy.mean(df[df['gold'] >= 1]['bronze'])
    #print avg_bronze_at_least_one_gold


    #avg_medal_count = numpy.mean(df[['gold', 'silver','bronze']])
    #print avg_medal_count


#avg_medal_count()

#d = {'one': Series([1,2,3], index=['a','b','c']),
#      'two': Series([1,2,3,4], index=['a','b','c','d'])}
#
# df = DataFrame(d)
# #print df
# print df.apply(numpy.mean)
# print df['one'].map(lambda x: x>= 1)
# print df.applymap(lambda x: x>= 1)

# d = {"name": Series(["Braund", "Cummings", "Heikkinen", "Allen"], index=["a", "b", "c", "d"]),
#      'age': Series([22, 38, 26, 35], index=['a', 'b', 'c', 'd']),
#      'fare': Series([7.25, 71.83, 8.05], index=['a', 'b', 'd']),
#      'survived?': Series([False, True, True, False], index=['a', 'b', 'c', "d"])}
#
# df = DataFrame(d)
# #print df
# #print df[df['age'] >= 30]
# print df['survived?'][df['age'] >= 30]


#def create_dataframe():
#     '''
#     Create a pandas dataframe called 'olympic_medal_counts_df' containing
#     the data from the  table of 2014 Sochi winter olympics medal counts.
#
#     The columns for this dataframe should be called
#     'country_name', 'gold', 'silver', and 'bronze'.
#
#     There is no need to  specify row indexes for this dataframe
#     (in this case, the rows will  automatically be assigned numbered indexes).
#     '''
#
#     o = {'country_name': Series(['Russian Fed.', 'Norway', 'Canada', 'United States',
#          'Netherlands', 'Germany', 'Switzerland', 'Belarus', 'Austria', 'France', 'Poland', 'China', 'Korea',
#          'Sweden', 'Czech Republic', 'Slovenia', 'Japan', 'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
#          'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']),
#          'gold': Series([13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]),
#          'silver': Series([11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]),
#          'bronze': Series([9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1])}
#
#     df = DataFrame(o)
#     #print df
#
#     #print df['country_name']
#     #print df.loc[0]
#
# #create_dataframe()