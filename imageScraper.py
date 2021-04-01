import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time     
import urllib.request
import os
import winsound

CHROME_PATH = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
chrome_options = Options()
chrome_options.add_argument('window-size=800x600')
chrome_options.add_argument("headless")
chrome_options.add_argument('no-proxy-server')
chrome_options.add_argument("proxy-server='direct://'")
chrome_options.add_argument("proxy-bypass-list=*")
chrome_options.binary_location = CHROME_PATH
file_path = ''
browser = webdriver.Chrome(executable_path='Chrome/chromedriver', options=chrome_options)

def search_image(search_term):
    browser.get('https://unsplash.com/')
    time.sleep(5)
    search_box = browser.find_element_by_name('searchKeyword')
    search_box.send_keys(search_term)
    search_box.submit()
    try:
        os.mkdir(search_term)
    except FileExistsError:
        print('folder already exists')
    os.chdir(search_term)
    time.sleep(5)
    get_image_url()

def get_image_url():
    check_list = []
    i = 0
    for y in range(10):
        scroll_down()
        images = browser.find_elements_by_xpath('//*[@id="app"]//img')
        for image in images:
            if "photo" in image.get_attribute('src'):
                src = image.get_attribute('src')
                if i == 100:
                    winsound.Beep(500, 200)
                    browser.close()
                if check_list.count(src) == 0:
                    check_list.append(src)
                    url_to_jpg(i, src, file_path)
                    i += 1
    browser.close()

def url_to_jpg(i, url, filepath):
    filename = 'image-{}.jpg'.format(i)
    full_path = '{}{}'.format(filepath, filename)
    urllib.request.urlretrieve(url, full_path)
    print('{} saved.'.format(filename))
    return None

def scroll_down():
    html = browser.find_element_by_tag_name('html')
    html.send_keys(Keys.END)
    time.sleep(0.5)
    html.send_keys(Keys.PAGE_UP)
    time.sleep(1.5)

search_image('new')