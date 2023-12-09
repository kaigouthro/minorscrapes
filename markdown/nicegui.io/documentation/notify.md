InstallationFeaturesDemosDocumentationExamplesWhy?

_search_

_dark_mode_ _light_mode_ _brightness_auto_

_more_vert_

← Overview

**Demos**

Notification TypesMultiline Notifications

Documentation

ui. _notify_

Displays a notification on the screen.

message:

content of the notification

position:

position on the screen ("top-left", "top-right", "bottom-left", "bottom-right", "top", "bottom", "left", "right" or "center", default: "bottom")

close_button:

optional label of a button to dismiss the notification (default: False)

type:

optional type ("positive", "negative", "warning", "info" or "ongoing")

color:

optional color name

multi_line:

enable multi-line notifications

Note: You can pass additional keyword arguments according to Quasar's Notify API.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    ui.button('Say hi!', on_click=lambda: ui.notify('Hi!', close_button='OK'))
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

Notification Types

_link_

There are different types that can be used to indicate the nature of the notification.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    ui.button('negative', on_click=lambda: ui.notify('error', type='negative'))
    ui.button('positive', on_click=lambda: ui.notify('success', type='positive'))
    ui.button('warning', on_click=lambda: ui.notify('warning', type='warning'))
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

Multiline Notifications

_link_

To allow a notification text to span multiple lines, it is sufficient to set `multi_line=True`. If manual newline breaks are required (e.g. \` need to define a CSS style and pass it to the notification
as shown in the example.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    ui.html('<style>.multi-line-notification { white-space: pre-line; }</style>')
    ui.button('show', on_click=lambda: ui.notify(
        'Lorem ipsum dolor sit amet, consectetur adipisicing elit. \n'
        'Hic quisquam non ad sit assumenda consequuntur esse inventore officia. \n'
        'Corrupti reiciendis impedit vel, '
        'fugit odit quisquam quae porro exercitationem eveniet quasi.',
        multi_line=True,
        classes='multi-line-notification',
    ))
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

Connection lost. Trying to reconnect...
