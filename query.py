from googlesearch import search
import requests
import webbrowser
def find(question):
      url=next(search(question))
      webbrowser.open(url)
      
if __name__=="__main__":
         find("apple")
