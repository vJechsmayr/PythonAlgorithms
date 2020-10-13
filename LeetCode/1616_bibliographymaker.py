#automatic Bibliography and Foot notes maker
bootPython = True


def atriclewithauthor():
    dic1= {'Author First name' : 'Sujith' , 'Author last name': 'Rex' , 'Article name' : 'indian marxist', 'Publisher': 'BTEG', ' Volume' : '5' , 'issue' :'6' , 'Month' : 'Dec-jan', 'Page Number' : '52', 'year' : '1997'}
    print('Author First name')
    dic1['Author First name'] = input()
    print('Author last name')
    dic1['Author last name'] = input()
    print('Article name')
    dic1['Article name'] = input()
    print('Publisher')
    dic1['Publisher'] = input()
    print('Volume')
    dic1[' Volume'] = input()
    print('issue')
    dic1['issue'] = input()
    print('Month')
    dic1['Month'] = input()
    print('Page Number')
    dic1['year'] = input()
    print('Year')
    dic1['Page Number'] = input()
    strby = '/'
    print('Your Foot note is here' , 'Check your intent and paste to your word file')
    print(dic1['Author First name'] , ',' , dic1['Author last name'], ',' , '"' ,dic1['Article name'], '"' , ',' , dic1['Publisher'] , dic1[' Volume'],strby, dic1['issue'] , '(', dic1['Month'], ',', dic1['year'], ')',':',dic1['Page Number'] , '.' )
    print('----'* 7 )
    print('Your Bibliography is here' , 'Check your intent and paste to your word file')
    print(dic1['Author last name'],',' , dic1['Author First name'], '.', '"' , dic1['Article name'],'.', '"' , dic1['Publisher'], dic1[' Volume'],strby, dic1['issue'],'(', dic1['Month'], ',', dic1['year'],')',':' ,dic1['Page Number'],'.')
    print('Exit Press 1')
    commonexit= input()

    if commonexit == 1:
        bootPython = True


def articlewithoutauthor():
    dic2 = { 'Article name': 'indian marxist', 'Publisher': 'BTEG', ' Volume': '5', 'issue': '6', 'Month': 'Dec-jan', 'year' : '1997', 'Page Number': '52'}


    print('Article name')
    dic2['Article name'] = input()
    print('Publisher')
    dic2['Publisher'] = input()
    print('Volume')
    dic2[' Volume'] = input()
    print('issue')
    dic2['issue'] = input()
    print('Month')
    dic2['Month'] = input()
    print('Page Number')
    dic2['year'] = input()
    print('Year')
    dic2['Page Number'] = input()
    strby = '/'
    print('Your Foot note is here', 'Check your intent and paste to your word file')
    print( '"', dic2['Article name'], '"', ',', dic2['Publisher'], dic2[' Volume'], strby, dic2['issue'], '(', dic2['Month'], ',', dic2['year'], ')', ':', dic2['Page Number'], '.')
    print('----' * 7)
    print('Your Bibliography is here', 'Check your intent and paste to your word file')
    print('"', dic2['Article name'], '.', '"',dic2['Publisher'], dic2[' Volume'], strby, dic2['issue'], '(', dic2['Month'], ',', dic2['year'], ')', ':', dic2['Page Number'], '.')
    print('Exit Press 1')
    commonexit = input()

    if commonexit == 1:
        bootPython = True

#encylopedia Article

def encylopaediawitheditor():
    dic3 = {'author First name': 'Sujith', 'Author last name': 'Rex', 'Article name': 'indian marxist','Publisher': 'BTEG', ' Volume': '5', 'Page Number': '52', 'year': '1997', 'Encyclo' : 'Religion and Ethics', 'Editor' : 'James', 'place' : 'edinburg'}
    print('Author First name')
    dic3['Author First name'] = input()
    print('Author last name')
    dic3['Author last name'] = input()
    print('Article name')
    dic3['Article name'] = input()
    print('Publisher')
    dic3['Publisher'] = input()
    print('Encyloaedia Name (only name)')
    dic3['Encyclo'] = input()
    print('Editor Name')
    dic3['Editor'] = input()
    dic3['Publisher'] = input()
    print('Volume')
    dic3[' Volume'] = input()
    print('issue')
    dic3['issue'] = input()
    print('Place')
    dic3['place'] = input()

    print('Page Number')
    dic3['year'] = input()
    print('Year')
    dic3['Page Number'] = input()
    strby = '/'
    print('Your Foot note is here' , 'Check your intent and paste to your word file')
    print(dic3['Author First name'] , dic3['Author last name'], ',' , '"' ,dic3['Article name'], ',' , '"' , 'Encyclopaedia of', dic3['Encyclo'], 'edited by' , dic3['Editor'], ',', dic3[' Volume'],strby, dic3['issue'], '(', dic3['place'], ':', dic3['Publisher']  , ',', dic3['year'], ')',':',dic3['Page Number'] , '.' )
    print('----'* 7 )
    print('Your Bibliography is here' , 'Check your intent and paste to your word file')
    print(dic3['Author last name'] , ',', dic3['Author First name'], '.' , '"' ,dic3['Article name'], '.' , '"' , 'Encyclopaedia of', dic3['Encyclo'], 'edited by' , dic3['Editor'], '.', dic3[' Volume'],strby, dic3['issue'], '(', dic3['place'], ':', dic3['Publisher']  , ',', dic3['year'], ')',':',dic3['Page Number'] , '.' )
    print('Exit Press 1')

    commonexit = input()

    if commonexit == 1:
        bootPython = True


