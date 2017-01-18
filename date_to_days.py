import pandas as pd
from datetime import datetime
    


class DateToDays(object):

    def __init__(self, data):

        self.data = data

        i = 0

        data['d'] = 0

        for i in range(len(data['date'])):

            data['d'][i] = datetime.strptime(data['date'][i], '%d/%m/%Y')

        print data['d'][len(data['d'])-1]

        data['day'] = 0

        i = 0

        for i in range(len(data['date'])-1):

            data['day'][i] = (data['d'][i] - data['d'][len(data['d'])-1]).days


        data.to_csv('/home/metalm/Desktop/udacity/petr4/new_csv_date_day.csv', sep=',')
