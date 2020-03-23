import requests
import discord
from lxml import html, etree
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options

from settings import (
    DISCORD_CLIENT,
    death_path,
    recovered_path,
    infected_path,
    arcgis_url
)

client = discord.Client()

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.binary_location = '/bin/google-chrome'
driver = webdriver.Chrome(options=chrome_options)

def scrape_arcgis():
    try:
        driver.get(arcgis_url)
        sleep(5)
        html_source = driver.page_source
        dom = etree.HTML(html_source)

        deaths = dom.xpath(death_path)[0].text
        recovered = dom.xpath(recovered_path)[0].text
        infected = dom.xpath(infected_path)[0].text

        text = f':thermometer_face: : {infected}\n:grinning: : {recovered},\n:skull: {deaths}'
        return text
    except Exception as e:
        print('Exception: ', e)
        return False

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        print('client user: ', client.user)
        return

    bot_word = '$rona'
    if message.content.startswith(bot_word):
        text = scrape_arcgis()
        print(text)
        if not text:
            text = "woops something went wrong"
        
        await message.channel.send(text)



client.run(DISCORD_CLIENT)
