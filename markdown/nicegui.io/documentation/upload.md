← Overview

**Demos**

Upload restrictionsShow file content

**Reference**

PropertiesMethodsInherited from

Documentation

ui. _upload_

Based on Quasar's QUploader component.

multiple:

allow uploading multiple files at once (default: False)

max_file_size:

maximum file size in bytes (default: 0)

max_total_size:

maximum total size of all files in bytes (default: 0)

max_files:

maximum number of files (default: 0)

on_upload:

callback to execute for each uploaded file (type: nicegui.events.UploadEventArguments)

on_rejected:

callback to execute for each rejected file

label:

label for the uploader (default: '')

auto_upload:

automatically upload files when they are selected (default: False)

_circle_ _circle_ _circle_

main.py

\[code\]

```python




    from nicegui import ui
    
    ui.upload(on_upload=lambda e: ui.notify(f'Uploaded {e.name}')).classes('max-w-full')
    
    ui.run()
    


```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

Upload restrictions

_link_

In this demo, the upload is restricted to a maximum file size of 1 MB. When a file is rejected, a notification is shown.

_circle_ _circle_ _circle_

main.py

\[code\]

```python




    from nicegui import ui
    
    ui.upload(on_upload=lambda e: ui.notify(f'Uploaded {e.name}'),
              on_rejected=lambda: ui.notify('Rejected!'),
              max_file_size=1_000_000).classes('max-w-full')
    
    ui.run()
    


```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

Show file content

_link_

In this demo, the uploaded markdown file is shown in a dialog.

_circle_ _circle_ _circle_

main.py

\[code\]

```python




    from nicegui import events, ui
    
    with ui.dialog().props('full-width') as dialog:
        with ui.card():
            content = ui.markdown()
    
    def handle_upload(e: events.UploadEventArguments):
        text = e.content.read().decode('utf-8')
        content.set_content(text)
        dialog.open()
    
    ui.upload(on_upload=handle_upload).props('accept=.md').classes('max-w-full')
    
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

**`reset`**`() -> None`

Clear the upload queue.

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

Inherited from

_link_

- `DisableableElement`

- `Element`

- `Visibility`

Connection lost. Trying to reconnect...
