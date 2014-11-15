import pandas
baseball_data = pandas.read_csv('Master.csv')
print baseball_data['nameFirst']
baseball_data['height_plus_weight'] = baseball_data['height'] + baseball_data['weight']
baseball_data.to_csv('baseball_data_with_weight_hight.csv')
#we create a new file 'baseball_data_with_weight_hight.csv'