def encyclopaediawithoutauthor():
    dic4 = {'Article name': 'indian marxist', ' Volume': '5', 'Page Number': '52', 'year': '1997', 'Encyclo' : 'Religion and Ethics', 'place' : 'edinburg'}

    print('Article name')
    dic4['Article name'] = input()
    print('Encyloaedia Name (only name)')
    dic4['Encyclo'] = input()
    print('Volume')
    dic4[' Volume'] = input()
    print('issue')
    dic4['issue'] = input()

    print('Page Number')
    dic4['Page Number'] = input()
    print('Year')
    dic4['year'] = input()
    strby = '/'
    print('Your Foot note is here', 'Check your intent and paste to your word file')
    print('Encyclopaedia of', dic4['Encyclo'], ',',  dic4['year'], 'ed.,', 'vol.', dic4[' Volume'],',', 's.v;','"', dic4['Article name'],'"', ',', dic4['Page Number'],'.')
    print('----' * 7)
    print('Your Bibliography is here', 'Check your intent and paste to your word file')
    print('Encyclopaedia of', dic4['Encyclo'], '.', dic4['year'], 'ed.', 'vol.', dic4[' Volume'], '.', 's.v.', '"', dic4['Article name'],'"', ',', dic4['Page Number'], '.')
    print('Exit Press 1')

    commonexit = input()

    if commonexit == 1:
        bootPython = True

def newspaperauthor():
    dic5 = {'Author full name' :'Sujith', 'Article Titile': 'Python5', 'News paper name' : 'Sujith', 'Date ': '12 oct 2007', 'page' : '5', 'Edition' :'nellai'}
    print('Author Full Name')
    dic5['Author full name'] = input()
    print('Article Title')
    dic5['Article Titile'] = input()
    print('News Paper Name')
    dic5['News paper name'] = input()
    print('Editon (city name)')
    dic5['Edition'] = input()
    print('Date  Example : 13 oct 1997')
    dic5['Date '] = input()
    print('Page Number')
    dic5['page'] = input()
    print('Your Foot note is here', 'Check your intent and paste to your word file')
    print(dic5['Author full name'], ',', '"', dic5['Article Titile'], ',','"',  dic5['News paper name'],'(', dic5['Edition'],')',',', dic5['Date '],',', dic5['page'],'.')
    print('----' * 7)
    print('Your Bibliography is here', 'Check your intent and paste to your word file')
    print(dic5['News paper name'], ',',dic5['Date '], '.' )
    print('Exit Press 1')
    print('Github @rexb0tnet')

    commonexit = input()

    if commonexit == 1:
        bootPython = True

def newspaperwithoutauthor():
    dic6 = { 'Article Titile': 'Python5', 'News paper name' : 'Sujith', 'Date ': '12 oct 2007', 'page' : '5', 'Edition' : 'nellai'}

    print('Article Title')
    dic6['Article Titile'] = input()
    print('News Paper Name')
    dic6['News paper name'] = input()
    print('Editon (city name)')
    dic6['Edition'] = input()
    print('Date  Example : 13 oct 1997')
    dic6['Date '] = input()
    print('Page Number')
    dic6['page'] = input()
    print('Your Foot note is here', 'Check your intent and paste to your word file')
    print( '"', dic6['Article Titile'], ',', '"', dic6['News paper name'], '(', dic6['Edition'],')',',', dic6['Date '],',', dic6['page'],'.')
    print('----' * 7)
    print('Your Bibliography is here', 'Check your intent and paste to your word file')
    print(dic6['News paper name'], ',',dic6['Date '], '.' )
    print('Exit Press 1')

    commonexit = input()

    if commonexit == 1:
        bootPython = True

