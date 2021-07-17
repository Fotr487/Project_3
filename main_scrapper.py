import sys
import csv
import requests as rq
from bs4 import BeautifulSoup as Bs

DIVI = "=" * 80
URL = "https://volby.cz/pls/ps2017nss/"
USER_URL = "https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ"


def name_creation():
    name = input("WHAT NAME WOULD YOU LIKE TO GIVE YOUR FILE? (WITHOUT SUFFIXES)\n")
    if "." in name:
        name = name.split(".")[0]
        return name
    else:
        return name


def get_id_name(line, lst):
    lst.append(line.find("a").string)
    lst.append(line.parent.find_all()[2].string)
    return lst


def souping(line, url):
    region_url = rq.get(url + line.find("a").attrs["href"])
    return Bs(region_url.text, "html.parser")


def voters_finder(region_result, lst):
    lst.append(region_result.find("td", {"class": "cislo", "headers": "sa2"}).string)
    lst.append(region_result.find("td", {"class": "cislo", "headers": "sa3"}).string)
    lst.append(region_result.find("td", {"class": "cislo", "headers": "sa6"}).string)
    return lst


def party_votes_finder(parties, lst):
    for line in parties:
        if not line.find("th"):
            lst.append(line.find_all("td", {"class": "cislo"})[1].string)
    return lst


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
    if "&xnumnuts=" not in link:
        if "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&x" not in link:
            print("INVALID URL. TURNING OFF. HAVE A NICE DAY...")
            sys.exit(0)

    name = name_creation()
    file = open(name + ".csv", mode="w")
    file_writer = csv.writer(file, delimiter=";")

    header = False
    scrap = rq.get(link)
    usi = Bs(scrap.text, "html.parser")
    regs = usi.find_all("td", {"class": "cislo"})

    for lini in regs:
        reg_dat = []
        reg_dat = get_id_name(lini, reg_dat)
        regs_soup = souping(lini, URL)
        reg_res = regs_soup.find(id="ps311_t1")
        reg_dat = voters_finder(region_result=reg_res, lst=reg_dat)
        parties = regs_soup.find(id="inner").find_all("tr")
        reg_dat = party_votes_finder(parties=parties, lst=reg_dat)

        if not header:
            print("ALMOST THERE")
            clmn_nm = ["ID", "NAME", "REGISTERED VOTERS", "ENVELOPES", "VALID VOTES"]
            for new_line in parties:
                if not new_line.find("th"):
                    clmn_nm.append(new_line.find_all("td")[1].string)
            file_writer.writerow(clmn_nm)
            header = True
        file_writer.writerow(reg_dat)
    file.close()
    print(f"""
{DIVI}
THE JOB IS DONE ψ(｀∇´)ψ,
{name}.csv IS READY FOR CHECKING.
I HOPE YOU WILL USE THIS DATA FOR GOOD. XD
MAY THE FORCE BE WITH YOU...""")
    sys.exit(0)


if __name__ == '__main__':
    sys.exit(main())
# Ten volný řádek se mi zde neukazuje, zkouším tohle
