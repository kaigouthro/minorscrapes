

← Overview

Controls

ButtonBadgeToggleRadio SelectionDropdown SelectionCheckboxSwitchSliderJoystickText InputTextareaNumber InputKnobColor InputColor PickerDate InputTime InputFile Upload

 _Controls_

Button

This element is based on Quasar's QBtn component.

The color parameter accepts a Quasar color, a Tailwind color, or a CSS color. If a Quasar color is used, the button will be styled according to the Quasar theme including the color of the text. Note
that there are colors like "red" being both a Quasar color and a CSS color. In such cases the Quasar color will be used.

main.py

[code]
```python




    from nicegui import ui
    
    ui.button('Click me!', on_click=lambda: ui.notify('You clicked me!'))
    
    ui.run()
    


```
[/code]


NiceGUI

See more...

Badge

A badge element wrapping Quasar's QBadge component.

main.py

[code]
```python




    from nicegui import ui
    
    with ui.button('Click me!', on_click=lambda: badge.set_text(int(badge.text) + 1)):
        badge = ui.badge('0', color='red').props('floating')
    
    ui.run()
    


```
[/code]


NiceGUI

See more...

Toggle

This element is based on Quasar's QBtnToggle component.

The options can be specified as a list of values, or as a dictionary mapping values to labels. After manipulating the options, call update() to update the options in the UI.

main.py

[code]
```python




    from nicegui import ui
    
    toggle1 = ui.toggle([1, 2, 3], value=1)
    toggle2 = ui.toggle({1: 'A', 2: 'B', 3: 'C'}).bind_value(toggle1, 'value')
    
    ui.run()
    


```
[/code]


NiceGUI

See more...

Radio Selection

This element is based on Quasar's QRadio component.

The options can be specified as a list of values, or as a dictionary mapping values to labels. After manipulating the options, call update() to update the options in the UI.

main.py

[code]
```python




    from nicegui import ui
    
    radio1 = ui.radio([1, 2, 3], value=1).props('inline')
    radio2 = ui.radio({1: 'A', 2: 'B', 3: 'C'}).props('inline').bind_value(radio1, 'value')
    
    ui.run()
    


```
[/code]


NiceGUI

See more...

Dropdown Selection

This element is based on Quasar's QSelect component.

The options can be specified as a list of values, or as a dictionary mapping values to labels. After manipulating the options, call update() to update the options in the UI.

If with_input is True, an input field is shown to filter the options.

If new_value_mode is not None, it implies with_input=True and the user can enter new values in the input field. See Quasar's documentation for details. Note that this mode is ineffective when setting
the value property programmatically.

main.py

[code]
```python




    from nicegui import ui
    
    select1 = ui.select([1, 2, 3], value=1)
    select2 = ui.select({1: 'One', 2: 'Two', 3: 'Three'}).bind_value(select1, 'value')
    
    ui.run()
    


```
[/code]


NiceGUI

See more...

Checkbox

This element is based on Quasar's QCheckbox component.

main.py

[code]
```python




    from nicegui import ui
    
    checkbox = ui.checkbox('check me')
    ui.label('Check!').bind_visibility_from(checkbox, 'value')
    
    ui.run()
    


```
[/code]


NiceGUI

See more...

Switch

This element is based on Quasar's QToggle component.

main.py

[code]
```python




    from nicegui import ui
    
    switch = ui.switch('switch me')
    ui.label('Switch!').bind_visibility_from(switch, 'value')
    
    ui.run()
    


```
[/code]


NiceGUI

See more...

Slider

This element is based on Quasar's QSlider component.

main.py

[code]
```python




    from nicegui import ui
    
    slider = ui.slider(min=0, max=100, value=50)
    ui.label().bind_text_from(slider, 'value')
    
    ui.run()
    


```
[/code]


NiceGUI

See more...

Joystick

Create a joystick based on nipple.js.

main.py

[code]
```python




    from nicegui import ui
    
    ui.joystick(color='blue', size=50,
                on_move=lambda e: coordinates.set_text(f"{e.x:.3f}, {e.y:.3f}"),
                on_end=lambda _: coordinates.set_text('0, 0'))
    coordinates = ui.label('0, 0')
    
    ui.run()
    


```
[/code]


NiceGUI

See more...

Text Input

This element is based on Quasar's QInput component.

