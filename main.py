import requests #import the requests package
import re       #import the regex package

if __name__ == '__main__':
    lastName = input("Enter instructor last name: ")                #prompt for a teacher's last name (ex. Zhang)
    web = requests.get("https://www.uah.edu/cgi-bin/schedule.pl")   #get content of the page that lists each of the semesters that need to be checked
    links = re.findall("(http://www.uah.edu/cgi-bin/schedule.pl\?file=[^\.]*\.html&segment=NDX)", web.content.decode()) #get the list of those valid links
    for i in range(len(links)):
        links[i] = links[i].replace(links[i][-3:], "CS")    #for each of the links, select the CS dept
        print(links[i][44:52])                              #label each semester
        for session in re.findall(".*" + lastName + ".*", requests.get(links[i]).content.decode()): #select each class that is taught by the requested teacher
            print(session)                                                                          #and print it
