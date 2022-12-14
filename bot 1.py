from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random


# sleep to wait for page loading
def sleeper():
    time.sleep(random.randrange(3, 5))


# Logging into Instagram
browser = webdriver.Chrome(r"\chromedriver")
browser.implicitly_wait(1)
browser.get('https://www.instagram.com/')
sleeper()
username_input = browser.find_element(By.CSS_SELECTOR, "input[name='username']")
password_input = browser.find_element(By.CSS_SELECTOR, "input[name='password']")
sleeper()
username_input.send_keys("macleodganjtrip@gmail.com")
password_input.send_keys("selenium@1")
login_button = browser.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()
sleeper()

print(browser.window_handles)

# Opening files
profile_links_file = open(r"profile links.txt", "r")
user_following_file = open(r"user's following list.txt", "r+")
done_with = open(r"done with profile links.txt", "r+")

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

# making done with user's following list
done_with_user_following_list = []
for i in user_following_file:
    if i[-1] == "\n":
        done_with_user_following_list.append(i[:-1])
    else:
        done_with_user_following_list.append(i)

# Iterating links and getting their following
for i in profile_links_list:
    if i not in done_with_list:
        browser.get(i)
        sleeper()
        # following_button = browser.find_element(By.CLASS_NAME, "_aacl")
        # sleeper()
        count = browser.find_elements(By.CLASS_NAME, "_ac2a")[2].text
        count = count.replace(",", "")
        print(count)
        browser.get(i+"following/")
        sleeper()
        following_list = []
        count_1 = 0
        count_2 = 0
        prev_count = 0

        # Getting their following
        while count_1 <= int(count):
            following = browser.find_elements(By.CLASS_NAME, "_ab8y")
            if count_1 == prev_count:
                count_2 += 1
            if count_2 == 4:
                break

            # Scrolling following list to get all the following
            for j in range(count_1, len(following)):
                browser.execute_script("arguments[0].scrollIntoView();", following[j])
                count_1 += 1
                print(following[j].text)
                following_list.append(following[j].text)
            prev_count = count_1
            sleeper()

        # Adding link to done with file
        done_with.write(i + "\n")

        # Adding the following to final file of all following
        print(following_list)
        for j in following_list:
            if j not in done_with_user_following_list:
                user_following_file.write(j)
                user_following_file.write("\n")

browser.close()
