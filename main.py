import scraper
import feedparser
import pandas as pd
import glob
from string import punctuation


keywords = ["startup", "venture", "alpha", "beta", "test", "launch", "release"]

f = open("links.txt","r")

ip_watchdog = ["div.text","h1","https://news.google.com/articles/CBMif2h0dHA6Ly93d3cuaXB3YXRjaGRvZy5jb20vMjAxOC8wOS8xNi9zbWFydGZsYXNoLWZpbGVzLXBldGl0aW9uLXdyaXQtc3VwcmVtZS1jb3VydC1jaGFsbGVuZ2UtcHRhYi1hcHBvaW50bWVudHMtY2xhdXNlL2lkPTEwMTM2Ni_SAQA?hl=en-US&gl=US&ceid=US%3Aen","https://news.google.com/articles/CBMiRGh0dHA6Ly93d3cuaXB3YXRjaGRvZy5jb20vMjAxOC8wOS8xNy9jYXBpdG9sLWhpbGwtcm91bmR1cC9pZD0xMDE0MzEv0gEA?hl=en-US&gl=US&ceid=US%3Aen", "https://news.google.com/articles/CBMiamh0dHBzOi8vd3d3Lmlwd2F0Y2hkb2cuY29tLzIwMTQvMDcvMjUvaWdub3JhbmNlLWlzLW5vdC1ibGlzcy1hbGljZS1jb3JwLXYtY2xzLWJhbmstaW50ZXJuYXRpb25hbC9pZD01MDUxNy_SAQA?hl=en-US&gl=US&ceid=US%3Aen"]

#Needs file

mondaq = ["https://news.google.com/articles/CBMiYmh0dHA6Ly93d3cubW9uZGFxLmNvbS9pbmRpYS94LzczMTAwOC9QYXRlbnQvQ2FzZStBbmFseXNpcytBbGljZStDb3JwK1YrQ2xzK0JhbmsrMTM0K1MrQ3QrMjM0NysyMDE00gEA?hl=en-US&gl=US&ceid=US%3Aen"] 


canadian_lawyer = ['article',"https://news.google.com/articles/CBMid2h0dHBzOi8vd3d3LmNhbmFkaWFubGF3eWVybWFnLmNvbS9hcnRpY2xlL3BhdGVudC1hbmQtYnVzaW5lc3Mtb3Bwb3J0dW5pdGllcy1pbi10aGUtd29ybGQtb2YtZGlnaXRhbC10ZWNobm9sb2dpZXMtMTYxMTcv0gEA?hl=en-US&gl=US&ceid=US%3Aen"]

law360 = ["https://news.google.com/articles/CBMiXmh0dHBzOi8vd3d3LmxhdzM2MC5jb20vYXJ0aWNsZXMvMTA4MTYwMy9mZWQtY2lyYy11cGhvbGRzLWF4LW9mLW9ubGluZS1zZWN1cml0eS1pcC1pbi11c2FhLWNhc2XSAXJodHRwczovL3d3dy1sYXczNjAtY29tLmNkbi5hbXBwcm9qZWN0Lm9yZy92L3Mvd3d3LmxhdzM2MC5jb20vYW1wL2FydGljbGVzLzEwODE2MDM_YW1wX2pzX3Y9MC4xI3dlYnZpZXc9MSZjYXA9c3dpcGU?hl=en-US&gl=US&ceid=US%3Aen","https://news.google.com/articles/CBMiUWh0dHBzOi8vd3d3LmxhdzM2MC5jb20vYXJ0aWNsZXMvMTA0MjIxMi9hbGljZS1wcm9vZmluZy15b3VyLXBhdGVudC1zcGVjaWZpY2F0aW9uc9IBcmh0dHBzOi8vd3d3LWxhdzM2MC1jb20uY2RuLmFtcHByb2plY3Qub3JnL3Yvcy93d3cubGF3MzYwLmNvbS9hbXAvYXJ0aWNsZXMvMTA0MjIxMj9hbXBfanNfdj0wLjEjd2Vidmlldz0xJmNhcD1zd2lwZQ?hl=en-US&gl=US&ceid=US%3Aen"]

lexology = ["https://news.google.com/articles/CBMiU2h0dHBzOi8vd3d3LmxleG9sb2d5LmNvbS9saWJyYXJ5L2RldGFpbC5hc3B4P2c9ZTc5MmMxMDItMzMyMi00YWUzLWE5MzEtMzUzYzkxYTlhN2M00gEA?hl=en-US&gl=US&ceid=US%3Aen","https://news.google.com/articles/CBMiU2h0dHBzOi8vd3d3LmxleG9sb2d5LmNvbS9saWJyYXJ5L2RldGFpbC5hc3B4P2c9MDBlZTQzZjMtZWE1OS00OGRlLTk0ZjAtYjQzZmI3OGUxMjQ30gEA?hl=en-US&gl=US&ceid=US%3Aen", "https://news.google.com/articles/CBMiU2h0dHBzOi8vd3d3LmxleG9sb2d5LmNvbS9saWJyYXJ5L2RldGFpbC5hc3B4P2c9Zjk1MDkxZTctMTU4Ny00ZjU1LWIzYzMtMDFiZTkwYWQ1YzI10gEA?hl=en-US&gl=US&ceid=US%3Aen"]


