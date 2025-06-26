import requests
from bs4 import BeautifulSoup

# URL of the news website
url = 'https://www.bbc.com/news'  # You can change to another news site if needed

# Set headers to mimic a real browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

# Send GET request
response = requests.get(url, headers=headers)

# Check if request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all headline tags (can vary per website, often <h2>, <h3>, etc.)
    headlines = soup.find_all(['h2', 'h3'])

    # Extract and clean text
    headlines_text = [headline.get_text(strip=True) for headline in headlines if headline.get_text(strip=True)]

    # Save to a .txt file
    with open('headlines.txt', 'w', encoding='utf-8') as f:
        for i, line in enumerate(headlines_text, start=1):
            f.write(f"{i}. {line}\n")

    print(" Headlines saved to headlines.txt")
else:
    print(f" Failed to fetch page. Status code: {response.status_code}")