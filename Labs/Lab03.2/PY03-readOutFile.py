from bs4 import BeautifulSoup 
with open("https://github.com/andrewbeattycourseware/datarepresentation2021/blob/main/code/week02/carviewer2.html") as fp: 
    soup = BeautifulSoup(fp,'html.parser')

print (soup.tr)
