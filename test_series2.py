import urllib.request
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


#Series Downloader from theNetNaija
__author__ = 'Dzhud'

class MovieDLerforNetNaija:

    def inputURL(self, url):
        try:
            self.url = url
            requestSeries = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            openSeriesPage = urlopen(requestSeries)
            soupy = BeautifulSoup(openSeriesPage, "html.parser")
            return soupy
        except:
            print('Please check your internet or the url')
            
    def getMovieDLLink(self):
        prefix = 'https://www.thenetnaija.com'
        for i in MovieDLerforNetNaija.inputURL(self, self.url).find_all('a', href=True):
            ty = i['href']
            if 'download' in ty and 'download-sub' not in ty:
                return prefix+ty
            
    def getSRTDLLink(self):
        prefix = 'https://www.thenetnaija.com'
        for i in MovieDLerforNetNaija.inputURL(self, self.url).find_all('a', href=True):
            ty = i['href']
            if 'download-sub' in ty:
                return prefix+ty

    def enable_download_headless(self, browser, download_dir, executable_path_for_chrome):
        browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
        params = {'cmd':'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
        browser.execute("send_command", params)

        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920x1080")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--verbose')
        chrome_options.add_experimental_option("prefs", {"download.default_directory": download_dir,
                                                         "download.prompt_for_download": False,
                                                         "download.directory_upgrade": True,
                                                         "safebrowsing_for_trusted_sources_enabled": False,
                                                         "safebrowsing.enabled": False })
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-software-rasterizer')
        driver = webdriver.Chrome(options=chrome_options, executable_path=executable_path_for_chrome)

        browser.get(MovieDLerforNetNaija.getSRTDLLink(self))
        srtDL = browser.find_element_by_xpath("//*[@id='action-buttons']/button")
        browser.execute_script("arguments[0].click();", srtDL)

        browser.get(MovieDLerforNetNaija.getMovieDLLink(self))
        videoDL = browser.find_element_by_xpath("//*[@id='action-buttons']/button")
        videoDL.click()
        

initializer = MovieDLerforNetNaija()
initializer.inputURL(' ')
initializer.getSRTDLLink()
initializer.getMovieDLLink()
chrome_options = Options()
browser = webdriver.Chrome(options=chrome_options, executable_path=" ")
download_dir = " "
executable_path_for_chrome = " " 

initializer.enable_download_headless(browser, download_dir, executable_path_for_chrome)
                

        
    
    
        
    
    
    
