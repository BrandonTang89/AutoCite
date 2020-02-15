from flask import render_template
from flask import request
from flask import Flask
import json
from autocite_fns import *

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('main_page.html', title="AutoCite")


#End-Point for Each URL
@app.route('/citation', methods=['POST'])
def citation():
    citation_format = request.form['format']
    raw_url = request.form['raw_urls']

    print("Server Received Request for:", raw_url)
    if raw_url == '':
        return json.dumps({'status':'BLANK', 'generated_citations':''})
    try:
        if citation_format == "APA":
            citation_format = "apa"

        citation = generate_citation(raw_url, citation_format)
            
    except Exception as e:
        print("exception")
        citation = "Failed to cite "+ raw_url + " Error: " + str(e) + " \n"

        
    return json.dumps({'status':'OK', 'generated_citations':citation, 'id':request.form['id']})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8000', debug=True)

