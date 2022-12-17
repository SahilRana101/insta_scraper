from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import xlsxwriter


def sleeper():
    time.sleep(random.randrange(3, 5))


browser = webdriver.Chrome(r"\chromedriver")
browser.implicitly_wait(1)
sleeper()


# Logging into Instagram
browser.get('https://www.instagram.com/')
sleeper()
username_input = browser.find_element(By.CSS_SELECTOR, "input[name='username']")
password_input = browser.find_element(By.CSS_SELECTOR, "input[name='password']")
username_input.send_keys("macleodganjtrip@gmail.com")
password_input.send_keys("selenium@1")
login_button = browser.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()
sleeper()


# Opening files
user_following_file = open(r"users' following list.txt", "r")
done_with = open(r"done with users' following list.txt", "r+")
extra_file = open(r"Extra file.txt", "r")

# Excel file number set
count = 0
for i in extra_file:
    count = i

# Opening Excel file and creating a sheet
book = xlsxwriter.Workbook('Bio data ' + count + '.xlsx')
sheet = book.add_worksheet()

# closing and reopening extra file to write to it
extra_file.close()
extra_file = open(r"Extra file.txt", "w")
extra_file.write(str(int(count)+1))

# making user's following list
user_following_list = []
for i in user_following_file:
    if i[-1] == "\n":
        user_following_list.append(i[:-1])
    else:
        user_following_list.append(i)

# making done with user's following list
done_with_user_following_list = []
for i in done_with:
    if i[-1] == "\n":
        done_with_user_following_list.append(i[:-1])
    else:
        done_with_user_following_list.append(i)


# row and column set
row = 0
column = 0


# iterating following list
for i in user_following_list:
    if i not in done_with_user_following_list:
        browser.get("https://www.instagram.com/" + i + "/")
        sleeper()
        sleeper()
        bio_data = browser.find_element(By.CLASS_NAME, "_aa_c")
        sheet.write(row, column, i)
        sheet.write(row, column + 1, "https://www.instagram.com/" + i + "/")
        sheet.write(row, column + 2, bio_data.text)
        bio_data_tokens = bio_data.text.split()

        links = ""
        mentions = ""
        count_1 = 0
        count_2 = 0

        # iterate bio data tokens and find links and mentions
        for j in range(len(bio_data_tokens)):
            if "@" in bio_data_tokens[j] and bio_data_tokens[j].index("@") == 0:
                mentions += str(bio_data_tokens[j])
                mentions += ", "
                count_1 = 1
            if "." and "/" in bio_data_tokens[j] or bio_data_tokens[j].endswith(".com") or bio_data_tokens[j].\
                    endswith(".in") or bio_data_tokens[j].endswith(".org") or bio_data_tokens[j].endswith(".net") or \
                    bio_data_tokens[j].endswith(".info") or bio_data_tokens[j].endswith(".biz"):
                links += str(bio_data_tokens[j])
                links += ", "
                count_2 = 1
        links = links[:-2]
        mentions = mentions[:-2]

        sheet.write(row, column + 3, mentions)
        sheet.write(row, column + 4, links)
        done_with_user_following_list.append(i)
        row += 1


# writing done with usernames to done with FILE
for i in done_with_user_following_list:
    done_with.write(i + "\n")

user_following_file.close()
done_with.close()
extra_file.close()

book.close()
