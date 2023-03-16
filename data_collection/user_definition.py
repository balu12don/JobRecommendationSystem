from datetime import date, datetime, timedelta
import os
import json
import configparser

today = date.today()
yesterday = date.today() - timedelta(days=1)
two_days_ago = date.today() - timedelta(days=4)
three_days_ago = date.today() - timedelta(days=5) 

x_rapidapi_key = '1b1cd853e0msh1849b1463bbe964p15df40jsn2fa6a5d956ef'
x_rapidapi_host = 'jsearch.p.rapidapi.com'
query = 'data science jobs in california'

x_rapidapi_key_seo = "1b1cd853e0msh1849b1463bbe964p15df40jsn2fa6a5d956ef"
x_rapidapi_host_seo = "seo-api.p.rapidapi.com"
query_seo ={"q":"data scientist", "num": 20}

try:
    bucket_name = os.environ["GS_BUCKET_NAME"]
    service_account_key_file = os.environ["GS_SERVICE_ACCOUNT_KEY_FILE"]
    mongo_username = os.environ["MONGO_USERNAME"]
    mongo_password =  os.environ["MONGO_PASSWORD"]
    mongo_ip_address = os.environ["MONGO_IP"]
    database_name = os.environ["MONGO_DB_NAME"]
    collection_name = os.environ["MONGO_COLLECTION_NAME"]
except:
    config = configparser.ConfigParser()
    config.read('api.ini')
    bucket_name = config['GCS_credentails']['bucket_name']
    service_account_key_file = config['GCS_credentails']['service_account_key_file']
    mongo_username = config['mongo_credentails']['mongo_username']
    mongo_password = config['mongo_credentails']['mongo_password']
    mongo_ip_address = config['mongo_credentails']['mongo_ip_address']
    database_name = config['mongo_credentails']['database_name']
    collection_name = config['mongo_credentails']['collection_name']
