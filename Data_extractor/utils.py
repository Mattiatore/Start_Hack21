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
def DownloadTimeSeriesCurve(access_token, curveID):

    headers = {
        'accept': 'application/json',
        'authorization': 'Bearer '+ access_token,
    }
    params = (
        ('from', '2018-01-10'),
        ('to', '2021-03-21'),
    )

    response = r.get('https://api.wattsight.com/api/series/'+str(curveID), headers=headers, params=params)
    price = response.json()
    df = pd.DataFrame(price["points"])
    
#the api return a unixtimestamp use this Function to replace it with a datatype and save in a new csv
    dt = []
    for i in df[0]:
        print(i)
        dt.append(datetime.datetime.fromtimestamp(i / 1000))
    df[0] = dt
    df.to_csv(str(curveID)+'.csv',index=False)



def main():
    
    #Access token expire so need to refresh it sometimes
    access_token = getauthToken()

    curveIDIntraday = ['1103', '143289', '143325']
    for i in curveIDIntraday:
        DownloadTimeSeriesCurve(access_token,i)
   

    #Download pri de intraday €/mwh cet min15 a
    #DownloadPriceCurve(access_token, 1103)
    
    #UnixTimestampConverter()


main()