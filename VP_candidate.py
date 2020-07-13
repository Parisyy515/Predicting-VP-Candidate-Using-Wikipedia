import collections
import matplotlib.pyplot as plt
import bs4
import requests
import datetime
from datetime import *
import operator


url_list=['https://en.wikipedia.org/w/index.php?title=Keisha_Lance_Bottoms&action=history','https://en.wikipedia.org/w/index.php?title=Elizabeth_Warren&action=history','https://en.wikipedia.org/w/index.php?title=Val_Demings&action=history','https://en.wikipedia.org/w/index.php?title=Kamala_Harris&action=history','https://en.wikipedia.org/w/index.php?title=Michelle_Lujan_Grisham&action=history','https://en.wikipedia.org/w/index.php?title=Susan_Rice&action=history']
allcandidate={}
candidate=[]
cnt=[]
present = datetime.now()
past7 = present-timedelta(days=7)
datemask = "%Y-%m-%d"

def get_name(text):
    a=''
    for i in range(0,len(text)):
        if a[i]==':':
            break
        else:
            a+=a[i]
    return a[i]


def each_candidate(url): 
    #define a sub-function to extract name 
    def get_name(text):
        a=''
        for i in range(0,len(text)):
            if text[i]==':':
                break
            else:
                a+=text[i]
                i+=i
        return a
    
    #define a sub-function to find how many time the page has been editted in the recent week
    def one_week(r):
        new_r=[]
        r_recent=[]
        for i in range(0,len(r)):
            date=r[i]
            date_split=r[i].split()
            d=date_split[0]

            if len(d)==1:
                d='0'+str(d) 
            else: 
                d=str(d)

            y=str(date_split[2]) 

            if date_split[1]== "January":
                m='01'
            elif date_split[1]== "February":
                m='02'
            elif date_split[1]== "March":
                m='03'
            elif date_split[1]== "April":
                m='04'
            elif date_split[1]== "May":
                m='05'
            elif date_split[1]== "June":
                m='06'
            elif date_split[1]== "July":
                m='07'
            elif date_split[1]== "August":
                m='08'
            elif date_split[1]== "September":
                m='09' 
            elif date_split[1]== "October":
                m='10' 
            elif date_split[1]== "November":
                m='11'
            elif date_split[1]== "December":
                m='12' 
            else:
                m='00'     

            new_r.append(y+'-'+m+'-'+d)
            
        #among the list of newly formatted date, find the recent one week 
        for i in range(0,len(new_r)):
            if datetime.strptime(new_r[i], datemask)>=past7:
                r_recent.append(new_r[i])
            elif datetime.strptime(new_r[i], datemask)<past7:
                break
                     
        return r_recent               


    #loop through main page to find all candidate wikipedia page, and print out its editting frequency   
    result=requests.get(url)
    result_soup=bs4.BeautifulSoup(result.text,"html.parser")
    a=result_soup.select('.mw-changeslist-date')
    R= []
    
    
    #loop through all items in the mw-changelist-date class and append dates into a new list R, R contain all edit dates 
    for i in range(0,len(a)):
        a1=a[i].text
        i+=i
        R.append(a1[-12:])
    
    r=one_week(R)
    
    #extract candidate name 
    text=result_soup.select('title')[0].getText()
    name=get_name(text)
    
    occurrences = collections.Counter(R)

    print(name)
    print(f'The total editting times in recent one week is {len(one_week(R))}')
    plt.figure(figsize=(30,3))
    plt.title(f'{name} - Editing frequency ')
    plt.bar(occurrences.keys(),occurrences.values(),align='edge',width=0.3)

    candidate.append(name)
    cnt.append(len(one_week(R)))
  
for url in url_list:
    each_candidate(url)
      
allcandidate=dict(zip(candidate,cnt))  
max_key = max(allcandidate, key=allcandidate.get)
print(f'Today is {present}')
print(f'Based on the total editting times in the recent week, my guess for VP is {max_key}')
print('Please see most recent 50 edits for each candidate below')


    