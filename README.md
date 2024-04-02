# Paraweb Demo

This repository demonstrates basic encoding and decoding mechanisms for the
[Paraweb](https://www.paraweb.io).

The Paraweb is an invisible world wide web that is built and surfable on top of
the existing world wide web. Paraweb sites are embedded
[steganographically](https://en.wikipedia.org/wiki/Steganography) in content on
existing sites.

Tthe high-degree, high-throughput nature of Web 2.0 social networking sites to
may allow low-degree, low-throughput posting, hosting, and traversal of a
network embedded in the larger network while allowing that traffic to appear
similar or indistinguishable from regular traffic in the larger network.

This repository contains basic Python programs for creating this content and
decoding it in social network posts where it is known to exist.

**NOTE:** These programs are basic prototypes. The social networks listed below
are used because they return images with minimal processing and non-lossy
formats. Additionally, the steganographic encoding is basic.

Fortunately, the encrypting protocol is as much a part of a Paraweb link as its
hosting URL, and is as individually customizable.

## Use

### Paraweb Creator (Basic)

For basic text messages:

`python paraweb_creator_basic.py input_image.png --message "Your hidden message here" output_image.png`

For whole HTML files:

`python paraweb_creator_basic.py input_image.png --message-file path/to/your_message.txt output_image.png`

### Paraweb Browser (Basic) (directly-hosted images)

`python paraweb_browser_basic.py <Page with img URL>`

### Paraweb Browser (Basic) (Flickr-hosted Para sites)

`python paraweb_browser_basic_flickr.py <Flickr Photo URL>`

### Paraweb Browser (Basic) (Imgur-hosted Para sites)

`python paraweb_browser_basic_imgur.py <Imgur Post URL>`

### Paraweb Browser (Basic) (Tumblr-hosted Para sites)

`python paraweb_browser_basic_imgur.py <Tumblr Post URL>`