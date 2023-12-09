_menu_

InstallationFeaturesDemosDocumentationExamplesWhy?

_search_

_dark_mode_ _light_mode_ _brightness_auto_

_more_vert_

← Overview

Styling & Appearance

StylingTry styling NiceGUI elements!Tailwind CSSQuery SelectorColor ThemingDark mode

_Styling & Appearance_

Styling

_link_

NiceGUI uses the Quasar Framework version 1.0 and hence has its full design power. Each NiceGUI element provides a `props` method whose content is passed to the Quasar component: Have a look at the
Quasar documentation for all styling props. Props with a leading `:` can contain JavaScript expressions that are evaluated on the client. You can also apply Tailwind CSS utility classes with the
`classes` method.

If you really need to apply CSS, you can use the `style` method. Here the delimiter is `;` instead of a blank space.

All three functions also provide `remove` and `replace` parameters in case the predefined look is not wanted in a particular styling.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    ui.radio(['x', 'y', 'z'], value='x').props('inline color=green')
    ui.button(icon='touch_app').props('outline round').classes('shadow-lg')
    ui.label('Stylish!').style('color: #6E93D6; font-size: 200%; font-weight: 300')
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

Try styling NiceGUI elements!

_link_

Try out how Tailwind CSS classes, Quasar props, and CSS styles affect NiceGUI elements.

Select an element from those available and start styling it!

ui.button

_arrow_drop_down_

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    element = ui.button('element')
    
```

\[/code\]

`element.classes('`

`')`

`element.props('`

`')`

`element.style('`

`')`

\[code\]

```python


    ui.run()
    
```

\[/code\]

_circle_ _circle_ _circle_

NiceGUI

element

Tailwind CSS

_link_

Tailwind CSS is a CSS framework for rapidly building custom user interfaces. NiceGUI provides a fluent, auto-complete friendly interface for adding Tailwind classes to UI elements.

You can discover available classes by navigating the methods of the `tailwind` property. The builder pattern allows you to chain multiple classes together (as shown with "Label A"). You can also call
the `tailwind` property with a list of classes (as shown with "Label B").

Although this is very similar to using the `classes` method, it is more convenient for Tailwind classes due to auto-completion.

Last but not least, you can also predefine a style and apply it to multiple elements (labels C and D).

Note that sometimes Tailwind is overruled by Quasar styles, e.g. when using `ui.button('Button').tailwind('bg-red-500')`. This is a known limitation and not fully in our control. But we try to provide
solutions like the `color` parameter: `ui.button('Button', color='red-500')`.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import Tailwind, ui
    
    ui.label('Label A').tailwind.font_weight('extrabold').text_color('blue-600').background_color('orange-200')
    ui.label('Label B').tailwind('drop-shadow', 'font-bold', 'text-green-600')
    
    red_style = Tailwind().text_color('red-600').font_weight('bold')
    label_c = ui.label('Label C')
    red_style.apply(label_c)
    ui.label('Label D').tailwind(red_style)
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

Query Selector _link_

To manipulate elements like the document body, you can use the ui.query function. With the query result you can add classes, styles, and attributes like with every other UI element. This can be useful
for example to change the background color of the page (e.g. ui.query('body').classes('bg-green')).

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

See more...

Color Theming _link_

Sets the main colors (primary, secondary, accent, ...) used by Quasar.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    ui.button('Default', on_click=lambda: ui.colors())
    ui.button('Gray', on_click=lambda: ui.colors(primary='#555'))
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

See more...

Dark mode _link_

You can use this element to enable, disable or toggle dark mode on the page. The value None represents auto mode, which uses the client's system preference.

Note that this element overrides the dark parameter of the ui.run function and page decorators.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    dark = ui.dark_mode()
    ui.label('Switch mode:')
    ui.button('Dark', on_click=dark.enable)
    ui.button('Light', on_click=dark.disable)
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

See more...

Connection lost. Trying to reconnect...
