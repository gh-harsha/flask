# -*- coding: utf-8 -*-
"""CA1_20043367.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10t0ZwD1LCy90Va5w_30KCDN-ZAoknhMU
"""

import pandas as pd
import json

"""Website used to Web scraping: https://www.magicbricks.com/"""

#Since only 30 rows are being displayed, I am fetching data from two URLs on the same website.

# import requests

# url = "https://www.magicbricks.com/mbsrp/propertySearch.html?editSearch=Y&category=S&propertyType=10002,10003,10021,10022,10001,10017&bedrooms=11701,11702&city=2624&page=page&&sortBy=premiumRecent&postedSince=-1&pType=10002,10003,10021,10022,10001,10017&isNRI=Y&multiLang=en"

# headers = {
#   "Accept": "application/json, text/plain, */*",
#   "Accept-Encoding": "gzip, deflate",
#   "Accept-Language": "en-US,en;q=0.9,kn-IN;q=0.8,kn;q=0.7",
#   "Cookie": "trackerCookie=Google_Organic; firstInteractionCookie=P; paidInteractionCookie=Y; cookieDtfirstIntr=20241121; HDSESSIONID=41e3df10-0ea8-4ec4-ae48-f5adbea6cee4; JSESSIONID=02D641C2756A6BFD1197BE5E3995EE47-n2.32210; _clck=7jy7lb%7C2%7Cfr1%7C0%7C1785; userNTrackId=41650aa7-f62b-4bf2-82d5-c7328ae1ea96; NOEU=new; previousTab=tabBUY; semAttributesCookie=Seo%23; _gcl_au=1.1.498083650.1732138162; alertRaisedCount=1; _gid=GA1.2.1832576979.1732138162; _gat_UA-492553-10=1; luxuryCookie=N; projectCategory=B; subPropertyTypeCookie=10002%2C10003%2C10021%2C10022%2C10001%2C10017; subPropertyType=Multistorey-Apartment%2CBuilder-Floor-Apartment%2CPenthouse%2CStudio-Apartment%2CResidential-House%2CVilla; propertyTypeCookie=Multistorey-Apartment%2CBuilder-Floor-Apartment%2CPenthouse%2CStudio-Apartment%2CResidential-House%2CVilla; cityCookie=2624; cityCode=2624; propCategory=Residential; SRPSESSIONID=ZmJlZmY5ZDMtYWE0Ny00YmFlLWE2NzMtZTQ5MjY5OWYyY2Fh; VerifiedInfoCardShown=Y; psmIds=; mbRecommendationCookies=pageType%3Dproperty%7ClistType%3DS%7CpropType%3D10002%2C10003%2C10021%2C10022%2C10001%2C10017%7Cbedrooms%3D11701%2C11702%7Ccity%3D2624%7CcompleteCityCode%3D2624; _ga=GA1.2.583839844.1732138162; _clsk=ii0g60%7C1732138168237%7C2%7C1%7Cv.clarity.ms%2Fcollect; SS_RMB=; mbcc=Y; _gali=mb-consent-cookie; _ga_Y3D9LD1B01=GS1.1.1732138161.1.1.1732138178.43.0.0; uniqUserSearchId=b5027f8d542248af81751f35c9c9e409fbeff9d3_1732138182833",
#   "Priority": "u=1, i",
#   "Referer": "https://www.magicbricks.com/property-for-sale/residential-real-estate?bedroom=2,3&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&cityName=New-Delhi",
#   "Sec-CH-UA": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
#   "Sec-CH-UA-Mobile": "?0",
#   "Sec-CH-UA-Platform": "\"Windows\"",
#   "Sec-Fetch-Dest": "empty",
#   "Sec-Fetch-Mode": "cors",
#   "Sec-Fetch-Site": "same-origin",
#   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
# }

