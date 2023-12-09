

← Overview

**Demos**

AutocompletionClearableStyling

 **Reference**

PropertiesMethodsInherited from

Documentation

ui. _input_

This element is based on Quasar's QInput component.

The on_change event is called on every keystroke and the value updates accordingly. If you want to wait until the user confirms the input, you can register a custom event callback, e.g.
ui.input(...).on('keydown.enter', ...) or ui.input(...).on('blur', ...).

You can use the validation parameter to define a dictionary of validation rules. The key of the first rule that fails will be displayed as an error message.

Note about styling the input: Quasar's QInput component is a wrapper around a native input element. This means that you cannot style the input directly, but you can use the input-class and input-style
props to style the native input element. See the "Style" props section on the QInput documentation for more details.

label:

    

displayed label for the text input

placeholder:

    

text to show if no value is entered

value:

    

the current value of the text input

password:

    

whether to hide the input (default: False)

password_toggle_button:

    

whether to show a button to toggle the password visibility (default: False)

on_change:

    

callback to execute when the value changes

autocomplete:

    

optional list of strings for autocompletion

validation:

    

dictionary of validation rules, e.g. {'Too long!': lambda value: len(value) < 3}

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

Autocompletion

The `autocomplete` feature provides suggestions as you type, making input easier and faster. The parameter `options` is a list of strings that contains the available options that will appear.

main.py

[code]
```python




    from nicegui import ui
    
    options = ['AutoComplete', 'NiceGUI', 'Awesome']
    ui.input(label='Text', placeholder='start typing', autocomplete=options)
    
    ui.run()
    


```
[/code]


NiceGUI

Clearable

The `clearable` prop from Quasar adds a button to the input that clears the text.

main.py

[code]
```python




    from nicegui import ui
    
    i = ui.input(value='some text').props('clearable')
    ui.label().bind_text_from(i, 'value')
    
    ui.run()
    


```
[/code]


NiceGUI

Styling

Quasar has a lot of props to change the appearance. It is even possible to style the underlying input with `input-style` and `input-class` props and use the provided slots to add custom elements.

main.py

[code]
```python




    from nicegui import ui
    
    ui.input(placeholder='start typing').props('rounded outlined dense')
    ui.input('styling', value='some text') \
        .props('input-style="color: blue" input-class="font-mono"')
    with ui.input(value='custom clear button').classes('w-64') as i:
        ui.button(color='orange-8', on_click=lambda: i.set_value(None), icon='delete') \
            .props('flat dense').bind_visibility_from(i, 'value')
    
    ui.run()
    


```
[/code]


NiceGUI

## Reference

Properties

 **`enabled`**`: BindableProperty`

**`error`**`: Optional[str]`

The latest error message from the validation functions.

**`is_deleted`**`: 'bool'`

Whether the element has been deleted.

**`is_ignoring_events`**`: bool`

Return whether the element is currently ignoring events.

**`value`**`: BindableProperty`

**`visible`**`: BindableProperty`

Methods

 **`add_slot`**`(name: str, template: Optional[str] = None) -> Slot`

Add a slot to the element.

> name:
>  
>
> name of the slot
>
> template:
>  
>
> Vue template of the slot
>
> return:
>  
>
> the slot

**`bind_enabled`**`(target_object: Any, target_name: str = 'enabled', forward: Callable[..., Any] = [...], backward: Callable[..., Any] = [...]) -> Self`

Bind the enabled state of this element to the target object's target_name property.

> The binding works both ways, from this element to the target and from the target to this element.
>
> target_object:
>  
>
> The object to bind to.
>
> target_name:
>  
>
> The name of the property to bind to.
>
> forward:
>  
>
> A function to apply to the value before applying it to the target.
>
> backward:
>  
>
> A function to apply to the value before applying it to this element.

**`bind_enabled_from`**`(target_object: Any, target_name: str = 'enabled', backward: Callable[..., Any] = [...]) -> Self`

Bind the enabled state of this element from the target object's target_name property.