def oneauthor():
    bookdic1 = {'Author First name': 'Romila', 'Author Last name' : 'Thapar', 'Title' : 'The Past and prejustice', 'Pub Place' : 'Delhi' , 'Publisher': 'NBT', 'Year': '1197', 'page' : '25'}

    print('Author First Name')
    bookdic1['Author First name'] = input()
    print('Author Last Name')
    bookdic1['Author Last name'] = input()
    print('Book Title')
    bookdic1['Title'] = input()
    print('Publish Place')
    bookdic1['Pub Place'] = input()
    print('Publisher')
    bookdic1['Publisher'] = input()
    print('Year')
    bookdic1['Year'] = input()
    print('Page number')
    bookdic1['page'] = input()
    print('Your Foot note is here', 'Check your intent and paste to your word file')
    print(bookdic1['Author First name' ], bookdic1['Author Last name'], ',', bookdic1['Title'],'(',bookdic1['Pub Place'],':',bookdic1['Publisher'],',', bookdic1['Year'],')',',', bookdic1['page'],'.' )
    print('Your Bibliography is here', 'Check your intent and paste to your word file')
    print(bookdic1['Author Last name'],',', bookdic1['Author First name'],  '.', bookdic1['Title'], '.',bookdic1['Pub Place'], ':', bookdic1['Publisher'], ',', bookdic1['Year'], '.')
    print('Exit Press 1')

    commonexit = input()

    if commonexit == 1:
        bootPython = True

def twoauthors():
    bookdic2 = {'Author First name': 'Romila', 'Author Last name' : 'Thapar', 'Second Author':'Rex',  'Title' : 'The Past and prejustice', 'Pub Place' : 'Delhi' , 'Publisher': 'NBT', 'Year': '1197', 'page' : '25'}

    print('First author First Name')
    bookdic2['Author First name'] = input()
    print('Author Last Name')
    bookdic2['First author Last name'] = input()
    print('Second Author  fullname')
    bookdic2['Second Author'] = input()
    print('Book Title')
    bookdic2['Title'] = input()
    print('Publish Place')
    bookdic2['Pub Place'] = input()
    print('Publisher')
    bookdic2['Publisher'] = input()
    print('Year')
    bookdic2['Year'] = input()
    print('Page number')
    bookdic2['page'] = input()
    print('Your Foot note is here', 'Check your intent and paste to your word file')
    print(bookdic2['Author First name' ], bookdic2['Author Last name'], 'and', bookdic2['Second Author'],',', 'Jr.,', bookdic2['Title'],'(',bookdic2['Pub Place'],':',bookdic2['Publisher'],',', bookdic2['Year'],')',',', bookdic2['page'],'.' )
    print('Your Bibliography is here', 'Check your intent and paste to your word file')
    print(bookdic2['Author Last name'],',', bookdic2['Author First name'], 'and', bookdic2['Second Author'], ',','Jr.,', '.', bookdic2['Title'], '.',bookdic2['Pub Place'], ':', bookdic2['Publisher'], ',', bookdic2['Year'], '.')
    print('Exit Press 1')

    commonexit = input()

    if commonexit == 1:
        bootPython = True
def books():
    print('1. oneauthor')
    print('2. Two authors')
    book_choose = input()
    if book_choose == '1':
        oneauthor()
    if book_choose == '2':
        twoauthors()

def artice():
    print('1.Article with Author')
    print('2.Article without Author')
    print('3.Encylopaedia articles - with author')
    print('4.Encylopaedia articles - without author')
    print('5. News article - author name given')
    print('6.News article - author name not given')
    article_choose = input()

    if article_choose == '1':
        atriclewithauthor()
    if article_choose == '2' :
        articlewithoutauthor()
    if article_choose == '3':
        encylopaediawitheditor()
    if article_choose =='4':
        encyclopaediawithoutauthor()
    if article_choose == '5':
        newspaperauthor()
    if article_choose == '6':
        newspaperwithoutauthor()


while bootPython == True:

    print("Automatic Bibliography and Foot notes maker")
    print("by Sujith Rex github@rexb0tnet")
    print('Choose your source')
    print('1.Books')
    print('2.Articles')
    print('3.Websites')
    choosenumber = input()
    print('Choose your number')

    if choosenumber == '1':
        books()
    if choosenumber == '2':
        artice()


