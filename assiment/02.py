import requests
import os


def clearConsole(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')


clearConsole()


def isitdown():
    input_url = input(
        'Welcome to IsItDown.py! \nPlease write a URL or URLs you want to check. (separated by comma) \n').split(',')

    url_list = [x.strip() for x in input_url]

    for check_url in url_list:
        if len(url_list) == 1 and '.' not in check_url:
            print(f"{check_url} is not a valid URL")

        elif check_url[0:4] != 'http':
            check_url = "http://" + check_url
        try:
            if requests.get(check_url).status_code == 200:
                print(f"{check_url} is Up!")
        except requests.exceptions.ConnectionError:
            if '.' not in check_url:
                pass
            else:
                print(f"{check_url} is down!")
        except requests.exceptions.MissingSchema:
            if '.' not in check_url:
                pass
            else:
                print(f"{check_url} is down!")

    def anwser_me():
        anwser = input("Do you want to start over? y/n ").lower()
        if anwser == "n":
            print("ok, bye!")
        elif anwser == "y":
            clearConsole()
            isitdown()
        else:
            print("That\'s not a valid answer!")
            anwser_me()

    anwser_me()


isitdown()