> The binding works one way only, from the target to this element.
>
> target_object:
>  
>
> The object to bind from.
>
> target_name:
>  
>
> The name of the property to bind from.
>
> backward:
>  
>
> A function to apply to the value before applying it to this element.

**`bind_enabled_to`**`(target_object: Any, target_name: str = 'enabled', forward: Callable[..., Any] = [...]) -> Self`

Bind the enabled state of this element to the target object's target_name property.

> The binding works one way only, from this element to the target.
>
> target_object:
>  
>
> The object to bind to.
>
> target_name:
>  
>
> The name of the property to bind to.
>
> forward:
>  
>
> A function to apply to the value before applying it to the target.

**`bind_value`**`(target_object: Any, target_name: str = 'value', forward: Callable[..., Any] = [...], backward: Callable[..., Any] = [...]) -> Self`

Bind the value of this element to the target object's target_name property.

> The binding works both ways, from this element to the target and from the target to this element.
>
> target_object:
>  
>
> The object to bind to.
>
> target_name:
>  
>
> The name of the property to bind to.
>
> forward:
>  
>
> A function to apply to the value before applying it to the target.
>
> backward:
>  
>
> A function to apply to the value before applying it to this element.

**`bind_value_from`**`(target_object: Any, target_name: str = 'value', backward: Callable[..., Any] = [...]) -> Self`

Bind the value of this element from the target object's target_name property.

> The binding works one way only, from the target to this element.
>
> target_object:
>  
>
> The object to bind from.
>
> target_name:
>  
>
> The name of the property to bind from.
>
> backward:
>  
>
> A function to apply to the value before applying it to this element.

**`bind_value_to`**`(target_object: Any, target_name: str = 'value', forward: Callable[..., Any] = [...]) -> Self`

Bind the value of this element to the target object's target_name property.

> The binding works one way only, from this element to the target.
>
> target_object:
>  
>
> The object to bind to.
>
> target_name:
>  
>
> The name of the property to bind to.
>
> forward:
>  
>
> A function to apply to the value before applying it to the target.

**`bind_visibility`**`(target_object: Any, target_name: str = 'visible', forward: Callable[..., Any] = [...], backward: Callable[..., Any] = [...], value: Any = None) -> Self`

Bind the visibility of this element to the target object's target_name property.

> The binding works both ways, from this element to the target and from the target to this element.
>
> target_object:
>  
>
> The object to bind to.
>
> target_name:
>  
>
> The name of the property to bind to.
>
> forward:
>  
>
> A function to apply to the value before applying it to the target.
>
> backward:
>  
>
> A function to apply to the value before applying it to this element.
>
> value:
>  
>
> If specified, the element will be visible only when the target value is equal to this value.

**`bind_visibility_from`**`(target_object: Any, target_name: str = 'visible', backward: Callable[..., Any] = [...], value: Any = None) -> Self`

Bind the visibility of this element from the target object's target_name property.

> The binding works one way only, from the target to this element.
>
> target_object:
>  
>
> The object to bind from.
>
> target_name:
>  
>
> The name of the property to bind from.
>
> backward:
>  
>
> A function to apply to the value before applying it to this element.
>
> value:
>  
>
> If specified, the element will be visible only when the target value is equal to this value.

**`bind_visibility_to`**`(target_object: Any, target_name: str = 'visible', forward: Callable[..., Any] = [...]) -> Self`

Bind the visibility of this element to the target object's target_name property.

> The binding works one way only, from this element to the target.
>
> target_object:
>  
>
> The object to bind to.
>
> target_name:
>  
>
> The name of the property to bind to.
>
> forward:
>  
>
> A function to apply to the value before applying it to the target.

**`classes`**`(add: Optional[str] = None, remove: Optional[str] = None, replace: Optional[str] = None) -> Self`

Apply, remove, or replace HTML classes.

