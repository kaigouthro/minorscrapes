← Overview

**Demos**

Search-as-you-typeMulti selectionUpdate options

**Reference**

PropertiesMethodsInherited from

Documentation

ui. _select_

This element is based on Quasar's QSelect component.

The options can be specified as a list of values, or as a dictionary mapping values to labels. After manipulating the options, call update() to update the options in the UI.

If with_input is True, an input field is shown to filter the options.

If new_value_mode is not None, it implies with_input=True and the user can enter new values in the input field. See Quasar's documentation for details. Note that this mode is ineffective when setting
the value property programmatically.

options:

a list \['value1', ...\] or dictionary {'value1':'label1', ...} specifying the options

label:

the label to display above the selection

value:

the initial value

on_change:

callback to execute when selection changes

with_input:

whether to show an input field to filter the options

new_value_mode:

handle new values from user input (default: None, i.e. no new values)

multiple:

whether to allow multiple selections

clearable:

whether to add a button to clear the selection

_circle_ _circle_ _circle_

main.py

\[code\]

```python




    from nicegui import ui
    
    select1 = ui.select([1, 2, 3], value=1)
    select2 = ui.select({1: 'One', 2: 'Two', 3: 'Three'}).bind_value(select1, 'value')
    
    ui.run()
    


```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

Search-as-you-type

_link_

You can activate `with_input` to get a text input with autocompletion. The options will be filtered as you type.

_circle_ _circle_ _circle_

main.py

\[code\]

```python




    from nicegui import ui
    
    continents = [
        'Asia',
        'Africa',
        'Antarctica',
        'Europe',
        'Oceania',
        'North America',
        'South America',
    ]
    ui.select(options=continents, with_input=True,
              on_change=lambda e: ui.notify(e.value)).classes('w-40')
    
    ui.run()
    


```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

Multi selection

_link_

You can activate `multiple` to allow the selection of more than one item.

_circle_ _circle_ _circle_

main.py

\[code\]

```python




    from nicegui import ui
    
    names = ['Alice', 'Bob', 'Carol']
    ui.select(names, multiple=True, value=names[:2], label='comma-separated') \
        .classes('w-64')
    ui.select(names, multiple=True, value=names[:2], label='with chips') \
        .classes('w-64').props('use-chips')
    
    ui.run()
    


```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

Update options

_link_

Options can be changed with the `options` property. But then you also need to call `update()` afterwards to let the change take effect. `set_options` is a shortcut that does both and works well for
lambdas.

_circle_ _circle_ _circle_

main.py

\[code\]

```python




    from nicegui import ui
    
    select = ui.select([1, 2, 3], value=1)
    with ui.row():
        ui.button('4, 5, 6', on_click=lambda: select.set_options([4, 5, 6], value=4))
        ui.button('1, 2, 3', on_click=lambda: select.set_options([1, 2, 3], value=1))
    
    ui.run()
    


```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

## Reference

Properties

_link_

**`enabled`**`: BindableProperty`

**`is_deleted`**`: 'bool'`

Whether the element has been deleted.

**`is_ignoring_events`**`: bool`

Return whether the element is currently ignoring events.

**`value`**`: BindableProperty`

**`visible`**`: BindableProperty`

Methods

_link_

**`add_slot`**`(name: str, template: Optional[str] = None) -> Slot`

Add a slot to the element.

> name:
>
> name of the slot
>
> template:
>
> Vue template of the slot
>
> return:
>
> the slot

**`bind_enabled`**`(target_object: Any, target_name: str = 'enabled', forward: Callable[..., Any] = [...], backward: Callable[..., Any] = [...]) -> Self`

Bind the enabled state of this element to the target object's target_name property.

> The binding works both ways, from this element to the target and from the target to this element.
>
> target_object:
>
> The object to bind to.
>
> target_name:
>
> The name of the property to bind to.
>
> forward:
>
> A function to apply to the value before applying it to the target.
>
> backward:
>
> A function to apply to the value before applying it to this element.

**`bind_enabled_from`**`(target_object: Any, target_name: str = 'enabled', backward: Callable[..., Any] = [...]) -> Self`

Bind the enabled state of this element from the target object's target_name property.

> The binding works one way only, from the target to this element.
>
> target_object:
>
> The object to bind from.
>
> target_name:
>
> The name of the property to bind from.
>
> backward:
>
> A function to apply to the value before applying it to this element.

**`bind_enabled_to`**`(target_object: Any, target_name: str = 'enabled', forward: Callable[..., Any] = [...]) -> Self`

Bind the enabled state of this element to the target object's target_name property.

> The binding works one way only, from this element to the target.
>
> target_object:
>
> The object to bind to.
>
> target_name:
>
> The name of the property to bind to.
>
> forward:
>
> A function to apply to the value before applying it to the target.

**`bind_value`**`(target_object: Any, target_name: str = 'value', forward: Callable[..., Any] = [...], backward: Callable[..., Any] = [...]) -> Self`

Bind the value of this element to the target object's target_name property.

> The binding works both ways, from this element to the target and from the target to this element.
>
> target_object:
>
> The object to bind to.
>
> target_name:
>
> The name of the property to bind to.
>
> forward:
>
> A function to apply to the value before applying it to the target.
>
> backward:
>
> A function to apply to the value before applying it to this element.

