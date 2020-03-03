import requests
import pandas as pd
import math
import sys



def task(url):
    
    def parcing(string):
        if string[21:25] == 'true':
            return True
        elif string[21:26] == 'false':
            return False
        else:
            return 'geo_type'


    r = requests.get(url)

    df = pd.DataFrame(r.text.split('\n'))
    df.drop(df.tail(1).index,inplace=True)
    df['switch'] = df.apply(lambda x: parcing(x[0]), axis =  1)
    df['time'] = df.apply(lambda x: int(x[0][-20:-1]), axis =  1)
    df = df.sort_values(['time'])

    
    switch_on_road = []
    switch_off_road = []
    switch = False
    list_of_ways = []

    for index, row in df.iterrows():

        if row['switch'] != switch:
            if not row['switch'] == 'geo_type':   
                if switch == False:
                    switch_off_road.append(list_of_ways)
                    list_of_ways = []
                else:
                    switch_on_road.append(list_of_ways)
                    list_of_ways = []
                switch = not switch


        if row['switch'] == 'geo_type':
            list_of_ways.append(row[0])

    def sum_length(list_of_lists):
        return_sum = 0
        for each in list_of_lists:

            if each:
                prev_lat = float(each[0].replace(',', ':').replace('}', ':').split(':')[2])
                prev_lon = float(each[0].replace(',', ':').replace('}', ':').split(':')[4])

                for geo_data in each[1::]:
                    lat = float(geo_data.replace(',', ':').replace('}', ':').split(':')[2])
                    lon = float(geo_data.replace(',', ':').replace('}', ':').split(':')[4])			
                    way = math.sqrt((lat - prev_lat)**2 + (lon - prev_lon)**2)
                    return_sum += way
        return return_sum
    
    print("Autopilot is on: " + str(sum_length(switch_on_road)) + '.')
    print("Autopilot is off: " + str(sum_length(switch_off_road)) + '.')


task(sys.argv[1])
