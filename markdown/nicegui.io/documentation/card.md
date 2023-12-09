InstallationFeaturesDemosDocumentationExamplesWhy?

_search_

_dark_mode_ _light_mode_ _brightness_auto_

_more_vert_

← Overview

**Demos**

Card without shadowThe issue with nested borders

**Reference**

PropertiesMethodsInherited from

Documentation

ui. _card_

This element is based on Quasar's QCard component. It provides a container with a dropped shadow.

Note: There are subtle differences between the Quasar component and this element. In contrast to this element, the original QCard has no padding by default and hides outer borders of nested elements.
If you want the original behavior, use the tight method. If you want the padding and borders for nested children, move the children into another container.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    with ui.card().tight():
        ui.image('https://picsum.photos/id/684/640/360')
        with ui.card_section():
            ui.label('Lorem ipsum dolor sit amet, consectetur adipiscing elit, ...')
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

Card without shadow

_link_

You can remove the shadow from a card by adding the `no-shadow` class. The following demo shows a 1 pixel wide border instead.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    with ui.card().classes('no-shadow border-[1px]'):
        ui.label('See, no shadow!')
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

The issue with nested borders

_link_

The following example shows a table nested in a card. Cards have a default padding in NiceGUI, so the table is not flush with the card's border. The table has the `flat` and `bordered` props set, so
it should have a border. However, due to the way QCard is designed, the border is not visible (first card). There are two ways to fix this:

- To get the original QCard behavior, use the `tight` method (second card). It removes the padding and the table border collapses with the card border.

- To preserve the padding _and_ the table border, move the table into another container like a `ui.row` (third card).

See https://github.com/zauberzeug/nicegui/issues/726 for more information.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    columns = [{'name': 'age', 'label': 'Age', 'field': 'age'}]
    rows = [{'age': '16'}, {'age': '18'}, {'age': '21'}]
    
    with ui.row():
        with ui.card():
            ui.table(columns, rows).props('flat bordered')
    
        with ui.card().tight():
            ui.table(columns, rows).props('flat bordered')
    
        with ui.card():
            with ui.row():
                ui.table(columns, rows).props('flat bordered')
    
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

Remove all child elements.

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

**`tight`**`() -> Self`

Remove padding and gaps between nested elements.

**`tooltip`**`(text: str) -> Self`

Add a tooltip to the element.

> text:
>
> text of the tooltip

**`update`**`() -> None`

Update the element on the client side.

Inherited from

_link_

- `Element`

- `Visibility`

Connection lost. Trying to reconnect...
