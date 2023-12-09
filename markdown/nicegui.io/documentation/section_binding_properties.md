_menu_

InstallationFeaturesDemosDocumentationExamplesWhy?

_search_

_dark_mode_ _light_mode_ _brightness_auto_

_more_vert_

← Overview

Binding Properties

Bindings

_Binding Properties_

Bindings _link_

NiceGUI is able to directly bind UI elements to models. Binding is possible for UI element properties like text, value or visibility and for model properties that are (nested) class attributes. Each
element provides methods like bind_value and bind_visibility to create a two-way binding with the corresponding property. To define a one-way binding use the \_from and \_to variants of these methods.
Just pass a property of the model as parameter to these methods to create the binding.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    class Demo:
        def __init__(self):
            self.number = 1
    
    demo = Demo()
    v = ui.checkbox('visible', value=True)
    with ui.column().bind_visibility_from(v, 'value'):
        ui.slider(min=1, max=3).bind_value(demo, 'number')
        ui.toggle({1: 'A', 2: 'B', 3: 'C'}).bind_value(demo, 'number')
        ui.number().bind_value(demo, 'number')
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

See more...

Connection lost. Trying to reconnect...
