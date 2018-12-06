import requests
import sys

print("WEBSITE DOWNLOADER")
url = input("Enter or Paste the URL: ")
name = input("Enter File Name: ")


url.strip()

if url.find("https") or url.find("http") or url.find(".com") or url.find(".org") or url.find(".in") or url.find(".edu"):
    pass
else:
    print("INVALID URL")
    sys.exit()


def crawl(url):

    try:
        print("url -> " + url)
        sourcecode = requests.get(url)
        plaintext = sourcecode.text
        filename=str(name)+".html"
        fx = open(filename, "w")
        fx.write("<!-- PIYUSH GARG --> \n")
        fx.write(plaintext)
        fx.close()
        print(filename + " File Successfully Created")

    except:
        print("An exception occurred or Invalid URL")




crawl(url)
