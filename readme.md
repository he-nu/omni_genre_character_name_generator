# Character name generator that supports *all* genres

The internet is full of different character generators, but why should you need to settle for pre-generated lists of names, browsing from site to site trying to find the best ones, when you could generate new names with a language model? Input *anything* as your preferred genre and optionally prompt with your existing nickname that you want to use as inspiration for the model.

## State of the art UX

![Image of the command line user interface](image.png "Interface")

## Install requirements

TODO installation script

``` bash
sudo apt-get update && \
sudo apt-get install -y screen && \
curl -fsSL https://ollama.com/install.sh -o install.sh && \
chmod +x install.sh && \
./install.sh && \
python3 -m pip install -r requirements.txt
```

### Run in terminal

``` python3
python3 main.py
```
