import requests
import re


def print_hi(name):
    print("Hi, {0}".format(name))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pattern = "(http://www.uah.edu/cgi-bin/schedule.pl\?file=[^\.]*\.html&segment=NDX)"
    web = requests.get("https://www.uah.edu/cgi-bin/schedule.pl")
    links = re.findall(pattern, web.content.decode())
    for link in links:
        link = link.replace(link[-3:],"CS")
    print(links)