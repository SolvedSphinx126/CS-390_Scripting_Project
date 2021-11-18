import requests
import re

if __name__ == '__main__':
    lastName = "Menon"
    web = requests.get("https://www.uah.edu/cgi-bin/schedule.pl")
    links = re.findall("(http://www.uah.edu/cgi-bin/schedule.pl\?file=[^\.]*\.html&segment=NDX)", web.content.decode())
    rawClasses = []
    semesters = []
    for i in range(len(links)):
        links[i] = links[i].replace(links[i][-3:], "CS")
        rawClasses.append(re.findall(".*" + lastName + ".*", requests.get(links[i]).content.decode()))
    for clas in rawClasses:
        semesters.append(re.findall("((\S+ )+\S+(?= +((\d\.\d)|(\.\d))))", str(clas).replace(',', '\n')))

    for semester in semesters:
        for session in semester:
            print(session[0])