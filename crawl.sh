#!/bin/sh

# This is to make the python file executable
chmod u+x main.py

echo "Please Enter a Valid URL or Press CTRL+C to Exit: "
echo "Example: www.cheatcc.com "
read url_input 

python ./main.py "$url_input"