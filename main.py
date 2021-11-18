import requests
import re


def print_hi(name):
    print("Hi, {0}".format(name))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    lastName = "Zhang"
    linkPattern = "(http://www.uah.edu/cgi-bin/schedule.pl\?file=[^\.]*\.html&segment=NDX)"
    namePattern = ".*" + lastName + ".*"
    web = requests.get("https://www.uah.edu/cgi-bin/schedule.pl")
    links = re.findall(linkPattern, web.content.decode())
    classes = []
    for i in range(len(links)):
        links[i] = links[i].replace(links[i][-3:], "CS")
        classes.append(re.findall(namePattern, requests.get(links[i]).content.decode()))
    for clas in classes:
        print(str(clas))