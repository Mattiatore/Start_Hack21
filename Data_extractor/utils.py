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
    print('DownloadTimeSeriesCurve called')
    headers = {
        'accept': 'application/json',
        'authorization': 'Bearer '+ access_token,
    }
    params = (
        ('from', '2018-12-10'),
        ('to', '2021-03-21'),
    )

    response = r.get('https://api.wattsight.com/api/series/' + str(curveID), headers=headers, params=params)
    print(response)
    price = response.json()
    print(price)
    df = pd.DataFrame(price["points"])
    
#the api return a unixtimestamp  here I am replacing it with a datatype and save in a new csv
    dt = []
    for i in df[0]:
        print(i)
        dt.append(datetime.datetime.fromtimestamp(i / 1000))
    df[0] = dt
    df.to_csv(str(curveID)+'.csv',index=False)



#Downlaod intradayPriceCurve and save into a csv file
def getIntradayCurve():
   #Access token expire so need to refresh it sometimes
    access_token = getauthToken()

    curveIDIntraday = ['1103', '143289', '143325']

    for i in curveIDIntraday:
        DownloadTimeSeriesCurve(access_token,i)
    

#Download Price Imbalance curve 
def getImbalancePriceCurve():
  
   #Access token expire so need to refresh it sometimes
    access_token = getauthToken()
    print(access_token)

    DownloadTimeSeriesCurve(access_token,'66305')
    


#Download Price Imbalance curve 
def getImbalanceGRIDCurve():
  
   #Access token expire so need to refresh it sometimes
    access_token = getauthToken()
    print(access_token)

    DownloadTimeSeriesCurve(access_token,'66315')


#Download Nuc Production curve and available capacity
def getNUCCurve():

    curveIDs = ['21899', '128629']

   #Access token expire so need to refresh it sometimes
    access_token = getauthToken()

    for i in curveIDs:
        DownloadTimeSeriesCurve(access_token,i)



#Download CoalProduction curve
def getCoalCurve():

    curveIDs = ['28138']

   #Access token expire so need to refresh it sometimes
    access_token = getauthToken()

    for i in curveIDs:
        DownloadTimeSeriesCurve(access_token,i)


#Download LigniteProduction curve
def getLigniteCurve():

    curveIDs = ['28266']

   #Access token expire so need to refresh it sometimes
    access_token = getauthToken()

    for i in curveIDs:
        DownloadTimeSeriesCurve(access_token,i)


#DownloadGASProduction curve
def getGASCurve():

    curveIDs = ['28336']

   #Access token expire so need to refresh it sometimes
    access_token = getauthToken()

    for i in curveIDs:
        DownloadTimeSeriesCurve(access_token, i)
        

def main():
    #getImbalancePriceCurve()
    #getIntradayCurve()
    #getImbalanceGRIDCurve()
    #getNUCCurve()
    #getCoalCurve()
    #getLigniteCurve()
    
    getGASCurve()

main()