import requests
#url_1 = "https://www.magicbricks.com/mbsrp/propertySearch.html?editSearch=Y&category=S&propertyType=10002,10003,10021,10022,10001,10017&bedrooms=11701,11702&city=2624&page=1&&sortBy=premiumRecent&postedSince=-1&pType=10002,10003,10021,10022,10001,10017&isNRI=Y&multiLang=en"
#url_2 = "https://www.magicbricks.com/mbsrp/propertySearch.html?editSearch=Y&category=S&propertyType=10002,10003,10021,10022,10001,10017&bedrooms=11701,11702&city=2624&page=2&&sortBy=premiumRecent&postedSince=-1&pType=10002,10003,10021,10022,10001,10017&isNRI=Y&multiLang=en"
#url_3 = "https://www.magicbricks.com/mbsrp/propertySearch.html?editSearch=Y&category=S&propertyType=10002,10003,10021,10022,10001,10017&bedrooms=11701,11702&city=2624&page=3&&sortBy=premiumRecent&postedSince=-1&pType=10002,10003,10021,10022,10001,10017&isNRI=Y&multiLang=en"
url = "https://www.magicbricks.com/mbsrp/propertySearch.html?editSearch=Y&category=S&propertyType=10002,10003,10021,10022,10001,10017&bedrooms=11701,11702&city=2624&page={}&&sortBy=premiumRecent&postedSince=-1&pType=10002,10003,10021,10022,10001,10017&isNRI=Y&multiLang=en"

headers = {
  "Accept": "application/json, text/plain, */*",
  "Accept-Encoding": "gzip, deflate",
  "Accept-Language": "en-US,en;q=0.9,kn-IN;q=0.8,kn;q=0.7",
  "Cookie": "trackerCookie=Google_Organic; firstInteractionCookie=P; paidInteractionCookie=Y; cookieDtfirstIntr=20241121; HDSESSIONID=41e3df10-0ea8-4ec4-ae48-f5adbea6cee4; JSESSIONID=02D641C2756A6BFD1197BE5E3995EE47-n2.32210; _clck=7jy7lb%7C2%7Cfr1%7C0%7C1785; userNTrackId=41650aa7-f62b-4bf2-82d5-c7328ae1ea96; NOEU=new; previousTab=tabBUY; semAttributesCookie=Seo%23; _gcl_au=1.1.498083650.1732138162; alertRaisedCount=1; _gid=GA1.2.1832576979.1732138162; _gat_UA-492553-10=1; luxuryCookie=N; projectCategory=B; subPropertyTypeCookie=10002%2C10003%2C10021%2C10022%2C10001%2C10017; subPropertyType=Multistorey-Apartment%2CBuilder-Floor-Apartment%2CPenthouse%2CStudio-Apartment%2CResidential-House%2CVilla; propertyTypeCookie=Multistorey-Apartment%2CBuilder-Floor-Apartment%2CPenthouse%2CStudio-Apartment%2CResidential-House%2CVilla; cityCookie=2624; cityCode=2624; propCategory=Residential; SRPSESSIONID=ZmJlZmY5ZDMtYWE0Ny00YmFlLWE2NzMtZTQ5MjY5OWYyY2Fh; VerifiedInfoCardShown=Y; psmIds=; mbRecommendationCookies=pageType%3Dproperty%7ClistType%3DS%7CpropType%3D10002%2C10003%2C10021%2C10022%2C10001%2C10017%7Cbedrooms%3D11701%2C11702%7Ccity%3D2624%7CcompleteCityCode%3D2624; _ga=GA1.2.583839844.1732138162; _clsk=ii0g60%7C1732138168237%7C2%7C1%7Cv.clarity.ms%2Fcollect; SS_RMB=; mbcc=Y; _gali=mb-consent-cookie; _ga_Y3D9LD1B01=GS1.1.1732138161.1.1.1732138178.43.0.0; uniqUserSearchId=b5027f8d542248af81751f35c9c9e409fbeff9d3_1732138182833",
  "Priority": "u=1, i",
  "Referer": "https://www.magicbricks.com/property-for-sale/residential-real-estate?bedroom=2,3&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&cityName=New-Delhi",
  "Sec-CH-UA": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
  "Sec-CH-UA-Mobile": "?0",
  "Sec-CH-UA-Platform": "\"Windows\"",
  "Sec-Fetch-Dest": "empty",
  "Sec-Fetch-Mode": "cors",
  "Sec-Fetch-Site": "same-origin",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}

# response_1 = requests.get(url.format(1), headers=headers)
# response_1
# response_2 = requests.get(url_2, headers=headers)
# response_2
# response_3 = requests.get(url_3, headers=headers)
# response_3

# Using For loop to fetch data from the multiple pages

responses= [requests.get(url.format(i), headers=headers) for i in range (1,11)]
responses

# data1 = response_1.json()
# print(data1)
# data2 = response_2.json()
# print(data2)
# data3 = response_3.json()
# print(data3)

data = [i.json() for i in responses]
print(data)

# data1.keys()
# data2.keys()
# data3.keys()

print(data[0].keys())

"""Displaying the information present in  the resultlist keys"""