> This allows modifying the look of the element or its layout using Tailwind or Quasar classes.
>
> Removing or replacing classes can be helpful if predefined classes are not desired.
>
> add:
>  
>
> whitespace-delimited string of classes
>
> remove:
>  
>
> whitespace-delimited string of classes to remove from the element
>
> replace:
>  
>
> whitespace-delimited string of classes to use instead of existing ones

**`clear`**`() -> None`

Remove all child elements.

**`delete`**`() -> None`

Delete the element.

**`disable`**`() -> None`

Disable the element.

**`enable`**`() -> None`

Enable the element.

**`move`**`(target_container: Optional[Element] = None, target_index: int = -1)`

Move the element to another container.

> target_container:
>  
>
> container to move the element to (default: the parent container)
>
> target_index:
>  
>
> index within the target slot (default: append to the end)

**`on`**`(type: str, handler: Optional[Callable[..., Any]] = None, args: Union[None, Sequence[str], Sequence[Optional[Sequence[str]]]] = None, throttle: float = 0.0, leading_events: bool = True,
trailing_events: bool = True) -> Self`

Subscribe to an event.

> type:
>  
>
> name of the event (e.g. "click", "mousedown", or "update:model-value")
>
> handler:
>  
>
> callback that is called upon occurrence of the event
>
> args:
>  
>
> arguments included in the event message sent to the event handler (default: None meaning all)
>
> throttle:
>  
>
> minimum time (in seconds) between event occurrences (default: 0.0)
>
> leading_events:
>  
>
> whether to trigger the event handler immediately upon the first event occurrence (default: True)
>
> trailing_events:
>  
>
> whether to trigger the event handler after the last event occurrence (default: True)

**`props`**`(add: Optional[str] = None, remove: Optional[str] = None) -> Self`

Add or remove props.

> This allows modifying the look of the element or its layout using Quasar props. Since props are simply applied as HTML attributes, they can be used with any HTML element.
>
> Boolean properties are assumed True if no value is specified.
>
> add:
>  
>
> whitespace-delimited list of either boolean values or key=value pair to add
>
> remove:
>  
>
> whitespace-delimited list of property keys to remove

**`remove`**`(element: Union[Element, int]) -> None`

Remove a child element.

> element:
>  
>
> either the element instance or its ID

**`run_method`**`(name: str, *args: Any, timeout: float = 1, check_interval: float = 0.01) -> AwaitableResponse`

Run a method on the client side.

> If the function is awaited, the result of the method call is returned. Otherwise, the method is executed without waiting for a response.
>
> name:
>  
>
> name of the method
>
> args:
>  
>
> arguments to pass to the method
>
> timeout:
>  
>
> maximum time to wait for a response (default: 1 second)
>
> check_interval:
>  
>
> time between checks for a response (default: 0.01 seconds)

**`set_autocomplete`**`(autocomplete: Optional[List[str]]) -> None`

Set the autocomplete list.

**`set_enabled`**`(value: bool) -> None`

Set the enabled state of the element.

**`set_value`**`(value: Any) -> None`

Set the value of this element.

> value:
>  
>
> The value to set.

**`set_visibility`**`(visible: bool) -> None`

Set the visibility of this element.

> visible:
>  
>
> Whether the element should be visible.

**`style`**`(add: Optional[str] = None, remove: Optional[str] = None, replace: Optional[str] = None) -> Self`

Apply, remove, or replace CSS definitions.

> Removing or replacing styles can be helpful if the predefined style is not desired.
>
> add:
>  
>
> semicolon-separated list of styles to add to the element
>
> remove:
>  
>
> semicolon-separated list of styles to remove from the element
>
> replace:
>  
>
> semicolon-separated list of styles to use instead of existing ones

**`tooltip`**`(text: str) -> Self`

Add a tooltip to the element.

> text:
>  
>
> text of the tooltip

**`update`**`() -> None`

Update the element on the client side.

**`validate`**`() -> None`

Validate the current value and set the error message if necessary.

Inherited from

  * `ValidationElement`

  * `ValueElement`

  * `DisableableElement`

  * `Element`

  * `Visibility`

Connection lost. Trying to reconnect...

