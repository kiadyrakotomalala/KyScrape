
#Put here all actions
#All action take a BeautifulSoup object --> complete page
#Return a list for continue
#Return a string if stop (last action and writing data action)

def getDataField(option):
    dataField = {}
    for opt in option:
        dataField[opt]= None
    return dataField


def Action1(soup):
    print 'Action1'
    themeList = []
    for li in soup.findAll('li', class_ = 'list_thm'):
        themeList.append(li.find('a')['href'].replace('/.','http://www.annumada.com'))

    return themeList

def Action2(soup):    
    print 'Action2'
    rubriqueList = []
    for li in soup.findAll('li', class_ = 'list_rubrique'):
        rubriqueList.append(li.find('a')['href'].replace('/.','http://www.annumada.com'))
    return rubriqueList

def Action3(soup):
    print 'Action3'
    villeList = []
    for li in soup.findAll('li', class_ = 'list_ville'):
        villeList.append(li.find('a')['href'].replace('/.','http://www.annumada.com'))
    return villeList

def Action4(soup):
    print 'Action4'
    for fieldset in soup.findAll('fieldset', class_="display_list"):

#Put here all fields for the data        
        dataField = getDataField(['name', 'rubrique', 'adresse', 'telephone', 'fax', 'mail','ville'])

        dataField['name'] = fieldset.find('legend').get_text().encode('utf-8')
        dataField['rubrique'] = [x.get_text() for x in fieldset.findAll('li', class_= 'rubrique')]
        
        try:
            dataField['adresse'] = fieldset.find('li', class_ = 'address').get_text()
        except:
            pass
        try:
            dataField['telephone'] = fieldset.find('li', class_ = 'fix').get_text()
        except:
            pass
        try:
            dataField['fax'] = fieldset.find('li', class_ = 'fax').get_text()
        except:
            pass
        try:
            dataField['mail'] = fieldset.find('li', class_ = 'mailaka').find('a')['title']
        except:
            pass
        try:
            dataField['ville'] = soup.find('div', class_="display_clear2").find('strong').get_text()
        except:
            pass
        
    return dataField