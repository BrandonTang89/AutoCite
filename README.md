# AutoCite
A Batch Citation Machine with Chicago and APA Formatting Options

AutoCite is a tool aimed at students and researchers who wish to focus less on making citations and more on writing their papers. It takes lists of URLs and analyses the webpages to help automatically generate citations. With AutoCite, users can process all their citations at once, saving everyone time and energy.

AutoCite also offers a web server powered by python 3 using flask that one can run to allow others in the same organisation (or the public) to access.

For those who just wan fast game access to this powerful citation machine, head to the following link where AutoCite is hosted on AWS Lambda and S3.
<a href=http://autocite.zapto.org>AutoCite Web</a>

If the above link died due to lack of AWS credits, try this link instead. [https://AutoCite.brandontang89.repl.co](https://AutoCite.brandontang89.repl.co)

## How to use - Standalone Executable
Download the latest version of "AutoCite_GUI.exe" and run it.

Copy & paste raw URLs that you wish to be cited into the "Raw URls" box. URLs should be separated by newline characters.
<pre>
https://www.straitstimes.com/singapore/condo-conflicts
https://www.channelnewsasia.com/news/asia/southeast-asian-leaders-meet-us-china-trade-war-asean-summit-12057538
https://blog.seedly.sg/telegram-channels-that-every-millennials-singapore-must-have/
https://stackoverflow.com/questions/5815747/beautifulsoup-getting-href
https://www.channelnewsasia.com/news/asia/southeast-asian-leaders-meet-us-china-trade-war-asean-summit-12057538
https://www.dissentmagazine.org/online_articles/can-democratic-socialism-rise-in-rural-america
</pre>

After the "Generate Citations!" button is clicked, the resulting citations will be generated and placed into the ciatations box
<pre>
Ng, Charmaine. "Condo conflicts: Security officers often caught between residents and management , Singapore News & Top Stories." The Straits Times, 03 Nov 2019, https://www.straitstimes.com/singapore/condo-conflicts. (retrieved 04 Nov 2019).
"Trade talks in balance at Southeast Asian leaders summit." CNA, 02 Nov 2019, https://www.channelnewsasia.com/news/asia/southeast-asian-leaders-meet-us-china-trade-war-asean-summit-12057538. (retrieved 04 Nov 2019).
Tan, Cherie. "Useful Telegram Channels That Every Singaporean Needs To Join." Seedly, 15 Oct 2019, https://blog.seedly.sg/telegram-channels-that-every-millennials-singapore-must-have/. (retrieved 04 Nov 2019).
"python - BeautifulSoup getting href." Stack Overflow, 28 Apr 2011, https://stackoverflow.com/questions/5815747/beautifulsoup-getting-href. (retrieved 04 Nov 2019).
"Trade talks in balance at Southeast Asian leaders summit." CNA, 02 Nov 2019, https://www.channelnewsasia.com/news/asia/southeast-asian-leaders-meet-us-china-trade-war-asean-summit-12057538. (retrieved 04 Nov 2019).
Feldblum, Sammy. "Can Democratic Socialism Rise in Rural America?." Dissentmagazine, https://www.dissentmagazine.org/online_articles/can-democratic-socialism-rise-in-rural-america. (retrieved 04 Nov 2019).
--- FINISHED ---
</pre>

## Dependencies
If you wish to make modifications to AutoCite, you require python 3.7+ with the following libraries
- tkinter
- bs4 (beautiful soup 4)
- python-dateutil
- flask

## How to use - AutoCite_Web [On Linux Servers]
1. Clone the repositary
<pre>git clone https://github.com/BrandonTang89/AutoCite.git</pre>
2. Install the necessary libraries
<pre>
sudo apt-get install guincorn3
pip3 install bs4 python-dateutil flask
</pre>
3. Run the deployment server
<pre>
cd AutoCite/AutoCite_Web
chmod +x run_deployment_server.sh
./run_deployment_server.sh
</pre>


## Limitations
Due to my bad coding and the difficulty of the task, AutoCite does not generate perfect citations, here are some known limitations
- Only a maximum of 1 author is found
- Author sometimes not found by programme
- Website title is found through URL if it is not listed in the page title
- I may have a bad understanding of how the citation should be formatted
- Some citations are just generally wonky
- Some webpages are encoded and won't work with AutoCite

Thus, AutoCite is still not as good as a manual citation job. However, if you were looking for perfect citations, you wouldn't be looking for an automated batch citation tool :)
