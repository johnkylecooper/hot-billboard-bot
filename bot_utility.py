#!/usr/bin/env python
# coding: utf-8
import requests


def get_song_info():
    # In[1595]:
    
    
    # import the library we use to open URLs
    import urllib.request
    
    
    # In[1596]:
    
    
    from random import randint
    year=randint(1958,2020)
    
    
    # In[1597]:
    
    
    # specify which URL/web page we are going to be scraping
    url = "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_top-ten_singles_in_"+str(year)
    
    
    # In[1598]:
    
    
    # open the url using urllib.request and put the HTML into the page variable
    page = urllib.request.urlopen(url)
    
    
    # In[1599]:
    
    # import the BeautifulSoup library so we can parse HTML and XML documents
    from bs4 import BeautifulSoup
    
    # In[1600]:
    
    # parse the HTML from our URL into the BeautifulSoup parse tree format
    soup = BeautifulSoup(page, "html.parser")
    
    # In[1601]:
    
    
    # Use either View Source command on your web page or the BeautifulSoup function 'prettify' to
    # look at the HTML underlying our chosen web page
    #print(soup.prettify())
    
    # In[1602]:
    
    
    # play around with some of the HTML tags and bring back the page 'title' and the data between the start and end 'title' tags
    soup.title
    # refine this a step further by specifying the 'string' element and only bring back the content without the 'title' tags
    soup.title.string
    
    # In[1603]:
    
    
    # use the 'find_all' function to bring back all instances fo the 'table' tag in the HTML and store in 'all_tables' variable
    all_tables=soup.find_all("table")
    
    # In[1604]:
    
    
    right_table=soup.find('table', {"class": ["wikitable sortable", "plainrowheaders sortable wikitable"]})
    
    # In[1605]:
    
    
    A=[]
    B=[]
    C=[]
    D=[]
    E=[]
    F=[]
    G=[]
    idx=0
    for row in right_table.findAll('tr'):
        cells=row.findAll('td')
        if len(cells)==6:
            if cells[0].find(text=True)=="\"":
                A.append(A[idx-1])
                B.append(cells[0].find(text=""))
                C.append(cells[1].find(text=True))
                D.append(cells[2].find(text=True))
                E.append(cells[3].find(text=True))
                F.append(cells[4].find(text=True))
                G.append(cells[5].find(text=True))
            else:
                A.append(cells[0].find(text=True))
                B.append(cells[1].find(text=""))
                C.append(cells[2].find(text=True))
                D.append(cells[3].find(text=True))
                E.append(cells[4].find(text=True))
                F.append(cells[5].find(text=True))
            idx += 1
        if len(cells)==7:
            if cells[0].find(text=True)=="\"":
                A.append(A[idx-1])
                B.append(cells[0].find(text=""))
                C.append(cells[1].find(text=True))
                D.append(cells[2].find(text=True))
                E.append(cells[3].find(text=True))
                F.append(cells[4].find(text=True))
                G.append(cells[5].find(text=True))
            else:
                A.append(cells[0].find(text=True))
                B.append(cells[1].find(text=""))
                C.append(cells[2].find(text=True))
                D.append(cells[3].find(text=True))
                E.append(cells[4].find(text=True))
                F.append(cells[5].find(text=True))
                G.append(cells[6].find(text=True))
            idx += 1
        header=row.findAll('th')
        if len(header)==6:
            H0=header[0].find(text=True)
            H1=header[1].find(text=True)
            H2=header[2].find(text=True)
            H3=header[3].find(text=True)
            H4=header[4].find(text=True)
            H5=header[5].find(text=True)
        if len(header)==7:
            H0=header[0].find(text=True)
            H1=header[1].find(text=True)
            H2=header[2].find(text=True)
            H3=header[3].find(text=True)
            H4=header[4].find(text=True)
            H5=header[5].find(text=True)
            H6=header[6].find(text=True)
    
    # In[1607]:
    
    
    # Ensure B does not contain None Values
    # B = [i for i in B if i]
    res = [i for i in range(len(B)) if B[i] == None]
    n=0
    for index in res:
        A.pop(index-n)
        B.pop(index-n)
        C.pop(index-n)
        D.pop(index-n)
        E.pop(index-n)
        F.pop(index-n)
        n+=1
    
    
    # In[1608]:
    
    
    # HTML has an " between the td and the text; therefore, this needs to be fixed.
    for count, item in enumerate(B):
        B[count] = item.text
    # Remove \n in list items
    for count, item in enumerate(A):
        A[count] = item.strip()
    for count, item in enumerate(C):
        C[count] = item.strip()
    for count, item in enumerate(D):
        D[count] = item.strip()
    for count, item in enumerate(E):
        E[count] = item.strip()
    for count, item in enumerate(F):
        F[count] = item.strip()
    
    
    # In[1609]:
    
    
    import pandas as pd
    df = pd.DataFrame(A,columns=[H0.strip()])
    df[H1.strip()]=B
    df[H2.strip()]=C
    df[H3.strip()]=D
    df[H4.strip()]=E
    df[H5.strip()]=F
    
    # In[1610]:
    
    
    from datetime import datetime
    import calendar
    today = datetime.today()
    month = calendar.month_name[today.month]
    
    # In[1611]:
    
    import numpy as np
    x = np.array(df['Peak date'].str.find(month))
    index = np.where(x == 0)[0]
    from random import choice
    song = df.iloc[choice(index)]
    
    # In[1612]:
    
    textToSearch = song[H1.strip()]+" by "+song[H2.strip()]
    query = urllib.parse.quote(textToSearch)
    url = "https://www.youtube.com/results?search_query=" + query
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text_idx = response.text.find("\"videoId\"")
    result = response.text[text_idx:text_idx + 22].split(":")[1].strip('\"')

    lnk = "https://www.youtube.com/watch?v=" + result
    
    H = [H0.strip(), H1.strip(), H2.strip(), H3.strip(), H4.strip(), H5.strip()]
    
    return song, lnk, year, H