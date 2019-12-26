# Batch Citation Machine GUI
import re, datetime, urllib.request
from bs4 import BeautifulSoup
from dateutil import parser

# Main Citation Functions
def citation_components(web_address):
    
    req = urllib.request.Request(web_address, headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'})
    response = urllib.request.urlopen(req)
    html = response.read()

    soup = BeautifulSoup(html, 'html.parser')

    # Page Title from <title> tag | Website Title from <title> tag or from URL
    try:
        title_text = str(soup.title.contents[0]) # String Slice Removes <title> and </title>
    except:
        title_text = "" # In case no <title> tag

    title_segments = title_text.split(" - ")
    if len(title_segments) > 1: # If website title coems after "-" in page title
        website_title = title_segments[-1]
        page_title = " - "
        page_title = page_title.join(title_segments[:-1])

    else:
        website_title = re.search(r"([^.\/]+?)(?:\.(?:sg|net|com|org|gov|edu|int|eu|us))+",web_address).group(1) # Captures the last string between .DOMAIN and the . in front of that
        website_title = website_title.capitalize() # Capitalises the first letter of the string
        page_title = title_text

    if page_title == "":
        page_title = website_title # For when there is no <title> tag

    # Searches for Authors via href with "author"
    for a in soup.find_all('a', href=True): # Find first author
        if "author" in a['href']:
            # print ("Author URL", a['href'])
            author_path = a['href']
            author_name = re.search(r"\/([^\/]+)$", author_path).group(1)
            author_name = author_name.split("-")

            break
    try:
        first_name = author_name[0].capitalize()
        last_name = author_name[-1].capitalize()
        
        concat_name = first_name + last_name
        if '=' in concat_name or '?' in concat_name or '+' in concat_name:
            first_name = last_name = ""
    except:
        first_name = last_name = ""

     # Accessed Date
    today = datetime.date.today()
    date_accessed = today.strftime("%B %d, %Y")

    # Published Date
    try:
        date_published = ""
        time_element = soup.find('time')
        
        if time_element.has_attr('datetime') and time_element["datetime"]!= "": # Take date from attribute
            web_datetime = time_element["datetime"]
            date = parser.parse(web_datetime)
            
        else: # take date from contents
            date_published = time_element.contents[0]
            date = parser.parse(date_published)

        date_published = date.strftime("%B %d, %Y")
            

    except Exception as e:
        date_published = ""
        pass


    return (first_name,last_name,page_title,website_title,date_published, date_accessed)

def chicago_compile(web_address):
    if web_address[:4] != "http": #If https:// or http:// are not included in the URL
        web_address = "http://" + web_address
    web_address = web_address.lower()
    first_name,last_name,page_title,website_title,date_published, date_accessed = citation_components(web_address)
    
    # Compiling the Citation
    if first_name != "" and last_name != "":
        citation = last_name + ", " + first_name + ". "
    else:
        citation = ""

    citation += '"' +page_title + '." ' + website_title + ", "
    if date_published != "":
        citation += date_published + ", "

    citation += web_address+ ". Accessed " + date_accessed + "."

    return citation

def apa_compile(web_address):
    if web_address[:4] != "http": #If https:// or http:// are not included in the URL
            web_address = "http://" + web_address
    web_address = web_address.lower()
    first_name,last_name,page_title,website_title,date_published, date_accessed = citation_components(web_address)

    no_author = False
    if first_name != "" and last_name != "":
        citation = last_name + ", " + first_name[0] + ". "
    else:
        citation = page_title + ' '
        no_author = True

    if date_published != "":
        citation += "(" + date_published + "). "
    else:
        citation += "(n.d). "

    if not no_author:
        citation += page_title + ". " 
        
    citation +=  "Retrieved from " + web_address
    return citation



