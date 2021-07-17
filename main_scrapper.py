import sys
import csv
import requests as req
from bs4 import BeautifulSoup as BS

DIVI = "=" * 80
URL = "https://volby.cz/pls/ps2017nss/"
USER_URL = "https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ"
BS4_ES = "html.parser"


def name_creation():
    name = input("WHAT NAME WOULD YOU LIKE TO GIVE YOUR FILE? (WITHOUT SUFFIXES)\n")
    if "." in name:
        name = name.split(".")[0]
        return name
    else:
        return name

def file_use(name):
    file = open(name + ".csv", mode="w")
    file_writer = csv.writer(file, delimiter="|")

def names_id(ln, lst):
    lst.append(ln.find("a").string)
    lst.append(ln.parent.find_all()[2].string)
    return lst

def souping(ln, link):
    rg_url = req.get(link + ln.find("a").attrs["href"])
    return BS(rg_url.text, BS4_ES)

def voters_finder(region_result, lst):
    sa = ["sa2", "sa3", "sa6"]
    for s in sa:
        lst.append(region_result.find("td", {"class": "cislo", "headers": f"{s}"}))
    return lst

def party_votes_finder(parties, lst):
    pass

def main():
    print(f"""
{DIVI}
WELCOME TO THE ELECTIONS SCRAPPER.
I WILL SHOW YOU THE RESULTS OF THE 2017 ELECTIONS BY REGION.
OF COURSE IF YOU GIVE ME THE RIGHT DATA.(～￣▽￣)～
{DIVI}
VISIT THIS PAGE: {USER_URL}
THERE YOU HAVE TO CHOOSE REGION BY CLICKING ON 'X' IN COLUMN TITLED 'VYBER OBCE'
{DIVI}
    """)
    link = input("PASTE THE URL YOU HAVE COPIED FROM THAT SITE HERE:\n")
    if "&xnumnuts=" not in link and "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&x" not in link:
        print("INVALID URL. TURNING OFF. HAVE A NICE DAY...")
        sys.exit(0)
    name = name_creation()
    file_use(name=name)
    scp = req.get(link)
    usi = BS(scp.text, BS4_ES)
    regs = usi.find_all("td", {"class": "cislo"})
    header = False

    for lini in regs:
        regs_dat = []
        regs_dat = names_id(ln=lini, lst=regs_dat)
        regs_soup = souping(ln=lini, link=link)
        regs_res = regs_soup.find(id="ps311_6_t1")



name_creation()
#main()