import re
import requests
from bs4 import BeautifulSoup
import subprocess
from requests.exceptions import RequestException
from urllib3.exceptions import NewConnectionError

wordlist_file = "/mnt/c/Users/MrRobot/Coding/chinacoal/wordlist.txt"
base_url = 'https://www.scamdoc.com/view/'
start_number = 130180
end_number = 1301837

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

domain_pattern = r'[\w.-]+\.[a-zA-Z]{2,}'  # Matches domain names without protocol

def is_website_live(domain):
    try:
        response = requests.head(f'https://{domain}', headers=headers)
        return 200 <= response.status_code < 300
    except RequestException as e:
        if not (isinstance(e, ConnectionError) and isinstance(e.__context__, NewConnectionError)):
            pass
        return False

for num in range(start_number, end_number + 1):
    url = base_url + str(num)

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('title')

        if title:
            percentage_pattern = r'\d+%'  # Matches one or more digits followed by a percent sign
            percentage_match = re.search(percentage_pattern, title.string)
            domain_match = re.search(domain_pattern, title.string)

            if percentage_match and domain_match:
                percentage = int(percentage_match.group()[:-1])  # Convert percentage string to integer
                domain = domain_match.group()
                if percentage < 10:  # Check if percentage is less than 10
                    print(f'URL: {url} - Domain: https://{domain} - Percentage: {percentage}%')
                    
                    if is_website_live(domain):
                        print(f"Running directory scan against https://{domain}")
                        subprocess.run(['dirsearch', '-u', domain, '-q', '-x', '403,404', '-w', wordlist_file])
                    else:
                        print(f'Domain: https://{domain} - Website is not live.')
                else:
                    print(f'URL: {url} - Percentage: {percentage}% is not less than 10%.')

            else:
                print(f'URL: {url} - No percentage value or domain found in title tag.')
        else:
            print(f'URL: {url} - Title tag not found.')
    except requests.exceptions.HTTPError as e:
        pass
    except requests.exceptions.RequestException as e:
        pass
