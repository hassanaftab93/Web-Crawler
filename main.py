from ast import Break
import functions as crawler
import sys
import os

url = sys.argv[1]

if url!="":
    urlLink = "https://"+url+"/"
    print("Website URL: ",urlLink)
    crawler.crawl(urlLink,url,1)

elif url=="":
    os.system("sh crawl.sh")