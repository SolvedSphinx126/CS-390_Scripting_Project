import requests
import re

if __name__ == '__main__':
    lastName = input("Enter instructor last name: ")
    web = requests.get("https://www.uah.edu/cgi-bin/schedule.pl")
    links = re.findall("(http://www.uah.edu/cgi-bin/schedule.pl\?file=[^\.]*\.html&segment=NDX)", web.content.decode())
    for i in range(len(links)):
        links[i] = links[i].replace(links[i][-3:], "CS")
        print(links[i][44:52])
        for session in re.findall(".*" + lastName + ".*", requests.get(links[i]).content.decode()):
            print(session)
