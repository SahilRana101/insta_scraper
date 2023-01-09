from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time
import random


# sleep to wait for page loading
def sleeper():
    time.sleep(random.randrange(3, 5))


# Logging into Instagram
insta_accounts = []
insta_accounts_file = open("..\\resources\\insta accounts.txt", "r")
for i in insta_accounts_file:
    j = i
    if i[-1] == "\n":
        j = j[:-1]
    insta_accounts.append(j.split(" "))

for account in insta_accounts:
    chromedriver_autoinstaller.install()
    browser = webdriver.Chrome()
    browser.implicitly_wait(1)
    sleeper()
    browser.get('https://www.instagram.com/')
    sleeper()
    username_input = browser.find_element(By.CSS_SELECTOR, "input[name='username']")
    password_input = browser.find_element(By.CSS_SELECTOR, "input[name='password']")
    username_input.send_keys(account[0])
    password_input.send_keys(account[1])
    login_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    sleeper()

    # Opening files
    profile_links_file = open("..\\resources\\profile links.txt", "r")
    done_with = open("..\\resources\\done with profile links.txt", "r+")

    # making list of links from profile links file
    profile_links_list = []
    for i in profile_links_file:
        if i[-1] == "\n":
            profile_links_list.append(i[:-1])
        else:
            profile_links_list.append(i)

    # making done with profile links list
    done_with_list = []
    for i in done_with:
        if i[-1] == "\n":
            done_with_list.append(i[:-1])
        else:
            done_with_list.append(i)
    done_with.read()

    # Iterating links and getting their following
    for i in profile_links_list:
        if i not in done_with_list:
            browser.get(i)
            sleeper()
            sleeper()
            count = browser.find_elements(By.CLASS_NAME, "_ac2a")[2].text
            count = count.replace(",", "")
            print(count)
            browser.get(i+"following/")
            sleeper()
            following_list = []
            count_1 = 0
            count_2 = 0
            flag = True

            # making done with user's following list

            user_following_file = open("..\\resources\\users' following list.txt", "r+")

            done_with_user_following_list = []
            for o in user_following_file:
                if o[-1] == "\n":
                    done_with_user_following_list.append(o[:-1])
                else:
                    done_with_user_following_list.append(o)
            user_following_file.read()

            # Getting their following
            while count_1 <= int(count):
                following = browser.find_elements(By.CLASS_NAME, "_ab8y")
                print(count_1)
                if not flag:
                    count_2 += 1
                if count_2 == 4:
                    break
                flag = False
                # Scrolling following list to get all the following
                for j in range(count_1, len(following)):
                    browser.execute_script("arguments[0].scrollIntoView();", following[j])
                    count_1 += 1
                    following_list.append(following[j].text)
                    flag = True
                sleeper()

            # Adding link to done with file
            done_with.write(i + "\n")

            # Adding the following to final file of all following
            for j in following_list:
                if j not in done_with_user_following_list and j != "Verified":
                    user_following_file.write(j + "\n")
            user_following_file.close()

    profile_links_file.close()
    done_with.close()

browser.close()
