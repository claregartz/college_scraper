
from bs4 import BeautifulSoup
import requests
import csv
page_to_scrape = requests.get("https://www.collegedata.com/college-search")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
 
schools = soup.findAll("div", attrs ={"class": "CollegeCard_header__QmhMe"})

locations = soup.findAll("div", attrs={"class": "CollegeCard_subheader__227sr"})

file = open("college_data_practice.csv", "w")
writer = csv.writer(file)

writer.writerow(["Schools", "Locations"])

for school, location in zip(schools, locations):
    print(school.text + " - " + location.text)
    writer.writerow([school.text, location.text])
file.close()



