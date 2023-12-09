InstallationFeaturesDemosDocumentationExamplesWhy?

_search_

_dark_mode_ _light_mode_ _brightness_auto_

_more_vert_

← Overview

**Demos**

Set background gradientModify default page padding

Documentation

ui. _query_

To manipulate elements like the document body, you can use the ui.query function. With the query result you can add classes, styles, and attributes like with every other UI element. This can be useful
for example to change the background color of the page (e.g. ui.query('body').classes('bg-green')).

selector:

the CSS selector (e.g. "body", "#my-id", ".my-class", "div > p")

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    def set_background(color: str) -> None:
        ui.query('body').style(f'background-color: {color}')
    
    ui.button('Blue', on_click=lambda: set_background('#ddeeff'))
    ui.button('Orange', on_click=lambda: set_background('#ffeedd'))
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

Set background gradient

_link_

It's easy to set a background gradient, image or similar. See w3schools.com for more information about setting background with CSS.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    ui.query('body').classes('bg-gradient-to-t from-blue-400 to-blue-100')
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

Modify default page padding

_link_

By default, NiceGUI provides a built-in padding around the content of the page. You can modify it using the class selector `.nicegui-content`.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    ui.query('.nicegui-content').classes('p-0')
    with ui.column().classes('h-screen w-full bg-gray-400 justify-between'):
        ui.label('top left')
        ui.label('bottom right').classes('self-end')
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

Connection lost. Trying to reconnect...
