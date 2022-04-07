from email import message
import socket
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import json
import pandas as pd
import geopandas as gpd
from geopandas import GeoDataFrame
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, col
from pyspark.sql.functions import split
from datetime import datetime
import plotly.graph_objs as go
import plotly.io as pio
import plotly.express as px
import chart_studio.plotly as py
import plotly.graph_objs as go 
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import ast

HOST = '127.0.0.1'
PORT = 22223

timestamps=[]
x_lon=[]
y_lat=[]

#creating a socket at client side
#using TCP/IP Protocol
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
df=pd.DataFrame()
#connect it to server and port
#number on local computer
s.connect((HOST, PORT))
#receive message strinf from
#server, at a time 1024 
msg = s.recv(1024)

#repeat as long as message
#string are not empty
while msg:
    row=ast.literal_eval(msg.decode("UTF-8"))
    msg = s.recv(1024)
    print(row)
    timestamps.append(row['timestamp'])
    #print(timestamps)
    y_lat.append(float(row['iss_position']['latitude']))
    #print(y_lat)
    x_lon.append(float(row['iss_position']['longitude']))
    #print(x_lon)
    
s.close()

df= pd.DataFrame(
        {'timesamp': timestamps,
        'Latitude': y_lat,
        'Longitude': x_lon
        })

df['Mycol1'] =  pd.to_datetime(df['timesamp'], unit='s')

df['dates'] = df['Mycol1'].dt.time

init_notebook_mode(connected=True)

fig= px.scatter_geo(df,lat='Latitude',lon='Longitude', hover_name='dates')
fig.update_layout(title_text='ISS lOCATION', title_x=0.5)
pio.renderers.default = 'iframe'
fig.show()