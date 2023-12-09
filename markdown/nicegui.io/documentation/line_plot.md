InstallationFeaturesDemosDocumentationExamplesWhy?

_search_

_dark_mode_ _light_mode_ _brightness_auto_

_more_vert_

← Overview

**Demo**

**Reference**

PropertiesMethodsInherited from

Documentation

ui. _line_plot_

Create a line plot using pyplot. The push method provides live updating when utilized in combination with ui.timer.

n:

number of lines

limit:

maximum number of datapoints per line (new points will displace the oldest)

update_every:

update plot only after pushing new data multiple times to save CPU and bandwidth

close:

whether the figure should be closed after exiting the context; set to False if you want to update it later (default: True)

kwargs:

arguments like figsize which should be passed to pyplot.figure

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    import math
    from datetime import datetime
    from nicegui import ui
    
    line_plot = ui.line_plot(n=2, limit=20, figsize=(3, 2), update_every=5) \
        .with_legend(['sin', 'cos'], loc='upper center', ncol=2)
    
    def update_line_plot() -> None:
        now = datetime.now()
        x = now.timestamp()
        y1 = math.sin(x)
        y2 = math.cos(x)
        line_plot.push([now], [[y1], [y2]])
    
    line_updates = ui.timer(0.1, update_line_plot, active=False)
    line_checkbox = ui.checkbox('active').bind_value(line_updates, 'active')
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

## Reference

Properties

_link_

**`is_deleted`**`: 'bool'`

Whether the element has been deleted.

**`is_ignoring_events`**`: 'bool'`

Return whether the element is currently ignoring events.

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

Clear the line plot.

**`delete`**`() -> None`

Delete the element.

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

**`push`**`(x: List[float], Y: List[List[float]]) -> None`

Push new data to the plot.

> x:
>
> list of x values
>
> Y:
>
> list of lists of y values (one list per line)

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

Update the element on the client side.

**`with_legend`**`(titles: List[str], kwargs: Any)`

Add a legend to the plot.

> titles:
>
> list of titles for the lines
>
> kwargs:
>
> additional arguments which should be passed to pyplot.legend

Inherited from

_link_

- `Pyplot`

- `Element`

- `Visibility`

Connection lost. Trying to reconnect...
