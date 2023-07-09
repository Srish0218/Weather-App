import requests
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import win32com.client as wincom
import pytz
from PIL import Image, ImageTk
from prettytable import PrettyTable



root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)



def getWeather(event=None):
    global city
    city=textfield.get()
    geolocator=Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(city)
    if location is None or not hasattr(location, 'longitude') or not hasattr(location, 'latitude'):
        messagebox.showinfo("Place Not Found", "The place was not found. Please search again.")
        return

    obj = TimezoneFinder()
    lng = location.longitude
    lat = location.latitude

    result= obj.timezone_at(lng=location.longitude,lat=location.latitude)
    home=pytz.timezone(result)
    localtime=datetime.now(home)
    currenttime=localtime.strftime("%I: %M %p")
    clock.config(text=currenttime)
    name.config(text="CURRENT WEATHER")
    # print(result)



    #weather
    api=f"https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=646824f2b7b86caffec1d0b16ea77f79"
    jsondata=requests.get(api).json()

    condition= jsondata['weather'][0]['main']
    description = jsondata['weather'][0]['description']
    # capitalize the description
    description = description.capitalize()
    temp=int(jsondata['main']['temp']-275.15)
    pressure= jsondata['main']['pressure']
    humidity= jsondata['main']['humidity']
    wind= jsondata['wind']['speed']



    table = PrettyTable()
    table.field_names = ["City", "Condition", "Description", "Temperature (°C)", "Pressure", "Humidity", "Wind Speed",
                         "Latitude", "Longitude"]
    table.add_row([city, condition, description, temp, pressure, humidity, wind, lat, lng])

    # Print the table
    print(table)

    t.config(text=(temp,"°"))
    c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))
    w.config(text=wind)
    h.config(text=humidity)
    d.config(text=description)
    p.config(text=pressure)

    root.after(300, speakWeather, city, temp)



    if "cloud" in condition.lower():
        logo_img = PhotoImage(file="cloud_logo.png")
    elif "rain" in condition.lower():
        logo_img = Image.open("rain_logo.png")
        resized_logo_img = logo_img.resize((254, 242), Image.LANCZOS)
        logo_img = ImageTk.PhotoImage(resized_logo_img)
    elif "sun" in condition.lower():
        logo_img = PhotoImage(file="sun_logo.png")
    elif "mist" in condition.lower():
        logo_img = Image.open("mist_logo.png")
        resized_logo_img = logo_img.resize((254, 242), Image.LANCZOS)
        logo_img = ImageTk.PhotoImage(resized_logo_img)
    else:
        logo_img = PhotoImage(file="logo.png")

    logo.config(image=logo_img)
    logo.image = logo_img

    words = description.split()
    if len(words) > 2:
        # Decrease the font size for long descriptions
        d.config(text=description, font=("arial", 15, "bold"))
    else:
        d.config(text=description, font=("arial", 20, "bold"))

def speakWeather(city, temp):
    # Text-to-speech
    speak = wincom.Dispatch("SAPI.SpVoice")
    text = f"The current weather in {city} is {temp} degrees"
    speak.Speak(text)





# search
Search_img = PhotoImage(file="search.png")
myimage = Label(image=Search_img)
myimage.place(x=150, y=20)


textfield=tk.Entry(root, justify="center", width=17, font=("poppins",25,"bold"), bg="#404040", border=0, fg="white" )
textfield.place(x=190,y=40)
textfield.focus()

textfield.bind('<Return>', getWeather)


Search_icon=PhotoImage(file="search_icon.png")
myimageicon = Button(image=Search_icon,borderwidth=-0, cursor="hand2", bg="#404040", command=getWeather)
myimageicon.place(x=520, y=35)

#logo
Logo_img=PhotoImage(file="logo.png")
logo=Label(image=Logo_img)
logo.place(x=200,y=100)

#bottom box
boxframe=PhotoImage(file="box.png")
frame=Label(image=boxframe)
frame.pack(padx=5,pady=5,side=BOTTOM)

# time
name=Label(root, font=("arial",15,"bold"),bg=None)
name.place(x=20,y=100)
clock=Label(root,font=("Helventica", 20))
clock.place(x=20,y=130)


#label
label1=Label(root,text="WIND",font=("Helvetica",15,"bold"),fg="white", bg="#1ab5ef")
label1.place(x=120,y=400)
label2=Label(root,text="HUMIDITY",font=("Helvetica",15,"bold"),fg="white", bg="#1ab5ef")
label2.place(x=250,y=400)
label3=Label(root,text="DESCRIPTION",font=("Helvetica",15,"bold"),fg="white", bg="#1ab5ef")
label3.place(x=410,y=400)
label4=Label(root,text="PRESSURE",font=("Helvetica",15,"bold"),fg="white", bg="#1ab5ef")
label4.place(x=650,y=400)

t=Label(font=("arial",70,"bold"), fg="#ee666d",bg=None)
t.place(x=480,y=150)
c=Label(font=("arial",15,"bold"),bg=None)
c.place(x=480,y=250)

w=Label(text="...",font=("arial",20,"bold"), bg="#1ab5ef")
w.place(x=120,y=430)
h=Label(text="...",font=("arial",20,"bold"), bg="#1ab5ef")
h.place(x=270,y=430)
d=Label(text="...",font=("arial",20,"bold"), bg="#1ab5ef")
d.place(x=410,y=430)
p=Label(text="...",font=("arial",20,"bold"), bg="#1ab5ef")
p.place(x=650,y=430)


root.mainloop()