# merge_data = data1['resultList'] + data2['resultList'] + data3['resultList']
Actual_data = [i['resultList'] for i in data]
print(Actual_data)
# df = pd.DataFrame(merge_data)
# df.shape
# df = pd.json_normalize(merge_data)

dfs = [pd.json_normalize(i) for i in Actual_data]
df = pd.concat(dfs, ignore_index=True)
df.shape

"""Finding the Null values in the Column"""

df.isna().sum()

"""Displaying the data frame to see the column data for analysis"""

df

"""Displaying the total column name in the Data Frame"""

column_name = df.columns.to_list()
print(column_name)

"""After analyzing the data frame, there are 323 columns among them most important Property details columns("propTypeD","bedroomD","bathD","floorD", "priceD","OwnershipTypeD","furnishedD")"""

prop_details = ["propTypeD","bedroomD","bathD","floorD", "priceD","OwnershipTypeD","furnishedD"]
prop_details = df[prop_details]
print(prop_details.head())

"""Changing the "propTypeD","bedroomD","bathD","floorD", "priceD","OwnershipTypeD","furnishedD to new column names"""

new_prop_column_names = {
    "propTypeD": "Property Type",
    "bedroomD": "Bedrooms",
    "bathD": "Bathrooms",
    "floorD": "Floor",
    "priceD": "Price",
    "OwnershipTypeD": "Ownership Type",
    "furnishedD": "Furnished"
}

prop_details = prop_details.rename(columns=new_prop_column_names)

print(prop_details.head())

"""Property price details available in the data frame"""

prop_price_details = ["priceD","sqFtPrice","bookingAmtExact","maintenanceCharges"]
prop_price_details = df[prop_price_details]
print(prop_price_details.head())

new_prop_price_column_names = {
    "priceD": "price",
    "sqFtPrice": "SqFtPrice",
    "bookingAmtExact": "bookingAmount",
    "maintenanceCharges": "maintenanceCharges",

}
new_price_col_names = prop_price_details.rename(columns=new_prop_price_column_names)

print(new_price_col_names.head())

"""Amenities and important Listing Details in the data frame"""

prop_features_details = ["luxAmenitiesD","possStatusD","transType","OwnershipTypeD","userType","companyname","oname","crisilStarRating","operatingSinceYear","postDateT","endDateT"]
prop_features_details = df[prop_features_details]
print(prop_features_details.head())

prop_features_details = ["luxAmenitiesD", "possStatusD", "transType", "OwnershipTypeD", "userType", "companyname", "oname", "crisilStarRating", "operatingSinceYear", "postDateT", "endDateT"]


prop_features_details = df[prop_features_details]


prop_features_details = prop_features_details.rename(columns={
    "luxAmenitiesD": "LuxuryAmenities",
    "possStatusD": "Status",
    "transType": "TransactionType",
    "OwnershipTypeD": "OwnershipType",
    "userType": "Posted By",
    "companyname": "CompanyName",
    "oname": "AgentName",
    "crisilStarRating": "CrisilRating",
    "operatingSinceYear": "OperatingSince",
    "postDateT": "PostedDate",
    "endDateT": "Validity"
})

# Displaying the first few rows
print(prop_features_details.head())

#Checking data to modify which has both number and integer
unique_floorNos = df['floorNo'].unique()
print('Unique Floors',unique_floorNos)

unique_Status = df['possStatusD'].unique()
print('Status',unique_Status)

unique_furnished = df['furnishedD'].unique()
print('Furnished',unique_furnished)

unique_isPaidUser = df['isPaidUser'].unique()
print('PaidUser',unique_isPaidUser)

unique_bedroomD = df['bedroomD'].unique()
print('Bedroom',unique_bedroomD)

unique_bathD = df['bathD'].unique()
print('Bathroom',unique_bathD)

unique_facingD = df['facingD'].unique()
print('Facing',unique_facingD)


unique_pmtSource = df['pmtSource'].unique()
print('PmtSource',unique_pmtSource)

unique_appSub = df['appSub'].unique()
print('AppSub',unique_appSub)

unique_appovedAuthC = df['appovedAuthC'].unique()
print('cScore',unique_appovedAuthC)

unique_availUnit = df['availUnit'].unique()
print('AvailUnit',unique_availUnit)

# unique_pd = df['pd'].unique()
# print('PD',unique_pd)

unique_companyname = df['companyname'].unique()
print('CompanyName',unique_companyname)

unique_maintenance = df['maintenanceD'].unique()
print('maintenance',unique_maintenance)

unique_powere = df['powerStatusD'].unique()
print('Power',unique_powere)

