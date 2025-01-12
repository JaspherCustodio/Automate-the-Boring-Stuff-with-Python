import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def verify_links(url):
    try:
        # Fetch the main page cnontent
        response = requests.get(url)
        response.raise_for_status() # Raise an error for bad HTTP responses(e.g., 404, 500)
    except requests.exceptions.RequestException as e:
        print(f"Failed to load the main URL: {url}\nError: {e}")
        return

    # Parse the page content
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', href=True)

    if not links:
        print("No links found on the page.")
        return

    broken_links = []

    print(f"checking {len(links)} links on {url}...\n")

    for link in links:
        href = link['href']
        full_url = urljoin(url, href) # Handle relative links
        try:
            link_response = requests.head(full_url, allo_redirects=True, timeout=5)
            if link_response.status_code == 404:
                print(f"Broken link: {full_url}")
                broken_links.append(full_url)
        except requests.exceptions.RequestException as e:
            print(f"Error checking {full_url}: {e}")
            broken_links.append(full_url)

    # Print summary
    if broken_links:
        print("\nBroken links found:")
        for broken in broken_links:
            print(broken)
    else:
        print("No broken links found!")

# Main function
if __name__ == "__main__":
    url = input("Enter the URL of the web page: ").strip()
    verify_links(url)
