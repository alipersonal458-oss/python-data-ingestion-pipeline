import os
from dotenv import load_dotenv
import requests
load_dotenv()
api_url=os.getenv('BASE_API_URL')
env_mode=os.getenv('ENV_MODE')
cleaned_data=[]
print(f"Running pipeline in [{env_mode}] mode...")
try:
    response=requests.get(api_url,timeout=5)
    response.raise_for_status() 
    data=response.json()
    for post in data:
        cleaned_data.append({
            'Id':post['id'],
            'Title':post['title'],
            'Body':post['body'][:50],
            'User_Id':post['userId']
        })
except requests.exceptions.Timeout:
    print("The request timed out. Retrying in 5 seconds...")
except requests.exceptions.HTTPError as err:
    status_code = err.response.status_code
    if status_code == 401:
        print("Invalid API Key or token expired.")
    elif status_code == 429:
        print("Rate limit exceeded. Backing off...")
    else:
        print(f"HTTP error occurred: {err}")
except requests.exceptions.ConnectionError:
    print("Network down. Check your internet connection.")
except ValueError:
    print("Server sent back invalid data format.")
except requests.exceptions.RequestException as e:
    print(f"An unexpected API error occurred: {e}")
except Exception as e:
    print(f"Data Processing Error (The API worked, but your code broke!): {e}")
import csv
if cleaned_data:
    try:
        # FIX 2: Added mode='w' and newline=''
        with open('PROJECT/fetch_data.csv', mode='w', newline='', encoding='utf-8') as f:
            # FIX 3: Capitalized DictWriter
            writer = csv.DictWriter(f, fieldnames=["Id", "Title", "Body", "User_Id"])
            writer.writeheader()
            writer.writerows(cleaned_data)
            print("Data successfully saved to PROJECT/fetch_data.csv!")
    except FileNotFoundError:
        print("Error: The 'PROJECT' folder does not exist. Please create the folder first.")
    except Exception as e:
        print(f"Failed to save CSV file: {e}")