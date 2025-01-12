#! python3
import requests, webbrowser, bs4
import os

def search_query(query):
    print('Searching Bing...')
    
    # Request search results from Bing
    res = requests.get(f'https://www.bing.com/search?q={query}')
    res.raise_for_status()

    # Parse the HTML response
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Find result links (anchor tags inside search results)
    link_elems = soup.select('li.b_algo h2 a')  # Bing selector for results
    links = [link['href'] for link in link_elems]

    # Open up to 5 links in different Chrome windows
    num_open = min(5, len(links))
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"  # Update path if needed
    
    for i in range(num_open):
        webbrowser.get(chrome_path).open_new(links[i])

# Prompt the user for input
query = input("Enter search query: ")
search_query(query)
