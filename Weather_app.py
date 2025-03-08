import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name!")
        return

    api_key = "7879b3e5f48cea6c3c9b042cafa3ec93"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        print("API Response:", data)

        if data["cod"] != 200:
            messagebox.showerror("Error", f"City not found! Error: {data['message']}")
            return

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]

        result_label.config(text=f"Temperature: {temp}°C\nHumidity: {humidity}%\nCondition: {description.title()}")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to get data: {e}")

root = tk.Tk()
root.title("Weather App")
root.geometry("300x250")

tk.Label(root, text="Enter City:", font=("Arial", 12)).pack(pady=5)
city_entry = tk.Entry(root, font=("Arial", 12))
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", command=get_weather, font=("Arial", 12)).pack(pady=5)
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
