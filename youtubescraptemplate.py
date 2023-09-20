# youtubescrape.py
# description: A simple webscrape of a youtube channel (url) using selenium and pandas
# author: pcostjr
# created: 9.19.2023

# import libraries
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

# handles web navigation.
url = 'CHANNEL URL HERE'
driver = webdriver.Chrome()
driver.get(url)

# this will be the list we ultimately put our entries into
video_list = []
