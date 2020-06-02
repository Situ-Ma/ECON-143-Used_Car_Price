import requests
import pandas as pd
import json
import os 

session = requests.Session()



# Mercedes-Benz C-Class 2010-2019 90025 Nationwide

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Referer': 'https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?sourceContext=forSaleTab_false_0&newSearchFromOverviewPage=true&inventorySearchWidgetType=AUTO&entitySelectingHelper.selectedEntity=c6079&entitySelectingHelper.selectedEntity2=c21239&zip=90025&distance=50000&searchChanged=true&modelChanged=true&filtersModified=true&sortType=undefined&sortDirection=undefined',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    }

post = {
    'zip':'90025',
    'address':'Los+Angeles,+CA',
    'latitude':'34.642601013183594',
    'longitude':'-118.5416030883789',
    'distance':'50000',
    'selectedEntity':'c6079',
    'entitySelectingHelper.selectedEntity2':'c21239',
    'transmission':'ANY',
    'page':'1',
    'displayFeaturedListings':'true',
    'inventorySearchWidgetType':'AUTO',
    'allYearsForTrimName':'false',
    'vatOnly':'false',
    'startYear':'2010',
    'endYear':'2019',
    'isRecentSearchView':'false',
    }

my_url = 'https://www.cargurus.com/Cars/inventorylisting/ajaxFetchSubsetInventoryListing.action?sourceContext=forSaleTab_false_0'

cars = session.post(my_url,headers=headers,data=post).text
cars = json.loads(cars)['listings']
columns = cars[0].keys()
rows = {column:[] for column in columns}

for car in cars:
    for column in columns:
        try:
            rows[column].append(car[column])
        except:
            rows[column].append('')
all_data = pd.DataFrame(rows)

# Mercedes-Benz E-Class 2010-2019 90025 Nationwide

post['selectedEntity'] = 'c6086'
post['entitySelectingHelper.selectedEntity2'] = 'c21242'

cars = session.post(my_url,headers=headers,data=post).text
cars = json.loads(cars)['listings']
rows = {column:[] for column in columns}

for car in cars:
    for column in columns:
        try:
            rows[column].append(car[column])
        except:
            rows[column].append('')

rows = pd.DataFrame(rows)
all_data = all_data.append(rows)

# Audi A4 2010-2019 90025 Nationwide
post['selectedEntity'] = 'c21846'
post['entitySelectingHelper.selectedEntity2'] = 'c28519'

cars = session.post(my_url,headers=headers,data=post).text
cars = json.loads(cars)['listings']
rows = {column:[] for column in columns}

for car in cars:
    for column in columns:
        try:
            rows[column].append(car[column])
        except:
            rows[column].append('')

rows = pd.DataFrame(rows)
all_data = all_data.append(rows)

# Audi Q5 2010-2019 90025 Nationwide
post['selectedEntity'] = 'c21829'
post['entitySelectingHelper.selectedEntity2'] = 'c28512'

cars = session.post(my_url,headers=headers,data=post).text
cars = json.loads(cars)['listings']
rows = {column:[] for column in columns}

for car in cars:
    for column in columns:
        try:
            rows[column].append(car[column])
        except:
            rows[column].append('')

rows = pd.DataFrame(rows)
all_data = all_data.append(rows)

# BWM 3-series 2010-2019 90025 Nationwide

post['selectedEntity'] = 'c23512'
post['entitySelectingHelper.selectedEntity2'] = 'c23970'
post['startYear']='2010'
post['endYear']='2019'

cars = session.post(my_url,headers=headers,data=post).text
cars = json.loads(cars)['listings']
rows = {column:[] for column in columns}

for car in cars:
    for column in columns:
        try:
            rows[column].append(car[column])
        except:
            rows[column].append('')
rows = pd.DataFrame(rows)
all_data = all_data.append(rows)

# BWM 4-series 2014-2019 90025 Nationwide

