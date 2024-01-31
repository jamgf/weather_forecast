import tkinter as tk
import requests

def get_weather():
    api_key = "30d4741c779ba94c470ca1f63045390a"
    city = entry.get()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    weather_data = response.json()

    if weather_data["cod"] != "404":
        weather_info = weather_data["main"]
        temperature = weather_info["temp"]
        humidity = weather_info["humidity"]
        description = weather_data["weather"][0]["description"]
        weather_label.config(text=f"Temperature: {temperature}°C\nHumidity: {humidity}%\nDescription: {description.capitalize()}")
    else:
        weather_label.config(text="City not found!")


root = tk.Tk()
root.title("Weather Forecast")

canvas = tk.Canvas(root, height=400, width=800)
canvas.pack()

frame = tk.Frame(root, bg="#80c1ff", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

entry = tk.Entry(frame, font=("Courier", 14))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Let's check the weather", font=("Courier", 14), command=get_weather)
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg="#80c1ff", bd=10)
lower_frame.place(relx=0.5, rely=0.3, relwidth=0.75, relheight=0.6, anchor="n")

weather_label = tk.Label(lower_frame, font=("Courier", 18), anchor="nw", justify="left", bd=4)
weather_label.place(relwidth=1, relheight=1)

root.mainloop()