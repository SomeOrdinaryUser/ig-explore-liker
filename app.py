from random import randint
from time import sleep

from selenium import webdriver


# Change to your account login information.
username = ""
password = ""

# Global variables
max_likes = int(input('Enter amount of likes to perform: '))
print(
    f'Okay! I will like {max_likes} photo(s).')
liked_photos = 0


# Change this to your Firefox webdriver locationF
driver = webdriver.Firefox(executable_path=r"C:\\webdriver\\geckodriver.exe")


def login():
    # Get ig login page
    url = 'https://www.instagram.com/accounts/login/'
    driver.get(url)
    sleep(3)

    # Type username, password
    login_u = driver.find_element_by_name(name="username")
    login_p = driver.find_element_by_name(name="password")
    login_u.click()
    login_u.send_keys(username)
    sleep(1)
    login_p.click()
    sleep(1)
    login_p.send_keys(password)
    sleep(2)

    # Click login
    login_button = driver.find_element_by_xpath(
        '/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button/div')
    login_button.click()
    sleep(7)
    save_login_popup = driver.find_element_by_xpath(
        '/html/body/div[1]/section/main/div/div/div/section/div/button')
    save_login_popup.click()
    sleep(7)
    explore()


def ask_user():
    global max_likes
    max_likes = int(input('Okay. Enter new amount of likes to perform: '))


def explore():
    global max_likes
    global liked_photos
    driver.get('https://www.instagram.com/explore/')
    sleep(6)
    pics = driver.find_elements_by_class_name('eLAPa')
    pics = pics[16:17]
    for pic in pics:
        sleep(randint(3, 16))
        sleep(randint(5, 19))
        pic.click()
        print("Clicked picture.")
        sleep(randint(3, 16))

        # Like photo
        sleep(randint(3, 16))
        likeButton = driver.find_element_by_class_name('fr66n')
        sleep(randint(6, 15))
        likeButton.click()
        print("Liked picture")
        sleep(randint(3, 6))
        liked_photos += 1
        print(f"Liked {liked_photos} photos")
        if liked_photos >= max_likes:
            ask_quit_or_not = input('Would you like to quit? y/n ')
            if ask_quit_or_not == 'y':
                driver.quit()
            elif ask_quit_or_not == 'n':
                ask_user()
                explore()
    explore()


if __name__ == "__main__":
    login()
