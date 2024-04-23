import subprocess
from nicegui import ui
import requests

base_url = "http://127.0.0.1:5000"
top_results = {}
start_process = True

if start_process:
    subprocess.Popen(["python", "processor.py"])
    start_process = False

def on_start_click():
    # Send a GET request to the init endpoint of the Flask server
    response = requests.get(f"{base_url}/init")

    # Check if the response status code is 200
    if response.status_code == 200:
        print("Flask server initialized successfully.")

        # Display a notification message to the user
        ui.notify(response.json()['message'], type='positive')
    else:
        print("Error:", response.status_code, response.text)

        # Display an error notification message to the user
        ui.notify(response.json()['error'], type='negative')


def on_search_button_click():
    search_text = result.value
    # Define the URL for the POST request
    url = f"{base_url}/process_query"

    # Define any additional data to send in the POST request
    data = {"query": search_text}

    # Send the POST request using requests library
    response = requests.post(url, json=data)

    # Handle the response based on status code
    if response.status_code == 200:
        global top_results
        top_results = response.json()['results']
        refresh_search_list()

        # Display a notification message to the user
        ui.notify(response.json()['message'], type='positive', color='#00ff00')  # Green color
    else:
        print("Error:", response.status_code, response.text)

        # Display an error notification message to the user
        ui.notify(response.json()['error'], type='negative', color='#ff0000')  # Red color


@ui.refreshable
def refresh_search_list():
    with ui.list().classes('self.center'):
        for i in top_results:
            ui.item(i['article'], on_click=lambda x: ui.navigate().to(i['link'])).style('color: green')


ui.button("Start", on_click=on_start_click, color='primary')  # Blue color

with ui.row().classes('self-center'):
    result = ui.input(placeholder='start typing').props(
        'wide-input rounded outlined dense self-center').classes('w-96')
    ui.button("Search", on_click=on_search_button_click, color='primary')  # Blue color

refresh_search_list()

# Run the UI
ui.run()
