import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up Selenium WebDriver
def setup_driver():
    options = webdriver.ChromeOptions()
    #options.add_argument("--headless") # Run in headless mode (no browser window)
    driver = webdriver.Chrome(options=options)
    return driver

#Automate the game
def play_2048(driver):
    url = "https://gabrielecirulli.github.io/2048/"
    driver.get(url)
    time.sleep(2) # Wait for the game to load

    # Find the game container
    game_container = driver.find_element(By.TAG_NAME, "body")

    # Define the sequence of moves: up, right, down, left
    moves = [Keys.ARROW_UP, Keys.ARROW_RIGHT, Keys.ARROW_DOWN, Keys.ARROW_LEFT]

    try:
        while True:
            for move in moves:
                game_container.send_keys(move)
                time.sleep(0.1) # Small delay to simulate human behavior

            # Check if the game is over
            game_over = driver.find_elements(By.CLASS_NAME, "game-over")
            if game_over:
                print("Game Over!")
                break

    except KeyboardInterrupt:
            print("Stopped by user.")

# Main function
def main():
    driver = setup_driver()
    try:
        play_2048(driver)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
