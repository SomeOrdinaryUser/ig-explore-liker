import sys
from random import randint
from time import sleep

from selenium import webdriver

### change to your login info
username = "" # can be username, email, or phone #
password = "" # password

# Global variables
max_likes = int(input("Enter amount of likes to perform: "))
liked_photos = 0

print(f"Okay! Liking {max_likes} photo(s).")

### change this to your Firefox webdriver locationF
driver = webdriver.Firefox(executable_path=r"C:\\webdriver\\geckodriver.exe")


def login():
    # get ig login page
    url = "https://www.instagram.com/accounts/login/"
    driver.get(url)
    sleep(4)
    login_u = driver.find_element_by_name(name="username")
    login_p = driver.find_element_by_name(name="password")
    login_u.click()
    login_u.send_keys(username)
    sleep(2)
    login_p.click()
    sleep(2)
    login_p.send_keys(password)
    sleep(3)

    # Click login
    login_button = driver.find_element_by_xpath(
        "/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button"
    )
    sleep(3)
    login_button.click()
    print("logged in")
    sleep(7)
    save_login_popup = driver.find_element_by_xpath(
        "/html/body/div[1]/section/main/div/div/div/section/div/button"
    )
    sleep(2)
    save_login_popup.click()
    sleep(7)
    explore()


def ask_user():
    global max_likes
    max_likes = int(input("Okay. Enter new amount of likes to perform: "))


def scroll_page():
    scroll_pause_time = 4
    scroll_to_bottom_amount = 4
    while scroll_to_bottom_amount > 0:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(scroll_pause_time)
        scroll_to_bottom_amount -= 1
        if scroll_to_bottom_amount == 0:
            pass


def explore():
    global liked_photos
    global max_likes
    driver.get("https://www.instagram.com/explore/")
    sleep(10)
    scroll_page()
    sleep(2)
    # find picture id's
    pics = driver.find_elements_by_class_name("eLAPa")
    pics = pics[40:41]
    for pic in pics:
        sleep(randint(3, 16))
        sleep(randint(5, 19))
        pic.click()
        sleep(randint(3, 16))

        # like photo
        sleep(randint(3, 16))
        likeButton = driver.find_element_by_class_name("fr66n")
        sleep(randint(6, 15))
        likeButton.click()
        sleep(randint(3, 6))
        liked_photos += 1
        print(f"Liked pics: {liked_photos}")
        if liked_photos == max_likes:
            ask_quit_or_not = input("Would you like to quit? y/n ")
            if ask_quit_or_not == "y":
                driver.quit()
            elif ask_quit_or_not == "n":
                ask_user()
                explore()
    explore()


if __name__ == "__main__":
    login()
