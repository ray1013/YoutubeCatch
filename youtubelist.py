from selenium.webdriver import Chrome
from pytube import Playlist
import time
import os
d = Chrome("./chromedriver")
d.get("https://www.youtube.com/view_all_playlists?nv=1")

d.find_element_by_id("identifierId").send_keys("rliu.cmc")
d.find_element_by_id("identifierNext").click()
time.sleep(5)
d.find_element_by_class_name("whsOnd").send_keys("12zx10131028")
d.find_element_by_id("passwordNext").click()
time.sleep(5)
d.find_element_by_class_name("yt-uix-form-input-radio").click()
d.find_element_by_id("identity-prompt-confirm-button").click()
time.sleep(5)
ps = d.find_elements_by_class_name("vm-video-title-text")
for p in ps:
    t = p.text
    url = p.get_attribute("href")
    print(t,url)

    pl = Playlist(url)
    dn = "youtube/" + t + "/"
    if not os.path.exists(dn):
        os.makedirs(dn)
    pl.download_all(dn)
time.sleep(5)
d.close()