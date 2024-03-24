import tkinter as tk
import json
import requests
import urllib.request
from io import BytesIO
from PIL import imageTk


def display_image(image_url: str):
    with urllib.request.urlopen(image_url)as url:
        image_data = url.read()    # download image

    image_stream = BytesIO(image_data)

    image = ImageTk.PhotoImage(Image.open(image_stream))

    image_label.config(image=image)
    image_label.image = image    # keeps reference to the image


def get_image_url():
    headers = {'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYWI4NTM0MTUtNTc1Zi00M2ZiLThlZDYtYjRmMjdiZmY2ZmExIiwidHlwZSI6ImFwaV90b2tlbiJ9.cO0f8KrChI613aymSCbGoE8CbESYU0RobJ4c81SCikA'}

    url = "https://api.edenai.run/v2/image/generation"
    payload = {
        "providers": "openai",
        "text": input_field.get(),
        "resolution": "256x256",
        "fallback_providers": ""
    }

    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)

    # Check if the 'openai' key exists in the response
    if 'openai' in result:
        openai_data = result['openai']

        # Check if the 'items' key exists and it's not empty
        if 'items' in openai_data and openai_data['items']:
            # Assuming there's only one item in the 'items' list
            image_resource_url = openai_data['items'][0].get('image_resource_url')
            return image_resource_url
        else:
            print("No items found in the response.")
            return None
    else:
        print("No 'openai' key found in the response.")
        return None


def render_image():
    print('clicked')
    try:
        error_label.place_forget()
        image_url = get_image_url()
    except KeyError:
        error_label.place(x=175, y=50)
    else:
        display_image(image_url)


window = tk.Tk()
window.title('AI Image Generator')
window.geometry('500x350')    # width x height

error_label = tk.Label(window, text='Prompt cannot be empty!', fg='red')

input_field = tk.Entry(window, width=14)
input_field.place(x=165, y=20)

image_label = tk.Label(window)
image_label.place(x=125, y=70)

generator_button = tk.Button(window, text='Create', height=1, command=render_image)
generator_button.place(x=300, y=17)

window.mainloop()
