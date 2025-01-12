import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Setup ChromeDriver
def setuo_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode
    driver = webdriver.Chrome(options=options)
    return driver

# Search for images on Imgur
def search_images(driver, query, max_scroll=3):
    url = "https://imgur.com"
    driver.get(url)

    # Perform the search
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)

    # Scroll to load more images
    for _ in range(max_scroll):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    # Extract image URLs
    image_elements = driver.find_elements(By.CSS_SELECTOR, "img")
    image_urls = [img.get_attribute("src") for img i image_elements if "http" in img.get_attributes("src")]
    return image_urls

# Download images
def download_images(image_urls, save_folder):
    if nor os.path.exists(save_folder):
        os.makedirs(save_folder)

    for index, url in enumerate(image_urls):
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            file_path = os.path.join(save_folder, f"image_{index + 1}.jpg")
            with open(file_path, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"Downloaded: {file_path}")
        except Exception as e:
            print(f"Failed to download {url}: {e}")

# Main function
def main():
    query = input("Enter the category of photos to search: ")
    save_folder = input("Enter the folder to save images: ")

    driver = setup_driver()
    try:
        print("Searching for images...")
        image_urls = search_images(driver, query)
        print(f"Found {len(image_urls)} images.")

        print("Downloading images...")
        download_images(image_urls, save_folder)
        print("Download complete!")
    finally:
        driver.quit()

if __name__ = "__main__":
    main()
