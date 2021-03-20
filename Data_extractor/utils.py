import requests as r
import csv
import pandas as pd
import datetime


#function to retrive access token to interact with the api
def getauthToken():
    headers = {
        'Content-type': 'application/x-www-form-urlencoded',
        'Authorization': 'Basic aW9PNGpGTVk1eTI4U3ZNamVpR1JueW8tUFRRMnhMYWs6YTF1Q20zSjNYWFZVRmNJaTJYT09pby1JTUw5Si11T2dRQWdmdTJFRDFjNnZfSXB6NHNSWGE2bWlScFlCbEtOTm04QnVtcTdmU3N6d3JXOEs1OGJfanNETzlQNC1kLnhBNS0wMw=='
    }
    data = {
    'grant_type': 'client_credentials'
    }
    response = r.post('https://auth.wattsight.com/oauth2/token', headers=headers, data=data).json()
    token = response["access_token"]
    return token



#use this function to download time serial data, find curveID here  https://api.wattsight.com/#curves
def DownloadPriceCurve(access_token, curveID):

    headers = {
        'accept': 'application/json',
        'authorization': 'Bearer '+ access_token,
    }
    params = (
        ('from', '2018-01-10'),
        ('to', '2021-03-21'),
    )

    response = r.get('https://api.wattsight.com/api/series/'+str(curveID), headers=headers, params=params)
    print(response.content)
    price = response.json()
    #print(price)
    df = pd.DataFrame(price["points"])
    
    # saving the dataframe  
    df.to_csv('priDEintradayID1103.csv',header=['Timestamp','Price'])  

    
#the api return a unixtimestamp use this Function to replace it with a datatype and save in a new csv
def UnixTimestampConverter():
    df = pd.read_csv('/Users/emanuele.cesari/Desktop/Start_Hack21/Data_extractor/priDEintradayID1103.csv', header=0, index_col=0, parse_dates=True, squeeze=True)

    dt = []

    for i in df["Timestamp"]:
        dt.append(datetime.datetime.fromtimestamp(i / 1000))

    df["Timestamp"] = dt 
    df.to_csv('PriDEintradayID1103.csv',index=False)


def main():
    
    #Access token expire so need to refresh it sometimes
    access_token = getauthToken()

    #Download pri de intraday €/mwh cet min15 a
    #DownloadPriceCurve(access_token, 1103)
    
    #UnixTimestampConverter()


main()