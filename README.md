# Bot Setup

## Getting Started

### MacOS
1. download chrome if you haven't already https://www.google.com/chrome/
2. check the version 
```bash
$ /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --version
Google Chrome 80.0.3987.149
```
3. Download the chromedriver that mataches your installed Chrome version https://chromedriver.chromium.org/downloads
4. move the chromedriver to /bin
5. Install all python dependencies 
```bash
$ pipenv install
```
6. Run the app 
```bash
$ python3 app.py
```

### Linux
1. Install Chrome 
```bash
curl https://intoli.com/install-google-chrome.sh | bash
mv /usr/bin/google-chrome-stable /usr/bin/google-chrome
google-chrome --version
```
2. Install chromedriver, make sure the major version matches your chrome install
```bash
wget https://chromedriver.storage.googleapis.com/80.0.3987.106/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/chromedriver
chromedriver --version
```
3. Run the app
```bash
$ python3 app.py
```