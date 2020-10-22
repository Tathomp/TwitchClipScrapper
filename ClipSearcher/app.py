from twitch import TwitchClient
import glob
import os
from urllib import request
import requests
import pprint

from lxml import html

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

clientId = "rdyd9n2lahnrv4i7zho7kgy2nl8na2"
client = TwitchClient(client_id=clientId)

channel_names = ["dogdog",
                 "ludwig",
                 "moistcr1tikal",
                 "hasanabi"
                 ]

driver = webdriver.Chrome(ChromeDriverManager().install())

for cn in channel_names:
    c = client.clips.get_top(channel=cn, limit=5, period="day", trending=True)
    for slug in c:
        url = slug['url']
        driver.get(url)
        elements = driver.find_elements_by_tag_name('video')
        vid_url = elements[0].get_attribute("src")
        print(vid_url)
        driver.get(vid_url)

