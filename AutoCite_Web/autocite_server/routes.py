from flask import render_template
from flask import request
import json
from autocite_server import app
from autocite_fns import *
@app.route('/')
def index():
    return render_template('main_page.html', title="AutoCite")


#End-Point for Each URL
@app.route('/citation', methods=['POST'])
def citation():
    citation_format = request.form['format']
    raw_url = request.form['raw_urls']

    print(raw_url)
    if raw_url == '':
        return json.dumps({'status':'BLANK', 'generated_citations':''})
    try:
        if citation_format == "APA":
            citation = apa_compile(raw_url)+"\n"
        else:
            citation =  chicago_compile(raw_url)+"\n"
            
    except Exception as e:
        print("exception")
        citation = "Failed to cite "+ raw_url + " Error: " + str(e) + " \n"

        
    return json.dumps({'status':'OK', 'generated_citations':citation, 'id':request.form['id']})

