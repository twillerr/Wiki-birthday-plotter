from bokeh.plotting import figure, show, output_file
from bokeh.models import Title
from collections import Counter
import wikipediaapi
from bs4 import BeautifulSoup
import requests
import sys

def get_html(x):
    #get html from url
    f = requests.get(str(x))
    y = f.text
    return y

def get_bday(html_text):
    #extract birthday (dd-mm-yyyy) from wikipedia page
    soup = BeautifulSoup(html_text, "html.parser")
    y = soup.find(class_ = "bday").string
    return y

cal =  ["January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"]

#abbreviated calendar months
cal3 =[i[0:3] for i in cal]

#-------------------------get urls, write to file------------------------

#gets dictionariy of all links on a given wiki page,
#in this case "list of famous kpop artists"
wiki_wiki = wikipediaapi.Wikipedia('en')
links = wiki_wiki.page('List_of_K-pop_artists').links

#write all urls to a file seperated by newlies,
#check if file has content first
with open("kpop_urls.txt", "r") as r:
    lns_a = len(r.readlines())
    if lns_a ==0:
        with open("kpop_urls.txt", "w") as f:
            i=1
            #sliced list to exclude non-kpop artist links
            for title in (list(links.values())[5:-15]):
                f.write(str(title.fullurl)+"\n")
                print("birthday {x} written to file".format(x=i))
                i+=1
    else:
        print("URLS file already contains data")
print("URL writning completed.")

#------------------------get bdays, write to file-------------------------


#from file containing urls, get birthday of each person and write to new file,
#checking if file has content first
with open("kpop_urls.txt", "r") as links:
    with open("kpop_birthdays", "r") as bdays:
        lns_b = len(bdays.readlines())
        if lns_b == 0:
            with open("kpop_birthdays","w") as bdays:
                i=1
                for link in links:
                    try:
                        #catch errors from pages that contain no birthday data
                        date = (get_bday(get_html(link.strip())))
                        bdays.write(date+"\n")
                        print("date {x} written to file".format(x=i))
                        i+=1
                    except:
                        print("Error: No Birthday found")
        else:
            print("birthdays file already contains data.")
print("Birthday writing completed.")

## ----------------------------- Plotting ------------------------------------

with open("kpop_birthdays", "r") as f:
    #list of months of birth of kpop idols
    months = [int(date.strip().split("-")[1]) for date in f if len(date.strip()) ==10]

#number of members per month
tally = Counter(months)
month_dict = {cal[i]:tally[i+1] for i in range(0,12)}

#file to write graph plot
output_file("kpop_idols_birthdays.html")

x_categories = cal3
x = cal3
y= list(month_dict.values())

p = figure(x_range = x_categories, title =
           "Month of birth of top {x} K-pop idols (Wikipedia)".format(x=len(months)))
p.vbar(x=x, top =y, width =0.5)

#left and right titles
p.add_layout(Title(text="Month", align = "center"), "below")
p.add_layout(Title(text="Number", align = "center"), "left")

show(p)
