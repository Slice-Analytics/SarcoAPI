import os 
from fastapi import FastAPI
import requests
import json
from dotenv import load_dotenv 

load_dotenv()

app = FastAPI()

@app.get("/")
async def circulatingSupply():
    dune_api_key = os.getenv('DUNE_API_KEY') 
    if dune_api_key:
        url = f'https://api.dune.com/api/v1/query/2771660/results?api_key={dune_api_key}'
        response_API = requests.get(url)
        json_response = response_API.json()
        circulating_supply = json_response['result']['rows'][0]['balance']
    else:
        print("API key not found.")
    return circulating_supply