#!/bin/bash
python3 -m venv autocite_env
source autocite_env/bin/activate
pip3 install flask bs4 python-dateutil pyinstaller
pyinstaller --onefile AutoCite_GUI.pyw 
rm -r build

echo "#### New Executable in dist/ ####"