unique_maintenanceD = df['maintenanceD'].unique()
print('Maintenance',unique_maintenanceD)

unique_maintenanceD = df['transType'].unique()
print('transType',unique_maintenanceD)

unique_oid = df['oid'].unique()
print('oid',unique_oid)

"""After analysing the details in data frmrame this are the important properties categories (Property Details, Pricing, Amenities,Listing Details"""

Final_df = ["oid","propTypeD","bedroomD","bathD","floorD", "priceD","OwnershipTypeD","furnishedD","luxAmenitiesD","possStatusD","transType","OwnershipTypeD","userType","companyname","oname","crisilStarRating","operatingSinceYear","postDateT","endDateT",]
Final_df = df[Final_df]
print(Final_df.head())

# Data Cleaning
df['floorNo'] =df['floorNo'].replace({'Ground':'0'})
df['floorNo'] =df['floorNo'].replace({'Upper Basement':'-1'})
df['floorNo'] =df['floorNo'].replace({'NaN':-1})
df["floorNo"] = df["floorNo"].fillna('-1')
df["crisilStarRating"] = df["crisilStarRating"].fillna("-1")
df['operatingSinceYear'] =df['operatingSinceYear'].replace({'nan':'No Data'})
df['postDateT'] =df['postDateT'].replace({'nan':'No Data'})
df['endDateT'] =df['endDateT'].replace({'nan':'No Data'})
df['priceD'] =df['priceD'].replace({'nan':'No Data'})
df['sqFtPrice'] =df['sqFtPrice'].replace({'nan':'No Data'})
df['bookingAmtExact'] =df['bookingAmtExact'].replace({'nan':'No Data'})
df['maintenanceCharges'] =df['maintenanceCharges'].replace({'nan':'No Data'})
df['OwnershipTypeD'] =df['OwnershipTypeD'].fillna('No Data')
df['luxAmenitiesD'] = df['luxAmenitiesD'].fillna('No Data')
df['possStatusD'] = df['possStatusD'].fillna('No Data')
df['transType'] = df['transType'].fillna('No Data')
df['companyname'] =df['companyname'].fillna('No Data')
df['oname'] = df['oname'].fillna('No Data')

Final_df = ["oid","propTypeD","bedroomD","bathD","floorNo","priceD","OwnershipTypeD","furnishedD","luxAmenitiesD","possStatusD","transType","OwnershipTypeD","userType","companyname","oname","crisilStarRating"]
Final_df = df[Final_df]
print(Final_df)

"""Changing the Column names"""

update_column_name = {
    "oid": "id",
    "propTypeD": "PropertyType",
    "bedroomD": "Bedrooms",
    "bathD": "Bathrooms",
    "floorNo": "FloorNumber",
    "floorD": "TotalFloors",
    "priceD": "Price",
    "OwnershipTypeD": "OwnershipType",
    "furnishedD": "Furnished",
    "luxAmenitiesD": "LuxuryAmenities",
    "possStatusD": "PossessionStatus",
    "transType": "TransactionType",
    "userType": "UserType",
    "companyname": "CompanyName",
    "oname": "OwnerName",
    "crisilStarRating": "Rating",
}
columns_to_select = list(update_column_name.keys())
Final_df = df[columns_to_select].rename(columns=update_column_name)
print(Final_df.head())

"""print(Final_df.dtypes)"""

print(Final_df.dtypes)

Final_df["id"] = pd.to_numeric(Final_df["id"], errors="coerce")
def convert_price(price):
    if isinstance(price, str):
        if 'Cr' in price:
            # Convert Cr to numeric value
            return float(price.replace(" Cr", "").strip()) * 1e7  # 1 Cr = 10 million
        elif 'Lac' in price:
            # Convert Lac to numeric value
            return float(price.replace(" Lac", "").strip()) * 1e5  # 1 Lac = 100 thousand
        else:
            return pd.NA  # Return NaN for unrecognized format
    return price
Final_df["Price"] = Final_df["Price"].apply(convert_price)
Final_df["Bedrooms"] = pd.to_numeric(Final_df["Bedrooms"], errors="coerce")
Final_df["Bathrooms"] = pd.to_numeric(Final_df["Bathrooms"], errors="coerce")
Final_df["FloorNumber"] = pd.to_numeric(Final_df["FloorNumber"], errors="coerce")

#Final_df["Price"] = Final_df["Price"].str.replace(" Cr", "").astype(float) * 1e7  # Converted to numeric (INR)
Final_df["Rating"] = pd.to_numeric(Final_df["Rating"], errors="coerce")
print(Final_df.head())

