# Character name generator that supports *all* genres

The internet is full of different character generators, but why should you need to settle for pre-generated lists of names, browsing from site to site trying to find the best ones, when you could generate new names with a language model? Input *anything* as your preferred genre and optionally prompt with your existing nickname that you want to use as inspiration for the model.

## Install requirements

TODO installation script

``` bash
sudo apt-get install screen \
curl -fsSL https://ollama.com/install.sh | sh \
ollama run phi3 \
python3 -m pip install -r requirements
```

### Run in terminal

``` python3
python3 main.py
```
