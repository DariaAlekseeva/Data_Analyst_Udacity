from pandas import *
from ggplot import *

import pandas

def lineplot(hr_year_csv):
    # A csv file will be passed in as an argument which
    # contains two columns -- 'HR' (the number of homerun hits)
    # and 'yearID' (the year in which the homeruns were hit).
    #
    # Fill out the body of this function, lineplot, to use the
    # passed-in csv file, hr_year.csv, and create a
    # chart with points connected by lines, both colored 'red',
    # showing the number of HR by year.
    #
    # You will want to first load the csv file into a pandas dataframe
    # and use the pandas dataframe along with ggplot to create your visualization
    #
    # You can check out the data in the csv file at the link below:
    # https://www.dropbox.com/s/awgdal71hc1u06d/hr_year.csv
    #
    # You can read more about ggplot at the following link:
    # https://github.com/yhat/ggplot/
    
    data = read_csv(hr_year_csv)
    df = DataFrame(data)
    gg = ggplot(data, aes('HR','yearID')) + geom_point(color = 'red') + geom_line(color = 'red') + ggtitle('Number of HR by year') + xlab('HR') + ylab('yearID')
    return gg






from pandas import *
from ggplot import *

import pandas

def lineplot_compare(hr_by_team_year_sf_la_csv):
    # Write a function, lineplot_compare, that will read a csv file
    # called hr_by_team_year_sf_la.csv and plot it using pandas and ggplot2.
    #
    # This csv file has three columns: yearID, HR, and teamID. The data in the
    # file gives the total number of home runs hit each year by the SF Giants 
    # (teamID == 'SFN') and the LA Dodgers (teamID == "LAN"). Produce a 
    # visualization comparing the total home runs by year of the two teams. 
    # 
    # You can see the data in hr_by_team_year_sf_la_csv
    # at the link below:
    # https://www.dropbox.com/s/wn43cngo2wdle2b/hr_by_team_year_sf_la.csv
    #
    # Note that to differentiate between multiple categories on the 
    # same plot in ggplot, we can pass color in with the other arguments
    # to aes, rather than in our geometry functions. For example, 
    # ggplot(data, aes(xvar, yvar, color=category_var)). This should help you 
    # in this exercise.
    data = read_csv(hr_by_team_year_sf_la_csv)
    df = DataFrame(data)
    gg = ggplot(df, aes('HR','yearID',color='teamID')) + geom_point() + geom_line() + ggtitle('Number of HR by year') + xlab('HR') + ylab('yearID')


    return gg




from pandas import *
from ggplot import *

def plot_weather_data(turnstile_weather):
    ''' 
    plot_weather_data is passed a dataframe called turnstile_weather. 
    Use turnstile_weather along with ggplot to make another data visualization
    focused on the MTA and weather data we used in Project 3.
    
    Make a type of visualization different than what you did in the previous exercise.
    Try to use the data in a different way (e.g., if you made a lineplot concerning 
    ridership and time of day in exercise #1, maybe look at weather and try to make a 
    histogram in this exercise). Or try to use multiple encodings in your graph if 
    you didn't in the previous exercise.
    
    You should feel free to implement something that we discussed in class 
    (e.g., scatterplots, line plots, or histograms) or attempt to implement
    something more advanced if you'd like.

    Here are some suggestions for things to investigate and illustrate:
     * Ridership by time-of-day or day-of-week
     * How ridership varies by subway station
     * Which stations have more exits or entries at different times of day

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/
     
    You can check out the link 
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
    to see all the columns and data points included in the turnstile_weather 
    dataframe.
     
    However, due to the limitation of our Amazon EC2 server, we will give you only 
    about 1/3 of the actual data in the turnstile_weather dataframe.
    '''

    turnstile_weather = turnstile_weather[["ENTRIESn_hourly"]].groupby(turnstile_weather['UNIT']).mean()
    turnstile_weather=turnstile_weather.reset_index()
    
    by_num_of_ent = turnstile_weather.sort(["ENTRIESn_hourly", "UNIT"], ascending=False)
    by_num_of_ent=by_num_of_ent.head(15)
    by_num_of_ent=by_num_of_ent.reset_index()
    plot = ggplot(by_num_of_ent, aes('UNIT', 'ENTRIESn_hourly')) + geom_bar(aes(weight='ENTRIESn_hourly'),fill='blue',stat = 'identity') + ggtitle('How ridership varies by subway station') + xlab('Station') + ylab('Entries')
    return plot






from pandas import *
from ggplot import *

def plot_weather_data(turnstile_weather):
    '''
    You are passed in a dataframe called turnstile_weather. 
    Use turnstile_weather along with ggplot to make a data visualization
    focused on the MTA and weather data we used in assignment #3.  
    You should feel free to implement something that we discussed in class 
    (e.g., scatterplots, line plots, or histograms) or attempt to implement
    something more advanced if you'd like.  

    Here are some suggestions for things to investigate and illustrate:
     * Ridership by time of day or day of week
     * How ridership varies based on Subway station
     * Which stations have more exits or entries at different times of day

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/
     
    You can check out:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
     
    To see all the columns and data points included in the turnstile_weather 
    dataframe. 
     
    However, due to the limitation of our Amazon EC2 server, we are giving you about 1/3
    of the actual data in the turnstile_weather dataframe
    '''
    
    
    import datetime
    
    turnstile_weather = turnstile_weather.copy()
    
    f = '%Y-%m-%d'
    turnstile_weather['DATEn'] = turnstile_weather['DATEn'].apply(lambda x: datetime.datetime.strptime(x, f))
    turnstile_weather['index'] = turnstile_weather['DATEn'].dt.dayofweek
    turnstile_weather['DATEn'] = turnstile_weather['DATEn'].apply(lambda x: x.strftime('%A'))
    days_df = turnstile_weather[['DATEn','ENTRIESn_hourly','index']].groupby('DATEn', as_index=False).mean()
    by_ent = days_df.sort(['index',"ENTRIESn_hourly","DATEn"], ascending=True)
    plot = ggplot(by_ent, aes(x='DATEn', y='ENTRIESn_hourly')) + geom_bar(aes(weight='ENTRIESn_hourly'),fill='blue',stat = 'identity') + xlab('Day of week') +ylab('Entries per day') + ggtitle("Ridership by day of week")
    return plot







