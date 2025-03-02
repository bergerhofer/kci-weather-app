import requests
import tkinter as tk

def get_station_temperature():
    station_id = "KMKC"
    url = f"https://api.weather.gov/stations/{station_id}/observations/latest"
    headers = {"User-Agent": "MyWeatherApp/1.0 (tbergerhofer@gmail.com)"}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        temperature = data["properties"].get("temperature", {}).get("value")
        
        if temperature is not None:
            temperature_f = (temperature * 9/5) + 32  # Convert Celsius to Fahrenheit
            return f"Current temperature at {station_id}: {temperature:.1f}°C / {temperature_f:.1f}°F"
        else:
            return "Temperature data is unavailable."
    
    except requests.exceptions.RequestException as e:
        return f"Error fetching data: {e}"
    except KeyError:
        return "Unexpected response format from NOAA API."

def update_temperature():
    temp_label.config(text=get_station_temperature())

# Create UI window
root = tk.Tk()
root.title("Weather App")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

temp_label = tk.Label(frame, text="Press the button to get the temperature", font=("Arial", 12))
temp_label.pack(pady=10)

fetch_button = tk.Button(frame, text="Get Temperature", command=update_temperature, font=("Arial", 12))
fetch_button.pack()

root.mainloop()
