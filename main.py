import random
import time
import tkinter.messagebox

import pyautogui
import tkinter as tk
import threading
import urllib.request
import json
import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
import base64
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

version = "1.2"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://magnilearn.com")

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome \
                         /83.0.4103.116 Safari/537.36"}
html = requests.get(driver.current_url, headers=headers)

soup = BeautifulSoup(html.content, 'html.parser')

dataurl = "https://raw.githubusercontent.com/TastyCake/AutoMagnilearn/master/Data.json"
versionurl = "https://raw.githubusercontent.com/TastyCake/AutoMagnilearn/master/Version"

headers = {
    "Authorization": "Bearer github_pat_11AX4RDGI0urP2lGOvjZc5_FWVK1DoMAvrtfHvC7LclyiNoG0eXlZC\
4eJWfyviHoF8RDRFXAZCzYryMIVW"
}


def updatesoup():
    global html
    global soup

    html = requests.get(driver.current_url, headers=headers)
    soup = BeautifulSoup(html.content, 'html.parser')


def fakeclick():
    driver.switch_to.window(driver.window_handles[-1])
    driver.find_element(By.CLASS_NAME, "hGohjX").find_element(by=By.ID, value="next_button").click()

def newlesson():
    driver.switch_to.window(driver.window_handles[-1])
    driver.find_element(by=By.XPATH, value="(//button[contains(@class, 'sc-iBkjds')])[2]").click()
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="//div/div[2]/div[3]/div/div/div/button[contains(@class, 'eXjqHJ')][1]").click()
    time.sleep(10)
    driver.find_element(by=By.XPATH, value="(//button[contains(@class, 'DTejP')])[1]").click()


# response = urllib.request.urlopen("https://pastebin.com/raw/XXn7nYNd")
response = requests.get(dataurl, headers=headers)
data = response.content.decode("utf-8")
json_data = json.loads(data)
print(json_data)

loggedUsername = ""


def containsuser(user):
    return user in json_data


def getdata(user, d):
    return json_data[user][d]


def updatedata():
    global response
    global data
    global json_data

    response = requests.get(dataurl, headers=headers)
    data = response.content.decode("utf-8")
    json_data = json.loads(data)


def updatecheck():
    r = requests.get(versionurl, headers=headers)
    d = r.content.decode("utf-8")
    jd = json.loads(d)

    if jd["latestVersion"] != version:
        tkinter.messagebox.showerror("Update", "You are not on the latest version. Click OK to update.")
        r = requests.get(jd["latestDataFile"])
        if r.status_code == 200:
            with open("data", 'wb') as file:
                file.write(r.content)
                tkinter.messagebox.showinfo("Updated", "You are now on the latest version please reopen the app.")
        else:
            tkinter.messagebox.showerror("Error", "Unexpected error. Please contact the the developer.")
            root.destroy()


root = tk.Tk()
root.geometry("250x100")
root.title("Auto Magnilearn")
root.iconbitmap("icon.ico", "icon.ico")

updatecheck()

toggle = False

f = open("text", 'r')

texts = f.read().splitlines()


def run():
    global toggle
    toggle = not toggle

    updatecheck()

    if toggle:
        root.state(newstate='iconic')
        time.sleep(1)
        pyautogui.click()
        pyautogui.moveTo(1530, 800)

    def send_messages():
        updatecheck()
        times = 0
        times2 = 0
        times3 = 0
        times4 = 0
        times5 = 0
        times6 = 0
        times7 = 0

        while toggle:
            time.sleep(0.5)
            updatecheck()
            pyautogui.typewrite(random.choice(texts))
            times += 1
            times2 += 1
            times3 += 1
            times4 += 1
            times5 += 1
            times6 += 1
            times7 += 1

            if loggedUsername == "":
                tkinter.messagebox.showerror("Error", "You are not logged in.")
                root.destroy()
            if times >= 20:
                times = 0
                fakeclick()
            if times2 >= 24:
                times2 = 0
                pyautogui.click()
            if times3 >= random.randint(220, 245):
                times3 = 0
                pyautogui.press("f5")
            if times4 >= 3000:
                times4 = 0
                newlesson()
            if times5 >= 5:
                if not containsuser(loggedUsername):
                    updatedata()
                    tkinter.messagebox.showerror("Error", "Your time has expired.")
                    root.destroy()
            if times6 >= 50:
                times6 = 0
                pyautogui.press("enter")
            if times7 >= 35:
                times7 = 0
                pyautogui.click()

    if toggle:
        t = threading.Thread(target=send_messages)
        t.start()


def confirm_click():
    global loggedUsername
    username = username_text.get("1.0", tk.END).strip()
    password = password_text.get("1.0", tk.END).strip()

    if not containsuser(username):
        tkinter.messagebox.showerror("Error", "Username is incorrect.")
    else:
        if password != getdata(username, "password"):
            tkinter.messagebox.showerror("Error", "Password is incorrect.")
        else:
            loggedUsername = username
            tkinter.messagebox.showinfo("Logged in", "Logged in successfully.")
            username_text.grid_forget()
            password_text.grid_forget()
            confirm_button.grid_forget()
            username_label.grid_forget()
            password_label.grid_forget()
            button = tk.Button(root, text="Start/Stop", command=run)
            button.grid(row=2, column=1, padx=5, pady=5)


username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=5, pady=5)
username_text = tk.Text(root, height=1, width=20)
username_text.grid(row=0, column=1, padx=5, pady=5)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=5, pady=5)
password_text = tk.Text(root, height=1, width=20)
password_text.grid(row=1, column=1, padx=5, pady=5)

confirm_button = tk.Button(root, text="Confirm", command=confirm_click)
confirm_button.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()

# sample_string_bytes = code.encode("ascii")
#
# base64_bytes = base64.b64encode(sample_string_bytes)
# base64_string = base64_bytes.decode("ascii")
#
# print(base64_string)

# file = open("data", "r")
# a = file.read().splitlines()[0]
# file.close()
#
# bb = a.encode("ascii")
#
# sb = base64.b64decode(bb)
# s = sb.decode("ascii")
#
# compiled = compile(s, '<string>', 'exec')
# exec(compiled)