**`bind_value_from`**`(target_object: Any, target_name: str = 'value', backward: Callable[..., Any] = [...]) -> Self`

Bind the value of this element from the target object's target_name property.

> The binding works one way only, from the target to this element.
>
> target_object:
>
> The object to bind from.
>
> target_name:
>
> The name of the property to bind from.
>
> backward:
>
> A function to apply to the value before applying it to this element.

**`bind_value_to`**`(target_object: Any, target_name: str = 'value', forward: Callable[..., Any] = [...]) -> Self`

Bind the value of this element to the target object's target_name property.

> The binding works one way only, from this element to the target.
>
> target_object:
>
> The object to bind to.
>
> target_name:
>
> The name of the property to bind to.
>
> forward:
>
> A function to apply to the value before applying it to the target.

**`bind_visibility`**`(target_object: Any, target_name: str = 'visible', forward: Callable[..., Any] = [...], backward: Callable[..., Any] = [...], value: Any = None) -> Self`

Bind the visibility of this element to the target object's target_name property.

> The binding works both ways, from this element to the target and from the target to this element.
>
> target_object:
>
> The object to bind to.
>
> target_name:
>
> The name of the property to bind to.
>
> forward:
>
> A function to apply to the value before applying it to the target.
>
> backward:
>
> A function to apply to the value before applying it to this element.
>
> value:
>
> If specified, the element will be visible only when the target value is equal to this value.

**`bind_visibility_from`**`(target_object: Any, target_name: str = 'visible', backward: Callable[..., Any] = [...], value: Any = None) -> Self`

Bind the visibility of this element from the target object's target_name property.

> The binding works one way only, from the target to this element.
>
> target_object:
>
> The object to bind from.
>
> target_name:
>
> The name of the property to bind from.
>
> backward:
>
> A function to apply to the value before applying it to this element.
>
> value:
>
> If specified, the element will be visible only when the target value is equal to this value.

**`bind_visibility_to`**`(target_object: Any, target_name: str = 'visible', forward: Callable[..., Any] = [...]) -> Self`

Bind the visibility of this element to the target object's target_name property.

> The binding works one way only, from this element to the target.
>
> target_object:
>
> The object to bind to.
>
> target_name:
>
> The name of the property to bind to.
>
> forward:
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
> whitespace-delimited string of classes
>
> remove:
>
> whitespace-delimited string of classes to remove from the element
>
> replace:
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
> container to move the element to (default: the parent container)
>
> target_index:
>
> index within the target slot (default: append to the end)

**`on`**`(type: str, handler: Optional[Callable[..., Any]] = None, args: Union[None, Sequence[str], Sequence[Optional[Sequence[str]]]] = None, throttle: float = 0.0, leading_events: bool = True, trailing_events: bool = True) -> Self`

Subscribe to an event.

> type:
>
> name of the event (e.g. "click", "mousedown", or "update:model-value")
>
> handler:
>
> callback that is called upon occurrence of the event
>
> args:
>
> arguments included in the event message sent to the event handler (default: None meaning all)
>
> throttle:
>
> minimum time (in seconds) between event occurrences (default: 0.0)
>
> leading_events:
>
> whether to trigger the event handler immediately upon the first event occurrence (default: True)
>
> trailing_events:
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
> whitespace-delimited list of either boolean values or key=value pair to add
>
> remove:
>
> whitespace-delimited list of property keys to remove

**`remove`**`(element: Union[Element, int]) -> None`

Remove a child element.

> element:
>
> either the element instance or its ID

**`run_method`**`(name: str, *args: Any, timeout: float = 1, check_interval: float = 0.01) -> AwaitableResponse`

Run a method on the client side.

> If the function is awaited, the result of the method call is returned. Otherwise, the method is executed without waiting for a response.
>
> name:
>
> name of the method
>
> args:
>
> arguments to pass to the method
>
> timeout:
>
> maximum time to wait for a response (default: 1 second)
>
> check_interval:
>
> time between checks for a response (default: 0.01 seconds)

**`set_enabled`**`(value: bool) -> None`

Set the enabled state of the element.

**`set_options`**`(options: Union[List, Dict], value: Any = None) -> None`

Set the options of this choice element.

> options:
>
> The new options.
>
> value:
>
> The new value. If not given, the current value is kept.

**`set_value`**`(value: Any) -> None`

Set the value of this element.

> value:
>
> The value to set.

**`set_visibility`**`(visible: bool) -> None`

Set the visibility of this element.

> visible:
>
> Whether the element should be visible.

**`style`**`(add: Optional[str] = None, remove: Optional[str] = None, replace: Optional[str] = None) -> Self`

Apply, remove, or replace CSS definitions.

> Removing or replacing styles can be helpful if the predefined style is not desired.
>
> add:
>
> semicolon-separated list of styles to add to the element
>
> remove:
>
> semicolon-separated list of styles to remove from the element
>
> replace:
>
> semicolon-separated list of styles to use instead of existing ones

**`tooltip`**`(text: str) -> Self`

Add a tooltip to the element.

> text:
>
> text of the tooltip

**`update`**`() -> None`

Inherited from

_link_

- `ChoiceElement`

- `ValueElement`

- `DisableableElement`

- `Element`

- `Visibility`

Connection lost. Trying to reconnect...