print(Final_df.dtypes)

"""Changing the Datatypes"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#Bar Chart for Property Types
plt.figure(figsize=(10,6))
sns.countplot(x='propTypeD', data=df, palette='viridis')
plt.title('Number of Listings by Property Type')
plt.xlabel('Property Type')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10,6))
sns.countplot(x='furnishedD', data=df, palette='viridis')
plt.title('Number of Listings by Furnishing Status')
plt.xlabel('Furnishing Status')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

"""Creating the Database using the sqllite"""

import sqlite3
connection = sqlite3.connect('propertydetails.db', check_same_thread=False)
Final_df.to_sql('realestate_data', connection, if_exists='append', index=False)
cursor = connection.cursor()

cursor.execute("SELECT * FROM realestate_data")
rows = cursor.fetchall()
rows

#!pip install Flask

from flask import Flask
from flask import render_template
from flask import request
#!pip install flask_cors
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/viewproperty.html") #Default - Show Data
def viewproperty(): # Name of the method
    return render_template('viewproperty.html')

@app.route("/addproperty", methods=['GET', 'POST']) #
def addproperty():
  if request.method == 'POST':
    Id = request.form['id']
    PropertyType = request.form['PropertyType']
    Bedrooms = request.form['Bedrooms']
    Bathrooms = request.form['Bathrooms']
    FloorNumber = request.form['FloorNumber']
    TotalFloors = request.form['TotalFloors']
    Price = request.form['Price']
    OwnershipType = request.form['OwnershipType']
    Furnished = request.form['Furnished']
    LuxuryAmenities = request.form['LuxuryAmenities']
    PossessionStatus = request.form['PossessionStatus']
    TransactionType = request.form['TransactionType']
    UserType = request.form['UserType']
    CompanyName = request.form['CompanyName']
    OwnerName = request.form['OwnerName']
    Rating = request.form['Rating']
    print(id,PropertyType,Bedrooms,Bathrooms,FloorNumber,TotalFloors,Price,OwnershipType,Furnished,LuxuryAmenities,PossessionStatus,TransactionType,UserType,CompanyName,OwnerName,Rating)
    cur = mysql.cursor() #create a connection to the SQL instance
    #s='''INSERT INTO students(PropertyType) VALUES('{}');'''.format(PropertyType)
    s='''INSERT INTO students(id,PropertyType,Bedrooms,Bathrooms,FloorNumber,TotalFloors,Price,OwnershipType,Furnished,LuxuryAmenities,PossessionStatus,TransactionType,UserType,CompanyName,OwnerName,Rating) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');'''.format(id,PropertyType,Bedrooms,Bathrooms,FloorNumber,TotalFloors,Price,OwnershipType,Furnished,LuxuryAmenities,PossessionStatus,TransactionType,UserType,CompanyName,OwnerName,Rating)
    app.logger.info(s)
    cur.execute(s)
    mysql.commit()
  else:
    return render_template('addproperty.html)

  return '{"Result":"Success"}'

@app.route("/getpropertydetails", methods=['GET']) #Get property details
def get():
  cursor.execute("SELECT * FROM realestate_data")
  rows = cursor.fetchall()
  Results=[]
  for row in rows: #Format the Output Results and get to return string
    Result={}
    Result['id']=row[0]
    Result['PropertyType']=row[1]
    Result['Bedrooms']=row[2]
    Result['Bathrooms']=row[3]
    Result['FloorNumber']=row[4]
    Result['TotalFloors']=row[5]
    Result['Price']=row[6]
    Result['OwnershipType']=row[7]
    Result['Furnished']=row[8]
    Result['LuxuryAmenities']=row[9]
    Result['PossessionStatus']=row[10]
    Result['TransactionType']=row[11]
    Result['UserType']=row[12]
    Result['CompanyName']=row[13]
    Result['OwnerName']=row[14]
    Result['Rating']=row[15]
    Results.append(Result)
  response={'Results':Results, 'count':len(Results)}
  ret=app.response_class(
    response=json.dumps(response),
    status=200,
    mimetype='application/json'
  )
  return ret #Return the data in a string format

if __name__ == "__main__":
  #app.run(host='0.0.0.0',port='8080') #Run the flask app at port 8080
  #app.run(host='0.0.0.0',port='5000', debug=True) #Run the flask app at port 8080
  app.run(host='0.0.0.0',port='8080', ssl_context=('cert.pem', 'privkey.pem')) #Run the flask app at port 8080