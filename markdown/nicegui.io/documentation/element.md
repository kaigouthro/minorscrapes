

← Overview

**Demos**

Move elementsDefault propsDefault classesDefault style

 **Reference**

PropertiesMethodsInherited from

Documentation

ui. _element_

This class is the base class for all other UI elements. But you can use it to create elements with arbitrary HTML tags.

tag:

    

HTML tag of the element

_client:

    

client for this element (for internal use only)

main.py

[code]
```python




    from nicegui import ui
    
    with ui.element('div').classes('p-2 bg-blue-100'):
        ui.label('inside a colored div')
    
    ui.run()
    


```
[/code]


NiceGUI

Move elements

This demo shows how to move elements between or within containers.

main.py

[code]
```python




    from nicegui import ui
    
    with ui.card() as a:
        ui.label('A')
        x = ui.label('X')
    
    with ui.card() as b:
        ui.label('B')
    
    ui.button('Move X to A', on_click=lambda: x.move(a))
    ui.button('Move X to B', on_click=lambda: x.move(b))
    ui.button('Move X to top', on_click=lambda: x.move(target_index=0))
    
    ui.run()
    


```
[/code]


NiceGUI

Default props

You can set default props for all elements of a certain class. This way you can avoid repeating the same props over and over again.

Default props only apply to elements created after the default props were set. Subclasses inherit the default props of their parent class.

main.py

[code]
```python




    from nicegui import ui
    
    ui.button.default_props('rounded outline')
    ui.button('Button A')
    ui.button('Button B')
    
    ui.run()
    


```
[/code]


NiceGUI

Default classes

You can set default classes for all elements of a certain class. This way you can avoid repeating the same classes over and over again.

Default classes only apply to elements created after the default classes were set. Subclasses inherit the default classes of their parent class.

main.py

[code]
```python




    from nicegui import ui
    
    ui.label.default_classes('bg-blue-100 p-2')
    ui.label('Label A')
    ui.label('Label B')
    
    ui.run()
    


```
[/code]


NiceGUI

Default style

You can set a default style for all elements of a certain class. This way you can avoid repeating the same style over and over again.

A default style only applies to elements created after the default style was set. Subclasses inherit the default style of their parent class.

main.py

[code]
```python




    from nicegui import ui
    
    ui.label.default_style('color: tomato')
    ui.label('Label A')
    ui.label('Label B')
    
    ui.run()
    


```
[/code]


NiceGUI

## Reference

Properties

 **`is_deleted`**`: 'bool'`

Whether the element has been deleted.

**`is_ignoring_events`**`: 'bool'`

Return whether the element is currently ignoring events.

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

Inherited from

  * `Visibility`

Connection lost. Trying to reconnect...

