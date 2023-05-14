import random
import time
import tkinter.messagebox

import pyautogui
import tkinter as tk
import threading
import urllib.request
import json
import requests
import base64

login_data = {
    'api_dev_key': "hh0Lpv00OHio-Sc-XSvvraLbsiT1f4Ru",
    'api_user_name': 'TastyCake098',
    'api_user_password': 'tomer192837465'
}


def generate(data):
    return requests.post("https://pastebin.com/api/api_login.php", data=data)


response = urllib.request.urlopen("https://pastebin.com/raw/XXn7nYNd")
data = response.read().decode("utf-8")
json_data = json.loads(data)

loggedUsername = ""


def containsuser(user):
    return user in json_data


def getdata(user, d):
    return json_data[user][d]


def updatedata():
    global response
    global data
    global json_data

    response = urllib.request.urlopen("https://pastebin.com/raw/XXn7nYNd")
    data = response.read().decode("utf-8")
    json_data = json.loads(data)


root = tk.Tk()
root.geometry("250x100")
root.title("Auto Magnilearn")

toggle = False

f = open("text", 'r')

texts = f.read().splitlines()


def run():
    global toggle
    toggle = not toggle

    if toggle:
        root.state(newstate='iconic')
        time.sleep(1)
        pyautogui.click()
        pyautogui.moveTo(1530, 800)

    def send_messages():
        times = 0
        times2 = 0
        times3 = 0
        times4 = 0
        times5 = 0

        while toggle:
            time.sleep(0.5)
            pyautogui.typewrite(random.choice(texts))
            times += 1
            times2 += 1
            times3 += 1
            times4 += 1
            times5 += 1

            if loggedUsername == "":
                tkinter.messagebox.showerror("You aren't logged in")
                root.destroy()
            if times >= 20:
                times = 0
                pyautogui.press("enter")
            if times2 >= 24:
                times2 = 0
                pyautogui.click()
            if times3 >= 60:
                times3 = 0
                pyautogui.press("f5")
            if times4 >= 3000:
                times4 = 0
                pyautogui.moveTo(1060, 815)
                pyautogui.click()
                time.sleep(0.5)
                pyautogui.moveTo(1150, 738)
                pyautogui.click()
                time.sleep(5)
                pyautogui.moveTo(1050, 125)
                pyautogui.click()
                time.sleep(3)
                pyautogui.moveTo(1530, 800)
            if times5 >= 5:
                if not containsuser(loggedUsername):
                    updatedata()
                    tkinter.messagebox.showerror("Your time has expired.")
                    root.destroy()

    if toggle:
        t = threading.Thread(target=send_messages)
        t.start()


def confirm_click():
    global loggedUsername
    username = username_text.get("1.0", tk.END).strip()
    password = password_text.get("1.0", tk.END).strip()

    if not containsuser(username):
        tkinter.messagebox.showerror("Username is incorrect.")
    else:
        if password != getdata(username, "password"):
            tkinter.messagebox.showerror("Password is incorrect.")
        else:
            loggedUsername = username
            tkinter.messagebox.showinfo("Logged in successfully.")
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