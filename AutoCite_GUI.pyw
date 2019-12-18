# Batch Citation Machine GUI
import re, datetime, urllib.request
import tkinter.scrolledtext as scrolledtext
from tkinter import *
from bs4 import BeautifulSoup
from dateutil import parser


def citation_components(web_address):
    
    req = urllib.request.Request(web_address, headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'})
    response = urllib.request.urlopen(req)
    html = response.read()

    soup = BeautifulSoup(html, 'html.parser')

    # Page Title from <title> tag | Website Title from <title> tag or from URL
    title_text = str(soup.title.contents[0]) # String Slice Removes <title> and </title>
    title_segments = title_text.split(" - ")
    
    if len(title_segments) > 1: # If website title coems after "-" in page title
        website_title = title_segments[-1]
        page_title = " - "
        page_title = page_title.join(title_segments[:-1])

    else:
        website_title = re.search(r"([^.\/]+?)(?:\.(?:sg|net|com|org|gov|edu|int|eu|us))+",web_address).group(1) # Captures the last string between .DOMAIN and the . in front of that
        website_title = website_title.capitalize() # Capitalises the first letter of the string
        page_title = title_text


    # Searches for Authors via href with "author"
    try:
        for a in soup.find_all('a', href=True): # Find first author
            if "author" in a['href']:
                # print ("Author URL", a['href'])
                author_path = a['href']
                author_name = re.search(r"\/([^\/]+)$", author_path).group(1)
                author_name = author_name.split("-")
    
        first_name = author_name[0].capitalize()
        last_name = author_name[-1].capitalize()
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

def generate_citations():
    citation_box.delete('1.0', END)
    raw_urls = raw_box.get("1.0", END)

    raw_urls = raw_urls.split("\n")
    # print(raw_urls)
    
    for url in raw_urls:
        print(url)
        if url == '':
            continue

        print(citation_format.get())
        if citation_format.get() == "APA":
            citation_box.insert(END, apa_compile(url)+"\n")
        else:
            citation_box.insert(END, chicago_compile(url)+"\n")
            
            
        citation_box.see(END)
        citation_box.grid(row=0, column=0, sticky=E+W+N+S)
        
        window.update()
    
    citation_box.insert(END, "--- FINISHED ---")
    citation_box.see(END)
    citation_box.grid(row=0, column=0, sticky=E+W+N+S)
    
    
window = Tk()
window.geometry('1000x700')
window.title("AutoCite: Batch Citation Programme - BrandonTang89")

# Frame for radio buttons
button_frame = Frame(window)
button_frame.grid(row=0, column=0, padx=10, pady=10, sticky=W+N)
button_frame.rowconfigure(0, weight=1)
button_frame.columnconfigure(0, weight=1)

radio_label = Label(button_frame, text="Citation Format: ", font=("consolas",15))
radio_label.grid(row=0, column=0)

citation_format = StringVar()
citation_format.set("chicago") #Default is chicago
apa_button = Radiobutton(button_frame, text="APA", padx=20, variable=citation_format, value="APA", font=("consolas",15))
apa_button.grid(row=0, column=2)

chicago_button = Radiobutton(button_frame, text="Chicago", padx=20, variable=citation_format, value="chicago", font=("consolas",15))
chicago_button.grid(row=0, column=1)

# Frame for RAW URLS
raw_frame = LabelFrame(window, text="Raw URLs", padx=5, pady=5, font=("consolas",15))
raw_frame.grid(row=1, column=0, padx=10, pady=10, sticky=E+W+N+S)

raw_frame.rowconfigure(0, weight=1)
raw_frame.columnconfigure(0, weight=1)

raw_box = scrolledtext.ScrolledText(raw_frame, width=80, height=15, font="consolas")

#raw_box.insert(END, '''
#https://www.straitstimes.com/singapore/condo-conflicts
#https://www.channelnewsasia.com/news/asia/southeast-asian-leaders-meet-us-china-trade-war-asean-summit-12057538
#https://blog.seedly.sg/telegram-channels-that-every-millennials-singapore-must-have/
#https://stackoverflow.com/questions/5815747/beautifulsoup-getting-href
#https://www.channelnewsasia.com/news/asia/southeast-asian-leaders-meet-us-china-trade-war-asean-summit-12057538
#https://www.dissentmagazine.org/online_articles/can-democratic-socialism-rise-in-rural-america")
#''')

raw_box.grid(row=0, column=0,sticky=E+W+N+S)


# Frame for Button
cite_frame = Frame(window)
cite_frame.grid(row=1, column=2, padx=10, pady=20, sticky=E+W+N+S)

cite_frame.rowconfigure(0, weight=1)
cite_frame.columnconfigure(0, weight=1)

cite_button = Button(cite_frame, text="Generate \n Citations!", command=generate_citations, font=("consolas",15))
cite_button.grid(row=0, column=0, sticky=N+E+W+S)

# Frame for Citations
citation_frame = LabelFrame(window, text="Citations", padx=5, pady=5, font=("consolas",15))
citation_frame.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky=E+W+N+S)

window.columnconfigure(0, weight=1)
window.rowconfigure(1, weight=1)

citation_frame.rowconfigure(0, weight=1)
citation_frame.columnconfigure(0, weight=1)

citation_box = scrolledtext.ScrolledText(citation_frame, width=80, height=17, font="consolas")
citation_box.grid(row=0, column=0,   sticky=E+W+N+S)

window.mainloop()

