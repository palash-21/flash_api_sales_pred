import requests, json

url = 'http://0.0.0.0:5000/api/'

data = {'CompetitionAge': [82.0, 92.0, 103.0], 'CompetitionAge_logt': [1.919078092376074, 1.968482948553935, 2.0170333392987803],
 'CompetitionDistance': [1270.0, 570.0, 14130.0], 'CompetitionDistance_logt': [3.104145550554008, 2.756636108245848, 4.150172896393132],
 'Date': [Timestamp('2015-07-31 00:00:00'), Timestamp('2015-07-31 00:00:00'), Timestamp('2015-07-31 00:00:00')],
 'Day': [31, 31, 31],
 'DayOfWeek': [5, 5, 5],
 'Day_Avg_Cust': [460, 401, 617],
 'Month': [7, 7, 7],
 'Month_Avg_Cust': [463, 559, 654],
 'Open': [1, 1, 1],
 'Promo': [1, 1, 1],
 'Promo2': [0, 1, 1],
 'Promo2New': [0, 1, 1],
 'Sales': [5263, 6064, 8314],
 'Sales_logt': [3.721315880605899, 3.782830805202592, 3.919862253555538],
 'SchoolHoliday': [1, 1, 1],
 'Store': [1, 2, 3],
 'Week_Day_Avg_Cust': [539, 534, 748],
 'Year': [2015, 2015, 2015],
 'assort_a': [1, 1, 1],
 'assort_b': [0, 0, 0],
 'assort_c': [0, 0, 0],
 'holy_0': [1, 1, 1],
 'holy_a': [0, 0, 0],
 'holy_b': [0, 0, 0],
 'holy_c': [0, 0, 0],
 'type_a': [0, 1, 1],
 'type_b': [0, 0, 0],
 'type_c': [1, 0, 0],
 'type_d': [0, 0, 0]}

j_data = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
print(r,r.text)