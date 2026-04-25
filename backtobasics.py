from selenium import webdriver
from selenium.webdriver.common.by import By
from tkinter import *
import tkinter as tk
driver=webdriver.Chrome()
driver.get("https://www.amazon.com/Apple-2025-MacBook-Laptop-10%E2%80%91core/dp/B0FWD623D1/ref=sr_1_2_sspa?crid=3GWVZRVJ3IK2W&dib=eyJ2IjoiMSJ9.LmX7Km5OFR0QV0KMCCeYI2FME-0Xj8yacXHzHlhnWauTiF69QXt3h6xzOf-XG4CwJD8Mec7TbWCEMQj5JPPIfntuGdbKPEsA6l_ETvQeE_4m-fR88hIUxfjq5vErSihjGKqehZjE8xqG3SH2xiMDwEwDhGQ6Ygsjw7VjkknruL3p_NkO3RokMyuxw_DHhiMzwfxcpw-71pKqSlYyaI-oLiQQhui2u5ppWzYqmdGvfs0.YmZeL4RzOXN0RAL-a6aeZgIxC9j4Sm7SH6Y8SohRBNQ&dib_tag=se&keywords=macbook%2Bpro&qid=1776539907&sprefix=macbook%2Bpro%2Caps%2C211&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1")
print("success")

whole_price=driver.find_element(By.CLASS_NAME,value="a-price-whole")
print("success")
portion_price=driver.find_element(By.CLASS_NAME,value="a-price-fraction")
print("success")
current=f"The current price of the macbook pro you are looking for is {whole_price.text}.{portion_price.text}"
print(current)
