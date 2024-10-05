sudo apt-get update && \
sudo apt-get install -y screen && \
curl -fsSL https://ollama.com/install.sh -o install.sh && \
chmod +x install.sh && \
./install.sh && \
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 installation/install_phi3.py