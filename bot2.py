from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import xlsxwriter


def sleeper():
    time.sleep(random.randrange(3, 5))


# function to make bot type like a human
def virtual_human(key, element):
    for j in key:
        element.send_keys(j)
        time.sleep(float("{:.2f}".format(random.uniform(0.1, 0.4))))


# Logging in
browser = webdriver.Chrome(r"C:\Users\sahil\PycharmProjects\insta_scrapper\chromedriver")
browser.implicitly_wait(1)
browser.get('https://www.instagram.com/mr.ace_hole/')
sleeper()

bio_data = browser.find_element(By.CLASS_NAME, "_aa_c")
a = bio_data.text.split()
f = open("biodata.txt", "w", encoding="utf-8")
for i in range(len(a)):
    if "@" in a[i] or "." and "/" in a[i]:
        f.write(a[i])
        f.write("\n")

book = xlsxwriter.Workbook('Example2.xlsx')
sheet = book.add_worksheet()

# Rows and columns are zero indexed.
row = 0
column = 0
links_and_mentions = ""
sheet.write(0, 0, "mr.ace_hole")

for i in range(len(a)):
    if "@" in a[i] and a[i].index("@") == 0:
        links_and_mentions += str(a[i])
        links_and_mentions += ", "
    if "." and "/" in a[i]:
        links_and_mentions += str(a[i])
        links_and_mentions += ", "
links_and_mentions = links_and_mentions[:-2]

sheet.write(0, 1, links_and_mentions)

book.close()