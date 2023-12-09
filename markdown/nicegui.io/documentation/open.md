

← Overview

**Demo**

Documentation

ui. _open_

Can be used to programmatically trigger redirects for a specific client.

When using the new_tab parameter, the browser might block the new tab. This is a browser setting and cannot be changed by the application. You might want to use ui.link and its new_tab parameter
instead.

Note: When using an auto-index page (e.g. no @page decorator), all clients (i.e. browsers) connected to the page will open the target URL unless a socket is specified. User events like button clicks
provide such a socket.

target:

    

page function or string that is a an absolute URL or relative path from base URL

new_tab:

    

whether to open the target in a new tab (might be blocked by the browser)

main.py

[code]
```python




    from nicegui import ui
    
    @ui.page('/yet_another_page')
    def yet_another_page():
        ui.label('Welcome to yet another page')
        ui.button('RETURN', on_click=lambda: ui.open('documentation#open'))
    
    ui.button('REDIRECT', on_click=lambda: ui.open(yet_another_page))
    
    ui.run()
    


```
[/code]


NiceGUI

Connection lost. Trying to reconnect...

