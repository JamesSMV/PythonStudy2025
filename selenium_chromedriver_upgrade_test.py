from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())  #  Автоматически скачает нужную версию

''' 
ввести в терминале для обновления chromedriver указав  версию как у браузера: 
wget https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/135.0.7049.52/linux64/chromedriver-linux64.zip
unzip chromedriver-linux64.zip
sudo mv chromedriver-linux64/chromedriver /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver 
'''