post['selectedEntity'] = 'c24128'
post['entitySelectingHelper.selectedEntity2'] = 'c27546'
post['startYear']='2014'
post['endYear']='2019'

cars = session.post(my_url,headers=headers,data=post).text
cars = json.loads(cars)['listings']
rows = {column:[] for column in columns}

for car in cars:
    for column in columns:
        try:
            rows[column].append(car[column])
        except:
            rows[column].append('')
rows = pd.DataFrame(rows)
all_data = all_data.append(rows)

# Mercedes-Benz A-Class 2019 90025 Nationwide

post['selectedEntity'] = 'c28505'
post['entitySelectingHelper.selectedEntity2'] = 'c28505'
post['startYear']='2019'
post['endYear']='2019'

cars = session.post(my_url,headers=headers,data=post).text
cars = json.loads(cars)['listings']
rows = {column:[] for column in columns}

for car in cars:
    for column in columns:
        try:
            rows[column].append(car[column])
        except:
            rows[column].append('')
rows = pd.DataFrame(rows)
all_data = all_data.append(rows)

# Audi A5 2010-2019 90025 Nationwide

post['selectedEntity'] = 'c21848'
post['entitySelectingHelper.selectedEntity2'] = 'c28571'
post['startYear']='2010'
post['endYear']='2019'

cars = session.post(my_url,headers=headers,data=post).text
cars = json.loads(cars)['listings']
rows = {column:[] for column in columns}

for car in cars:
    for column in columns:
        try:
            rows[column].append(car[column])
        except:
            rows[column].append('')
rows = pd.DataFrame(rows)
all_data = all_data.append(rows)

# Audi A6 2010-2019 90025 Nationwide

post['selectedEntity'] = 'c21860'
post['entitySelectingHelper.selectedEntity2'] = 'c27563'
post['startYear']='2010'
post['endYear']='2019'

cars = session.post(my_url,headers=headers,data=post).text
cars = json.loads(cars)['listings']
rows = {column:[] for column in columns}

for car in cars:
    for column in columns:
        try:
            rows[column].append(car[column])
        except:
            rows[column].append('')
rows = pd.DataFrame(rows)
all_data = all_data.append(rows)

# Mercedes-Benz GLE-Class 2016-2019 90025 Nationwide

post['selectedEntity'] = 'c24881'
post['entitySelectingHelper.selectedEntity2'] = 'c28347'
post['startYear']='2016'
post['endYear']='2019'

cars = session.post(my_url,headers=headers,data=post).text
cars = json.loads(cars)['listings']
rows = {column:[] for column in columns}

for car in cars:
    for column in columns:
        try:
            rows[column].append(car[column])
        except:
            rows[column].append('')
rows = pd.DataFrame(rows)
all_data = all_data.append(rows)

# Mercedes-Benz GLC-Class 2016-2019 90025 Nationwide

post['selectedEntity'] = 'c25330'
post['entitySelectingHelper.selectedEntity2'] = 'c28403'
post['startYear']='2016'
post['endYear']='2019'

cars = session.post(my_url,headers=headers,data=post).text
cars = json.loads(cars)['listings']
rows = {column:[] for column in columns}

for car in cars:
    for column in columns:
        try:
            rows[column].append(car[column])
        except:
            rows[column].append('')
rows = pd.DataFrame(rows)
all_data = all_data.append(rows)

# BMW X5 2010-2019 90025 Nationwide

post['selectedEntity'] = 'c21963'
post['entitySelectingHelper.selectedEntity2'] = 'c28154'
post['startYear']='2010'
post['endYear']='2019'

cars = session.post(my_url,headers=headers,data=post).text
cars = json.loads(cars)['listings']
rows = {column:[] for column in columns}

for car in cars:
    for column in columns:
        try:
            rows[column].append(car[column])
        except:
            rows[column].append('')
rows = pd.DataFrame(rows)
all_data = all_data.append(rows)

# Output data to CSV
all_data.to_csv('../data/used_car_data.csv')

# credit: https://github.com/cenalll/cargurus-web-scraper
