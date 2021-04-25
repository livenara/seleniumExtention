from selenium import webdriver
import glob

extention = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
path = glob.glob(f"C:\\Users\\<user>\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Extensions\\{extention}\\*")[0]

options = webdriver.ChromeOptions()
options.add_argument('--load-extension=' + path)
driver = webdriver.Chrome(chrome_options=options) 