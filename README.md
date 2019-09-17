# sticker2gif

A tool to download Facebook Messenger Stickers and convert them into gif.


## Dependencies

`pip install Pillow`

## Usage

```python
from sticker2gif import Maker

url = input('URL: ')

tool = Maker(url, log=True)

tool.run()
```

## How to get Facebook Messenger Stickers

1- Inspect the sticker you want to save:

![alt text](https://i.imgur.com/ic3aAP9.png)


2- Head to the link of the sticker and copy it:

![alt text](https://i.imgur.com/UeKnXNn.png)


3- Paste it into the terminal, give it a name and determine the duration between the frames of the GIF:

![alt text](https://i.imgur.com/eeJBIko.png)


4- Voilà:

![alt text](https://i.imgur.com/b2bB9yH.gif)
