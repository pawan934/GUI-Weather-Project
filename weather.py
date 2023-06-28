import tkinter as tk
from PIL import Image, ImageTk
import requests, json

root = tk.Tk()

root.title('Weather App')
root.geometry('600x500')

# 16b16666982b3b8bcfd2447d2baa047f

# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

def format_response(weather):
    try:
        city=weather['name']
        condiion=weather['weather'][0]['description']
        temp=weather['main']['temp']
        final_str = 'City:%s\nCondition:%s\ntemp:%s'%(city, condiion, temp)
    except:
        final_str = 'There was s problam retrieving taht information'
    return final_str



def get_weather(city):
    weather_key= "16b16666982b3b8bcfd2447d2baa047f"
    url = 'https://api.openweathermap.org/data/2.5/weather'
    parmas = {'appid':weather_key, 'q':city, 'units':'imperial'}
    response = requests.get(url, parmas)
    # print (response.json())
    weather = response.json()

    # print(weather['name'])
    # print(weather['weather'][0]['description'])
    # print(weather['main']['temp'])


    result["text"]=format_response(weather)
    # icon_name = weather['weather'][0]['icon']
    # open_image(icon_name)

    def open_image(icon_name):
        pass


img = Image.open('./bg.jpg')
img = img.resize((600,500))
img_photo = ImageTk.PhotoImage(img)


bg_lbl = tk.Label(root, image=img_photo)
bg_lbl.place(x=0, y=0, width=600, height=500)


heading = tk.Label(bg_lbl, text='Earth including over 200,000 cities !', bg='#8F9D9E' ,fg='black',font=('times new roman', 18, 'bold'))
heading.place(x=80, y=20)


frame1 = tk.Frame(bg_lbl, bg='lightblue', bd=5)
frame1.place(x=80, y=60, width=460, height=50)


tst_box = tk.Entry(frame1, font=('times new roman', 25), width=18)
tst_box.grid(row=0, column=1, sticky='w')


btn = tk.Button(frame1, text='Get Weather', command=lambda: get_weather(tst_box.get()) ,bg='lightgreen' ,fg='black',font=('times new roman', 16, 'bold'))
btn.grid(row=0, column=2, padx=5)


frame2 = tk.Frame(bg_lbl, bg='lightblue', bd=5)
frame2.place(x=80, y=130, width=460, height=300)

result = tk.Label(frame2, font=40, bg='white',justify='left', anchor='nw')
result.place(relwidth=1, relheight=1)

root.mainloop()