import requests
from bs4 import BeautifulSoup
import time
from tkinter import *
from tkinter import ttk

site = "https://www.pogoda1.ru/moskva/"


def get_weather():
    url = site + day.get() + "-" + month.get() + "-" + year.get() + "/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    temperature = soup.find('div', class_='weather-now-temp').get_text()
    pressure = soup.find_all('span', class_='value')[0].get_text()
    humidity = soup.find_all('span', class_='value')[1].get_text()

    time.sleep(1)

    label_temp.config(text=("Температура           " + temperature + "C"), font=("Times New Roman", 14))
    label_press.config(text=("Атмосферное давление  " + pressure), font=("Times New Roman", 14))
    label_humid.config(text=("Влажность             " + humidity), font=("Times New Roman", 14))

root = Tk()
root.title("Погода в Москве за прошедшее время")
root.geometry("500x210")
root.resizable(False, False)

top_frame = Frame(root)
top_frame.pack(side=TOP, fill=X)
middle_frame = Frame(root)
middle_frame.pack(padx=10)
bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM, fill=X)

label = ttk.Label(top_frame, text="Введите дату в формате ДД-ММ-ГГГГ: ",
                  font=("Times New Roman", 14))
label.pack(side=LEFT, padx=10, pady=10)

sun_pic = PhotoImage(file="./sun.png")
label_sun = ttk.Label(bottom_frame, image=sun_pic)
label_sun.pack(side=LEFT, padx=10)

day = ttk.Entry(top_frame, width=3)
day.pack(side=LEFT, padx=5)

month = ttk.Entry(top_frame, width=3)
month.pack(side=LEFT, padx=5)

year = ttk.Entry(top_frame, width=6)
year.pack(side=LEFT, padx=5)

btn = ttk.Button(bottom_frame, text="Узнать погоду", command=get_weather)
btn.pack(side=RIGHT, padx=10)

label_temp = ttk.Label(middle_frame, text=("Температура           n/a C"),
                       font=("Times New Roman", 14), justify=LEFT)
label_temp.pack()

label_press = ttk.Label(middle_frame, justify=LEFT, text=("Атмосферное давление  n/a"),
                        font=("Times New Roman", 14))
label_press.pack()

label_humid = ttk.Label(middle_frame, justify=LEFT, text=("Влажность             n/a"),
                        font=("Times New Roman", 14))
label_humid.pack()

root.mainloop()