The on_change event is called on every keystroke and the value updates accordingly. If you want to wait until the user confirms the input, you can register a custom event callback, e.g.
ui.input(...).on('keydown.enter', ...) or ui.input(...).on('blur', ...).

You can use the validation parameter to define a dictionary of validation rules. The key of the first rule that fails will be displayed as an error message.

Note about styling the input: Quasar's QInput component is a wrapper around a native input element. This means that you cannot style the input directly, but you can use the input-class and input-style
props to style the native input element. See the "Style" props section on the QInput documentation for more details.

main.py

[code]
```python




    from nicegui import ui
    
    ui.input(label='Text', placeholder='start typing',
             on_change=lambda e: result.set_text('you typed: ' + e.value),
             validation={'Input too long': lambda value: len(value) < 20})
    result = ui.label()
    
    ui.run()
    


```
[/code]


NiceGUI

See more...

Textarea

This element is based on Quasar's QInput component. The type is set to textarea to create a multi-line text input.

You can use the validation parameter to define a dictionary of validation rules. The key of the first rule that fails will be displayed as an error message.

main.py

[code]
```python




    from nicegui import ui
    
    ui.textarea(label='Text', placeholder='start typing',
                on_change=lambda e: result.set_text('you typed: ' + e.value))
    result = ui.label()
    
    ui.run()
    


```
[/code]


NiceGUI

See more...

Number Input

This element is based on Quasar's QInput component.

You can use the validation parameter to define a dictionary of validation rules. The key of the first rule that fails will be displayed as an error message.

main.py

[code]
```python




    from nicegui import ui
    
    ui.number(label='Number', value=3.1415927, format='%.2f',
              on_change=lambda e: result.set_text(f'you entered: {e.value}'))
    result = ui.label()
    
    ui.run()
    


```
[/code]


NiceGUI

See more...

Knob

This element is based on Quasar's QKnob component. The element is used to take a number input from the user through mouse/touch panning.

main.py

[code]
```python




    from nicegui import ui
    
    knob = ui.knob(0.3, show_value=True)
    
    with ui.knob(color='orange', track_color='grey-2').bind_value(knob, 'value'):
        ui.icon('volume_up')
    
    ui.run()
    


```
[/code]


NiceGUI

See more...

Color Input

This element extends Quasar's QInput component with a color picker.

main.py

[code]
```python




    from nicegui import ui
    
    label = ui.label('Change my color!')
    ui.color_input(label='Color', value='#000000',
                   on_change=lambda e: label.style(f'color:{e.value}'))
    
    ui.run()
    


```
[/code]


NiceGUI

See more...

Color Picker

This element is based on Quasar's QMenu and QColor components.

main.py

[code]
```python




    from nicegui import ui
    
    with ui.button(icon='colorize') as button:
        ui.color_picker(on_pick=lambda e: button.style(f'background-color:{e.color}!important'))
    
    ui.run()
    


```
[/code]


NiceGUI

See more...

Date Input

This element is based on Quasar's QDate component. The date is a string in the format defined by the mask parameter.

You can also use the range or multiple props to select a range of dates or multiple dates:

[code]
```python




    ui.date({'from': '2023-01-01', 'to': '2023-01-05'}).props('range')
    ui.date(['2023-01-01', '2023-01-02', '2023-01-03']).props('multiple')
    ui.date([{'from': '2023-01-01', 'to': '2023-01-05'}, '2023-01-07']).props('multiple range')


```
[/code]


main.py

[code]
```python




    from nicegui import ui
    
    ui.date(value='2023-01-01', on_change=lambda e: result.set_text(e.value))
    result = ui.label()
    
    ui.run()
    


```
[/code]


NiceGUI

See more...

Time Input

This element is based on Quasar's QTime component. The time is a string in the format defined by the mask parameter.

main.py

[code]
```python




    from nicegui import ui
    
    ui.time(value='12:00', on_change=lambda e: result.set_text(e.value))
    result = ui.label()
    
    ui.run()
    


```
[/code]


NiceGUI

See more...

File Upload

Based on Quasar's QUploader component.

main.py

[code]
```python




    from nicegui import ui
    
    ui.upload(on_upload=lambda e: ui.notify(f'Uploaded {e.name}')).classes('max-w-full')
    
    ui.run()
    


```
[/code]


NiceGUI

See more...

Connection lost. Trying to reconnect...

