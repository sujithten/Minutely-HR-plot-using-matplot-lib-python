# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 14:00:26 2019

@author: Sujith Tenali
"""

import pandas as pd
import time
from datetime import timedelta 
import datetime
from pandas import *
import random

data = pd.read_csv('df_Rhythm4analyze_o_37852_1558704625828706.csv')
data['epoch_start'] = data['epoch_start']/1000
data['time2'] = pd.to_datetime(data['epoch_start'],unit='ms',utc=None, box=True, format=None)

data['time2']=data['time2'].dt.tz_localize('UTC').dt.tz_convert('Asia/Calcutta')
data['normalised_date'] = data['time2'].dt.date

dates = data['normalised_date'].unique()

#creating range for x-axis
dates2 =[]
dates2.append(dates[0]-timedelta(days=1) )
dates2.append(dates[-1]+timedelta(days=1) )

#creating string dates for x-axis labels
strdates = []
#strdates.append(' ')


for date in dates:
    temp =date.strftime('%b %d,%Y')
    strdates.append(temp)
#strdates.append(' ')





#extracting info for a particular date
for date in dates:
    data[date] = data[data['normalised_date'] == date].filter(items=['RhythmHR'])

low = []
high=[]
mean2 = []
yrange = []
yrange.append(0)

   
for date in dates:
    low.append(data[date].min())
  
for date in dates:
    high.append(data[date].max())
    
    
for date in dates:
    mean2.append((data[date].mean()))
  
yrange.append(max(high) + 40)      
open=mean2

dates3 = []
for date in dates:
    dt = datetime.combine(date, datetime.min.time())
    dates3.append(dt)


dt2=[]
for date in dates2:
    dt = datetime.combine(date, datetime.min.time())
    dt2.append(dt)

unixseconds = []
timestamp3 = datetime.timestamp(dt2[0])* 1e3
unixseconds.append(timestamp3)

for date in dates3:
    timestamp3 = datetime.timestamp(date)* 1e3
    unixseconds.append(timestamp3)
timestamp3 = datetime.timestamp(dt2[-1])* 1e3
unixseconds.append(timestamp3)  


unix2 = []
unix2.append(int(unixseconds[0]))
unix2.append(int(unixseconds[-1]))


sum2 = unix2[1]-unix2[0]


i=1
unixseconds2=[]
for i in range(1,len(dates)+1):
    unixseconds2.append(unixseconds[i])
    i = i+1






import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.patches import Ellipse
from matplotlib.text import OffsetFrom
prop = fm.FontProperties(fname='C:/Users/Sujith Tenali/Desktop/Intern/DayWise/Montserrat-Bold.ttf')
prop2 = fm.FontProperties(fname='C:/Users/Sujith Tenali/Desktop/Intern/DayWise/Montserrat-Medium.ttf')

fig= plt.figure(figsize=(8,5))
plt.grid(b=None, which='major', axis='both',linewidth=0.2)
i=0
for unixsecond in unixseconds2:
    plt.annotate(int(high[i]),xy=(unixsecond, 1.5),  xytext=(unixsecond-(sum2/65), high[i]+2),fontproperties=prop2)
    i=i+1
i=0    
for unixsecond in unixseconds2:
    plt.annotate(int(low[i]),xy=(unixsecond, 1.5),  xytext=(unixsecond-(sum2/65), low[i]-4.5),fontproperties=prop2)
    i=i+1
i=0    
for unixsecond in unixseconds2:
    plt.annotate(int(mean2[i]),xy=(unixsecond, 1.5),  xytext=(unixsecond, mean2[i]+1),fontproperties=prop2)
    i=i+1

i=0
for unixsecond in unixseconds2:
    plt.hlines(mean2[i], unixsecond, unixsecond+(sum2/38), colors='#22ACE2')
    i=i+1
   
x=[unixseconds2[2]]
y = [low[2],high[2]]
plt.xticks(unixseconds2,strdates,fontproperties=prop,rotation=35,ha='right',va='top')
plt.yticks(fontproperties=prop)
plt.ylabel('Minutely HR (bpm)', fontproperties=prop,size=12)
i=0
plt.xlim(unix2[0],unix2[-1])
plt.ylim(yrange)


i=0
for  unixsecond in unixseconds2:
    plt.errorbar(x=unixsecond, y=[low[i],high[i]],  label=None,color="#22ACE2",elinewidth = 20)
    i=i+1
plt.errorbar(x=unixseconds[-1], y=[low[-1],high[-1]],  label='Avg',color="#22ACE2",elinewidth = 20)    
plt.title('Day Wise',fontproperties=prop,size=18)

 



plt.legend()
plt.savefig('name11'+str(random.randint(1,100000))+'.png', dpi=325, facecolor='w', edgecolor='w',
        orientation='landscape', papertype=None, format=None,
        transparent=False, bbox_inches='tight', pad_inches=0.1,
        frameon=None, metadata=None)