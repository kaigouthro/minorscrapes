

← Overview

**Demo**

Documentation

ui. _download_

Function to trigger the download of a file.

src:

    

target URL or local path of the file which should be downloaded

filename:

    

name of the file to download (default: name of the file on the server)

main.py

[code]
```python




    from nicegui import ui
    
    ui.button('NiceGUI Logo', on_click=lambda: ui.download('https://nicegui.io/logo.png'))
    
    ui.run()
    


```
[/code]


NiceGUI

Connection lost. Trying to reconnect...

