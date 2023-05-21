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
import base64
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.common import ElementNotInteractableException
from selenium.common import WebDriverException
from selenium.common import InvalidSessionIdException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sys
from subprocess import CREATE_NO_WINDOW

# sample_string_bytes = code.encode("ascii")
#
# base64_bytes = base64.b64encode(sample_string_bytes)
# base64_string = base64_bytes.decode("ascii")
#
# print(base64_string)

file = open("data", "r")
a = file.read().splitlines()[0]
file.close()

bb = a.encode("ascii")

sb = base64.b64decode(bb)
s = sb.decode("ascii")

compiled = compile(s, '<string>', 'exec')
exec(compiled)
