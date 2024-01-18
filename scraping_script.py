import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor, wait  # Add 'wait' import

def download_file(url, folder_path="."):
    local_filename = os.path.join(folder_path, url.split("/")[-1])
    with requests.get(url, stream=True) as response:
        with open(local_filename, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
    print(f"Downloaded: {local_filename}")

def download_zip_files(url, folder_path="."):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find all links with .zip extension
    zip_links = soup.find_all("a", href=lambda href: (href and href.endswith('.zip')))
    
    with ThreadPoolExecutor(max_workers=5) as executor:  # Adjust max_workers based on your preference
        # Download files concurrently using ThreadPoolExecutor
        futures = [executor.submit(download_file, urljoin(url, link['href']), folder_path) for link in zip_links]
        
        # Wait for all downloads to complete
        wait(futures)  # Use 'wait' function from concurrent.futures

if __name__ == "__main__":
    # Replace with your actual URL and folder path
    webpage_url = 'https://dbarchive.biosciencedbc.jp/data/open-tggates/LATEST/Rat/in_vitro/'
    folder_path = 'New Folder/'

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    download_zip_files(webpage_url, folder_path)

