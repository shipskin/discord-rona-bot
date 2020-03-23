from dotenv import load_dotenv
import os

load_dotenv()

DISCORD_CLIENT = os.getenv('DISCORD_CLIENT')

death_path = './body/div/div/div[2]/div/div/div/margin-container/full-container/div[9]/margin-container/full-container/div/div/div/div[2]/svg/g[2]/svg/text'
recovered_path = './body/div/div/div[2]/div/div/div/margin-container/full-container/div[11]/margin-container/full-container/div/div/div/div[2]/svg/g[2]/svg/text'
infected_path = './body/div/div/div[2]/div/div/div/margin-container/full-container/div[1]/margin-container/full-container/div/div/div/div[2]/svg/g[2]/svg/text'

arcgis_url = 'https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6'
