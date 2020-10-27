from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def getImageLink(query):
    driver = webdriver.Firefox()

    URL = f"https://duckduckgo.com/?q={query}&atb=v241-4&iax=images&ia=images"
    link = ""
    try:
        driver.get(URL)

        el = driver.find_elements_by_class_name("tile--img__img")
        el[0].click()

        link = driver.find_element_by_class_name("c-detail__btn").get_attribute("href")
    except:
        link = "Image not found!"

    driver.close()

    return link
