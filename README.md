# insta_scraper
 Scrapes bio-data of users to check which brands are promoted more often than others by similar type of instagram pages.

Bot 1 - Gets usernames of following of a instagram page from Profile links File and store them in users' 

Bot 2 - Opens instagram profile of users from users' following list and copies their bio data in a column of an excel file in row with their username and profile link and gets all mentions and links in seperate columns, if there's linktree, milkshake, beacons, zezam, bio site links are there then they are opened and all links in those are extracted in the same row of the user.

Bot 3 - This bot cleans the excel file by removing unnecessary links and emails from all columns except from bio data column, later it removes the rows which have no links and no mentions.

Bot 4 - This bot gets all sub-domain + root domains from the links and rank them in decreasing order of occurances in the data and saves it in same excel file in the next column available column which is 16th.
