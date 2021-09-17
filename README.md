# MovieDowloader-NetNaija
Script to automate Movie downloads from theNetnaija.com.

The script scrapes thenetnaija.com to download any available movie. This is for convenience given the Ad clogs that users often face when navigating the website.
Ensure you download Chromedriver or another executable for Selenium Webdriver to control the browser.
Also ensure you get the download page of the file in this manner 'https://www.thenetnaija.com/videos/movies/14542-vacation-friends-2021'.
You can adjust the script for the likes of `inputURL`, `executable_path`, `download_dir`, `executable_path_for_chrome`.
The following code donwloads the movie of choice:

```
initializer = MovieDLerforNetNaija()
# Download page's link in this manner
initializer.inputURL('https://www.thenetnaija.com/videos/movies/14542-vacation-friends-2021')
# To get link to subtitle download page
initializer.getSRTDLLink()
# To get link to video download page
initializer.getMovieDLLink()
chrome_options = Options()
# `executable_path` is where Chromedriver is located on your machine
browser = webdriver.Chrome(options=chrome_options, executable_path= ' ')
 # Preferred directory where downloaded files go
download_dir = ' '
# Path where Chromedriver is located
executable_path_for_chrome =  ' '
# Executes the code
initializer.enable_download_headless(browser, download_dir, executable_path_for_chrome)
```
