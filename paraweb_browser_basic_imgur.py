import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import requests
from io import BytesIO
import numpy as np
import urllib.parse


def setup_webdriver(headless=False):
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    return driver


def extract_and_decode_image(url):
    driver = setup_webdriver(headless=True)  # Modify as needed
    driver.get(url)
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'img.image-placeholder'))
    )
    image_element = driver.find_element(By.CSS_SELECTOR, 'img.image-placeholder')
    ActionChains(driver).click(image_element).perform()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.ImageViewerContent'))
    )
    image_element = driver.find_element(By.CSS_SELECTOR, 'div.ImageViewerContent').find_element(By.TAG_NAME, 'img')

    image_url = image_element.get_attribute('src')
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(image_url, headers=headers)
    
    pixels = np.array(image)

    binary_message = ''
    # Extract binary data from the image
    for row in pixels:
        for pixel in row:
            for channel in range(3):  # Assuming RGB channels
                # Get the last two bits from each channel and add to the binary message
                binary_message += bin(pixel[channel])[2:].rjust(8, '0')[-2:]

    # Extract the length of the actual message from the first 32 bits
    length_bits = binary_message[:32]
    message_length = int(length_bits, 2)  # Convert binary to int

    # Calculate the end index of the message bits, adjusting for the length prefix and bit repetition
    message_end_index = 32 + message_length * 2  # Each bit is doubled

    # Extract the message bits, taking every second bit to account for bit repetition
    actual_message_bits = binary_message[32:message_end_index:2]

    # Reconstruct the byte sequence from the binary data
    message_bytes = bytearray()
    for i in range(0, len(actual_message_bits), 8):
        byte = actual_message_bits[i:i+8]
        if len(byte) == 8:
            message_bytes.append(int(byte, 2))

    # Decode the byte sequence back into a string using UTF-8
    message = message_bytes.decode('utf-8')
    encoded_html = urllib.parse.quote(message)

    driver.get(f"data:text/html,{encoded_html}")

def main():
    parser = argparse.ArgumentParser(description="Extract and decode hidden messages from images hosted on Imgur.")
    parser.add_argument("url", help="The URL of the Imgur page containing the image.")
    args = parser.parse_args()

    message = extract_and_decode_image(args.url)
    print(f"Decoded Message: {message}")
    # Optional: Render the message as HTML or process further

if __name__ == "__main__":
    main()
