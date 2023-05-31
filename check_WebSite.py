import urllib.request as urllib
import time
import os

def check_connect(url):

    os.system("cls")
    print("\nChecking connectivity...")

    response = urllib.urlopen(url)
    print("Connected to --->", url, "succesfully")
    print("The responde code was:", response.getcode())

def welcome_script():
    print("this is a site connectivity checker program\n",
          "------------------------------------------")

def input_url():

    input_url = input("Input the url of the site you want to check: \n")
    return input_url

def reloadCheck(url):

    while True:
        print("\nchecking again in 1 minute")
        time.sleep(60)
        check_connect(url)

def main():

    welcome_script()
    url = input_url()
    check_connect(url)
    reloadCheck(url)

if __name__ == '__main__':
    main()