patentdocs = ["div.entry-body", "h3.entry-header","https://news.google.com/articles/CBMiXWh0dHA6Ly93d3cucGF0ZW50ZG9jcy5vcmcvMjAxNC8wNi9zdXByZW1lLWNvdXJ0LWlzc3Vlcy1kZWNpc2lvbi1pbi1hbGljZS1jb3JwLXYtY2xzLWJhbmsuaHRtbNIBAA?hl=en-US&gl=US&ceid=US%3Aen"]

fortune = ["div#article-body", "h1", "http://fortune.com/2014/06/19/supreme-court-limits-the-scope-of-software-patents/"]

links = {"ipwatchdog": ip_watchdog, "mondaq": mondaq, "canadianlawyer" : canadian_lawyer, "law360" : law360, "lexology": lexology, "patentdocs" : patentdocs, "fortune": fortune}

arr_links = f.read().split(',')
sources = []

for link in arr_links:
    try:
        sources.append((link.split('//')[1].strip("www.").split('.')[0], link))
    except:
        print "Bad Link:" + link
    
sources_unique = set(sources)

for source in sources:
    if source[0] in links:
        links[source[0]].append(source[1])
    else:
        links[source[0]] = [source[1]]

links["thehill"] = ["div#content", "h1"] + links["thehill"]
links["jdsupra"] = ["div#html-view-content", "div#DocumentHeaderPanel"] + links["jdsupra"]
links["ippropatents"] = ["div#article", "h1"] + links["ippropatents"]
links["inventorsdigest"] = ["div.post-content", "h1"] + links["inventorsdigest"]
links["abovethelaw"] = ["div.content", "h1"] + links["abovethelaw"]
links["reuters"] = ["div.StandardArticleBody_body", "h1"] + links["reuters"]
links["jurist"] = ["div.content","h3"] + links["jurist"]
links["techcrunch"] = ["div.article-content", "h1"] + links["techcrunch"]
links["eff"] = ["div.field__items", "h1"] + links["eff"]
links["nytimes"] = ["div.css-18sbwfn.StoryBodyCompanionColumn", 'h1'] + links["nytimes"]
links['patentlyo'] = ["div.entry-content", "h1.entry-title"] + links['patentlyo']
links['searchengineland'] = ["p", "h1"] + links['searchengineland']
links["scotusblog"] = ["div.post-content", "h1"] + links["scotusblog"]
links["newsclick"] = ["div.field.field--name-body", "div.article-subtitle"] + links["newsclick"]
links["internationallawoffice"] = ["div#textBody", "h1"] + links["internationallawoffice"]
links["forbes"] = ["article-body-container", "h1"] + links["forbes"]
links["orldipreview"] = ["div.content", "h1"] + links["orldipreview"]

links["mondaq"] = ["div#articlebody","h1"] + links["mondaq"]
links["law360"] = ["div#PrintBody","h2"] + links["law360"]
links["natlawreview"] = ["div.print-content", "h1"] + links["natlawreview"]
links["lexology"] = ["div.gated-content", "h1"] + links["lexology"]

"""
for entry in links:
    print entry + "\t" + str(links[entry]) + "\n"
    
    """


data = pd.DataFrame(columns=["Link","Score"])

def get_text_links():
    for entry in links:
        arr = links[entry]
        if "//" not in arr[0]:
            i = 0
            while i + 2 < len(arr):
                try: 
                    title = scraper.scrape(arr[i+2],arr[1])[0].strip().encode('ascii', 'ignore') + " " + entry
                except:
                    print arr
                    print i + 2
                
                data.loc[title] = ["",0]
                data.loc[title]["Link"] = arr[i+2]
                txts = scraper.scrape(arr[i+2], arr[0])

                for txt in txts:
                    words = txt.split()
                    for w in words:
                        w = ''.join(c for c in w if c not in punctuation)
                        if w.lower() in keywords:
                            data.loc[title]["Score"] += 1
                i += 1
        else:
            print entry
            
def get_text_files():
    paths = glob.glob('files/*/*')
    for f in paths:
        source = f.split('/')[1]
        title = scraper.scrape_file(f,links[source][1])[0].strip().encode('ascii', 'ignore') + ' ' + source
        data.loc[title] = ["",0]
        for s in ["lexology","natlawreview"]:
            if source == s:
                for link in links[s]:
                    if "//" in link:
                        t = scraper.scrape(link, links[s][1])[0].strip().encode('ascii', 'ignore')
                        if t[:10].lower() in title.lower():
                            data.loc[title]['Link'] = link
                            break
        if source == "law360":
            for link in links["law360"]:
                if "//" in link:
                    t = scraper.scrape(link,"h1")[0].strip().encode('ascii', 'ignore')
                    if t[:10].lower() in title.lower():
                        data.loc[title]['Link'] = link
                        break
            
        txts = scraper.scrape_file(f, links[source][0])
        for txt in txts:
            words = txt.split()
            for w in words:
                w = ''.join(c for c in w if c not in punctuation)
                if w.lower() in keywords:
                    data.loc[title]["Score"] += 1

def get_text():
    get_text_links()
    get_text_files()
            
    data.to_csv("results_final.csv")
            


get_text()
