import pandas as pd
from pytz import timezone
import numpy as np


def getdf():
           
    # Get single data frame with April and May data
    dfApr = pd.read_csv("http://www.interconnector.com/Data/ISIS/flowdata/interconnector_historical_201804.csv")
    dfMay = pd.read_csv("http://www.interconnector.com/Data/ISIS/flowdata/interconnector_historical_201805.csv")
    df = dfApr.append(dfMay)
    df = df.drop_duplicates()
    
    
    # Convert dates to timezone aware datetime objects
    tzGMT = timezone('GMT')
    tzUKT = timezone('Europe/London')
    tzCET = timezone('CET')
    
    time_cols = ['PublishTime GMT','PublishTime UKT','PublishTime CET','Hour GMT','Hour UKT','Hour CET']
    for i in time_cols:
        df[i] = pd.to_datetime(df[i], format='%d/%m/%Y %H:%M')
        if 'GMT' in i:
            df[i] = df[i].dt.tz_localize(tzGMT)
        if 'UKT' in i:
            df[i] = df[i].dt.tz_localize(tzUKT)
        if 'CET' in i:
            df[i] = df[i].dt.tz_localize(tzCET)
        
    date_cols = ['Gasday']
    for i in date_cols:
        df[i] = pd.to_datetime(df[i], format='%d/%m/%Y')
    
    
    # Replace appropriate values with Null (None)
    df = df.replace({'unknown':None, '-':None})
    df = df.where((pd.notnull(df)), None)
    
    
    # Explicitly define data types
    typesdict = {'Location':'object','DataItem':'object',
                 'Quantity':'float','Units':'object','Direction':'object',
                 'Inventory Type':'object','Notes':'object'}
    
    df = df.astype(dtype=typesdict)
    
    # Return cleaned dataframe
    return df


    