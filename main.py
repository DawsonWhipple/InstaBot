from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

from dotenv import load_dotenv

load_dotenv()
import os

# Class that handles all actions of the login page
class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def accept_cookies(self, driver):
        cookies_element = driver.find_element(By.XPATH, "//button[@class='_a9-- _ap36 _a9_0']")
        cookies_element.click()

    def login(self, username, password):
        username_input = self.driver.find_element(By.XPATH, "//input[@name='username']")
        password_input = self.driver.find_element(By.XPATH, "//input[@name='password']")
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        driver.execute_script("arguments[0].click();", login_button)

# Class that handles all actions of the home page
class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("http://www.instagram.com")

    def decline_notifications(self, driver):
        notifications_element = driver.find_element(By.XPATH, "//button[@class='_a9-- _ap36 _a9_1']")
        self.driver.execute_script("arguments[0].click();", notifications_element)

    def return_to_homepage(self, driver):
        home = WebDriverWait(driver, timeout=60).until(
            lambda d: d.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[1]/div/span/div/a'))
        home.click()

class Search:
    def __init__(self, driver):
        self.driver = driver
    # Searches the given tag
    def search_tag(self, driver, tag):
        search = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a')
        search.click()

        search_tag =  '#' + tag
        search_input = WebDriverWait(driver, timeout=60).until(
            lambda d: d.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input'))
        search_input.send_keys(search_tag)
        found = WebDriverWait(driver, timeout=60).until(
            lambda d: d.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a/div[1]'))
        found.click()


# <svg aria-label="Search" class="x1lliihq x1n2onr6 x5n08af" fill="currentColor" height="24" role="img" viewBox="0 0 24 24" width="24"><title>Search</title><path d="M19 10.5A8.5 8.5 0 1 1 10.5 2a8.5 8.5 0 0 1 8.5 8.5Z" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"></path><line fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" x1="16.511" x2="22" y1="16.511" y2="22"></line></svg>
# <div class="x9f619 x3nfvp2 xr9ek0c xjpr12u xo237n4 x6pnmvc x7nr27j x12dmmrz xz9dl7a xn6708d xsag5q8 x1ye3gou x80pfx3 x159b3zp x1dn74xm xif99yt x172qv1o x10djquj x1lhsz42 xzauu7c xdoji71 x1dejxi8 x9k3k5o xs3sg5q x11hdxyr x12ldp4w x1wj20lx x1lq5wgf xgqcy7u x30kzoy x9jhf4c"><div><div class="x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1"><div class="x9f619 xxk0z11 xii2z7h x11xpdln x19c4wfv xvy4d1p"><svg aria-label="Search" class="x1lliihq x1n2onr6 x5n08af" fill="currentColor" height="24" role="img" viewBox="0 0 24 24" width="24"><title>Search</title><path d="M19 10.5A8.5 8.5 0 1 1 10.5 2a8.5 8.5 0 0 1 8.5 8.5Z" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"></path><line fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" x1="16.511" x2="22" y1="16.511" y2="22"></line></svg></div></div></div><div class="x6s0dn4 x9f619 xxk0z11 x6ikm8r xeq5yr9 x1swvt13 x1s85apg xzzcqpx" style="opacity: 1;"><div style="width: 100%;"><div class="" style="width: 100%;"><span class="x1lliihq x1plvlek xryxfnj x1n2onr6 x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye xl565be xo1l8bm x5n08af x1tu3fi x3x7a5m x10wh9bi x1wdrske x8viiok x18hxmgj" dir="auto" style="line-height: var(--base-line-clamp-line-height); --base-line-clamp-line-height: 20px;"><span class="x1lliihq x193iq5w x6ikm8r x10wlt62 xlyipyv xuxw1ft">Search</span></span></div></div></div></div>
# <a class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _a6hd" href="#" role="link" tabindex="0"><div class="x9f619 x3nfvp2 xr9ek0c xjpr12u xo237n4 x6pnmvc x7nr27j x12dmmrz xz9dl7a xn6708d xsag5q8 x1ye3gou x80pfx3 x159b3zp x1dn74xm xif99yt x172qv1o x10djquj x1lhsz42 xzauu7c xdoji71 x1dejxi8 x9k3k5o xs3sg5q x11hdxyr x12ldp4w x1wj20lx x1lq5wgf xgqcy7u x30kzoy x9jhf4c"><div><div class="x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1"><div class="x9f619 xxk0z11 xii2z7h x11xpdln x19c4wfv xvy4d1p"><svg aria-label="Search" class="x1lliihq x1n2onr6 x5n08af" fill="currentColor" height="24" role="img" viewBox="0 0 24 24" width="24"><title>Search</title><path d="M19 10.5A8.5 8.5 0 1 1 10.5 2a8.5 8.5 0 0 1 8.5 8.5Z" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"></path><line fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" x1="16.511" x2="22" y1="16.511" y2="22"></line></svg></div></div></div><div class="x6s0dn4 x9f619 xxk0z11 x6ikm8r xeq5yr9 x1swvt13 x1s85apg xzzcqpx" style="opacity: 1;"><div style="width: 100%;"><div class="" style="width: 100%;"><span class="x1lliihq x1plvlek xryxfnj x1n2onr6 x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye xl565be xo1l8bm x5n08af x1tu3fi x3x7a5m x10wh9bi x1wdrske x8viiok x18hxmgj" dir="auto" style="line-height: var(--base-line-clamp-line-height); --base-line-clamp-line-height: 20px;"><span class="x1lliihq x193iq5w x6ikm8r x10wlt62 xlyipyv xuxw1ft">Search</span></span></div></div></div></div></a>
driver = webdriver.Firefox()
driver.implicitly_wait(5)

home_page = HomePage(driver)
login_page = LoginPage(driver)
login_page.accept_cookies(driver)
login_page.login(os.getenv('INSTAGRAM_USERNAME'), os.getenv('PASSWORD'))
sleep(5)
home_page.decline_notifications(driver)

search = Search(driver)

tags = ["wrx", "sti", "subaru", "subie"]
for tag in tags:
    search.search_tag(driver, tag)
    sleep(10)
    home_page.return_to_homepage(driver)

sleep(10)

home_page.return_to_homepage(driver)

sleep(10)

driver.close()



# driver.get("http://www.instagram.com")
# driver.implicitly_wait(10)
# # The html for the 'Accept all cookies' button:
# #<button class="_a9-- _ap36 _a9_0" tabindex="0">Allow all cookies</button>
# element = driver.find_element(By.XPATH, "//button[@class='_a9-- _ap36 _a9_0']")
# element.click()

# #Username:
# # <input aria-label="Phone number, username, or email" aria-required="true" autocapitalize="none" autocorrect="off" maxlength="75" 
# # class="_aa4b _add6 _ac4d _ap35" dir="" type="text" value="" name="username">
# element = driver.find_element(By.XPATH, "//input[@name='username']")
# element.send_keys("dawson.whipple")
# #Password:
# # <input aria-label="Password" aria-required="true" autocapitalize="none" autocorrect="off" 
# # class="_aa4b _add6 _ac4d _ap35" type="password" value="" name="password">
# element = driver.find_element(By.XPATH, "//input[@name='password']")
# element.send_keys("S0legehu")
# #submit username and password
# element = driver.find_element(By.XPATH, "//button[@type='submit']")
# driver.execute_script("arguments[0].click();", element)

# sleep(2)
# #do not accept notifications
# element = driver.find_element(By.XPATH, "//button[@class='_a9-- _ap36 _a9_1']")
# driver.execute_script("arguments[0].click();", element)

#search button
# element = driver.find_element(By.XPATH, "//div[@class='x1n2onr6 x6s0dn4 x78zum5']")
# driver.execute_script("arguments[0].click();", element)
# sleep(3)

# element = driver.find_element(By.XPATH, "//input[@aria-label='Search input']")
# element.send_keys("bittersweet_bakery_")
# driver.execute_script("arguments[0].click();", element)
# <div class="x1n2onr6 x6s0dn4 x78zum5"><a class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _a6hd" href="#" role="link" tabindex="0"><div class="x9f619 x3nfvp2 xr9ek0c xjpr12u xo237n4 x6pnmvc x7nr27j x12dmmrz xz9dl7a xn6708d xsag5q8 x1ye3gou x80pfx3 x159b3zp x1dn74xm xif99yt x172qv1o x10djquj x1lhsz42 xzauu7c xdoji71 x1dejxi8 x9k3k5o xs3sg5q x11hdxyr x12ldp4w x1wj20lx x1lq5wgf xgqcy7u x30kzoy x9jhf4c"><div><div class="x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1"><div class="x9f619 xxk0z11 xii2z7h x11xpdln x19c4wfv xvy4d1p"><svg aria-label="Search" class="x1lliihq x1n2onr6 x5n08af" fill="currentColor" height="24" role="img" viewBox="0 0 24 24" width="24"><title>Search</title><path d="M19 10.5A8.5 8.5 0 1 1 10.5 2a8.5 8.5 0 0 1 8.5 8.5Z" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"></path><line fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" x1="16.511" x2="22" y1="16.511" y2="22"></line></svg></div></div></div><div class="x6s0dn4 x9f619 xxk0z11 x6ikm8r xeq5yr9 x1swvt13 x1s85apg xzzcqpx" style="opacity: 1;"><div style="width: 100%;"><div class="" style="width: 100%;"><span class="x1lliihq x1plvlek xryxfnj x1n2onr6 x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye xl565be xo1l8bm x5n08af x1tu3fi x3x7a5m x10wh9bi x1wdrske x8viiok x18hxmgj" dir="auto" style="line-height: var(--base-line-clamp-line-height); --base-line-clamp-line-height: 20px;"><span class="x1lliihq x193iq5w x6ikm8r x10wlt62 xlyipyv xuxw1ft">Search</span></span></div></div></div></div></a></div>
# <input aria-label="Search input" autocapitalize="none" class="x1lugfcp x19g9edo x1lq5wgf xgqcy7u x30kzoy x9jhf4c x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x5n08af xl565be x5yr21d x1a2a7pz xyqdw3p x1pi30zi xg8j3zb x1swvt13 x1yc453h xh8yej3 xhtitgo xs3hnx8 x1dbmdqj xoy4bel x7xwk5j" dir="" placeholder="Search" type="text" value="">

# <button class="_a9-- _ap36 _a9_1" tabindex="0">Not Now</button>


# <button class=" _acan _acap _acas _aj1- _ap30" disabled="" type="submit">