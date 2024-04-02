#!/usr/bin/env python

import argparse
import requests
from PIL import Image
import numpy as np
from io import BytesIO
import urllib.parse
from selenium import webdriver

def paraweb_flickr(url):
    # Use requests to download the image
    response = requests.get(url)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))

        pixels = np.array(image)

        binary_message = ''
        # Extract binary data from the image
        for row in pixels:
            for pixel in row:
                for channel in range(3):  # Assuming RGB channels
                    binary_message += bin(pixel[channel])[2:].rjust(8, '0')[-2:]

        # Extract the length of the actual message from the first 32 bits
        length_bits = binary_message[:32]
        message_length = int(length_bits, 2)  # Convert binary to int

        # Calculate the end index of the message bits, adjusting for the length prefix
        message_end_index = 32 + message_length * 2

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
        
        driver = webdriver.Chrome()
        driver.get(f"data:text/html,{encoded_html}")
        print("Press Enter to exit...")
        input()
        
    else:
        print(f"Failed to download the image, status code: {response.status_code}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Extract hidden messages from Flickr images.")
    parser.add_argument("url", help="The URL of the Flickr image.")
    args = parser.parse_args()

    paraweb_flickr(args.url)

if __name__ == "__main__":
    main()