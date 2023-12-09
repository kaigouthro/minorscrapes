InstallationFeaturesDemosDocumentationExamplesWhy?

_search_

_dark_mode_ _light_mode_ _brightness_auto_

_more_vert_

← Overview

**Demos**

Select AG Grid RowsFilter Rows using Mini FiltersAG Grid with Conditional Cell FormattingCreate Grid from Pandas DataFrameRender columns as HTMLRespond to an AG Grid eventAG Grid with complex
objectsAG Grid with dynamic row height

**Reference**

PropertiesMethodsInherited from

Documentation

ui. _aggrid_

An element to create a grid using AG Grid.

The methods call_api_method and call_column_api_method can be used to interact with the AG Grid instance on the client.

options:

dictionary of AG Grid options

html_columns:

list of columns that should be rendered as HTML (default: \[\])

theme:

AG Grid theme (default: 'balham')

auto_size_columns:

whether to automatically resize columns to fit the grid width (default: True)

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    grid = ui.aggrid({
        'defaultColDef': {'flex': 1},
        'columnDefs': [
            {'headerName': 'Name', 'field': 'name'},
            {'headerName': 'Age', 'field': 'age'},
            {'headerName': 'Parent', 'field': 'parent', 'hide': True},
        ],
        'rowData': [
            {'name': 'Alice', 'age': 18, 'parent': 'David'},
            {'name': 'Bob', 'age': 21, 'parent': 'Eve'},
            {'name': 'Carol', 'age': 42, 'parent': 'Frank'},
        ],
        'rowSelection': 'multiple',
    }).classes('max-h-40')
    
    def update():
        grid.options['rowData'][0]['age'] += 1
        grid.update()
    
    ui.button('Update', on_click=update)
    ui.button('Select all', on_click=lambda: grid.call_api_method('selectAll'))
    ui.button('Show parent', on_click=lambda: grid.call_column_api_method('setColumnVisible', 'parent', True))
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

Select AG Grid Rows

_link_

You can add checkboxes to grid cells to allow the user to select single or multiple rows.

To retrieve the currently selected rows, use the `get_selected_rows` method. This method returns a list of rows as dictionaries.

If `rowSelection` is set to `'single'` or to get the first selected row, you can also use the `get_selected_row` method. This method returns a single row as a dictionary or `None` if no row is
selected.

See the AG Grid documentation for more information.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    grid = ui.aggrid({
        'columnDefs': [
            {'headerName': 'Name', 'field': 'name', 'checkboxSelection': True},
            {'headerName': 'Age', 'field': 'age'},
        ],
        'rowData': [
            {'name': 'Alice', 'age': 18},
            {'name': 'Bob', 'age': 21},
            {'name': 'Carol', 'age': 42},
        ],
        'rowSelection': 'multiple',
    }).classes('max-h-40')
    
    async def output_selected_rows():
        rows = await grid.get_selected_rows()
        if rows:
            for row in rows:
                ui.notify(f"{row['name']}, {row['age']}")
        else:
            ui.notify('No rows selected.')
    
    async def output_selected_row():
        row = await grid.get_selected_row()
        if row:
            ui.notify(f"{row['name']}, {row['age']}")
        else:
            ui.notify('No row selected!')
    
    ui.button('Output selected rows', on_click=output_selected_rows)
    ui.button('Output selected row', on_click=output_selected_row)
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

Filter Rows using Mini Filters

_link_

You can add mini filters to the header of each column to filter the rows.

Note how the "agTextColumnFilter" matches individual characters, like "a" in "Alice" and "Carol", while the "agNumberColumnFilter" matches the entire number, like "18" and "21", but not "1".

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    ui.aggrid({
        'columnDefs': [
            {'headerName': 'Name', 'field': 'name', 'filter': 'agTextColumnFilter', 'floatingFilter': True},
            {'headerName': 'Age', 'field': 'age', 'filter': 'agNumberColumnFilter', 'floatingFilter': True},
        ],
        'rowData': [
            {'name': 'Alice', 'age': 18},
            {'name': 'Bob', 'age': 21},
            {'name': 'Carol', 'age': 42},
        ],
    }).classes('max-h-40')
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

AG Grid with Conditional Cell Formatting

_link_

This demo shows how to use cellClassRules to conditionally format cells based on their values.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    ui.aggrid({
        'columnDefs': [
            {'headerName': 'Name', 'field': 'name'},
            {'headerName': 'Age', 'field': 'age', 'cellClassRules': {
                'bg-red-300': 'x < 21',
                'bg-green-300': 'x >= 21',
            }},
        ],
        'rowData': [
            {'name': 'Alice', 'age': 18},
            {'name': 'Bob', 'age': 21},
            {'name': 'Carol', 'age': 42},
        ],
    })
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

Create Grid from Pandas DataFrame

_link_

You can create an AG Grid from a Pandas DataFrame using the `from_pandas` method. This method takes a Pandas DataFrame as input and returns an AG Grid.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    import pandas as pd
    from nicegui import ui
    
    df = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
    ui.aggrid.from_pandas(df).classes('max-h-40')
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

Render columns as HTML

_link_

You can render columns as HTML by passing a list of column indices to the `html_columns` argument.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    ui.aggrid({
        'columnDefs': [
            {'headerName': 'Name', 'field': 'name'},
            {'headerName': 'URL', 'field': 'url'},
        ],
        'rowData': [
            {'name': 'Google', 'url': '<a href="https://google.com">https://google.com</a>'},
            {'name': 'Facebook', 'url': '<a href="https://facebook.com">https://facebook.com</a>'},
        ],
    }, html_columns=[1])
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

Respond to an AG Grid event

_link_

All AG Grid events are passed through to NiceGUI via the AG Grid global listener. These events can be subscribed to using the `.on()` method.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    ui.aggrid({
        'columnDefs': [
            {'headerName': 'Name', 'field': 'name'},
            {'headerName': 'Age', 'field': 'age'},
        ],
        'rowData': [
            {'name': 'Alice', 'age': 18},
            {'name': 'Bob', 'age': 21},
            {'name': 'Carol', 'age': 42},
        ],
    }).on('cellClicked', lambda event: ui.notify(f'Cell value: {event.args["value"]}'))
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

AG Grid with complex objects

_link_

You can use nested complex objects in AG Grid by separating the field names with a period. (This is the reason why keys in `rowData` are not allowed to contain periods.)

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    ui.aggrid({
        'columnDefs': [
            {'headerName': 'First name', 'field': 'name.first'},
            {'headerName': 'Last name', 'field': 'name.last'},
            {'headerName': 'Age', 'field': 'age'}
        ],
        'rowData': [
            {'name': {'first': 'Alice', 'last': 'Adams'}, 'age': 18},
            {'name': {'first': 'Bob', 'last': 'Brown'}, 'age': 21},
            {'name': {'first': 'Carol', 'last': 'Clark'}, 'age': 42},
        ],
    }).classes('max-h-40')
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

AG Grid with dynamic row height

_link_

You can set the height of individual rows by passing a function to the `getRowHeight` argument.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    ui.aggrid({
        'columnDefs': [{'field': 'name'}, {'field': 'age'}],
        'rowData': [
            {'name': 'Alice', 'age': '18'},
            {'name': 'Bob', 'age': '21'},
            {'name': 'Carol', 'age': '42'},
        ],
        ':getRowHeight': 'params => params.data.age > 35 ? 50 : 25',
    }).classes('max-h-40')
    
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

**`options`**`: 'Dict'`

The options dictionary.

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

**`call_api_method`**`(name: str, *args, timeout: float = 1, check_interval: float = 0.01) -> AwaitableResponse`

Call an AG Grid API method.

> See AG Grid API for a list of methods.
>
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
> timeout in seconds (default: 1 second)
>
> check_interval:
>
> interval in seconds to check for a response (default: 0.01 seconds)
>
> return:
>
> AwaitableResponse that can be awaited to get the result of the method call

**`call_column_api_method`**`(name: str, *args, timeout: float = 1, check_interval: float = 0.01) -> AwaitableResponse`

Call an AG Grid Column API method.

> See AG Grid Column API for a list of methods.
>
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
> timeout in seconds (default: 1 second)
>
> check_interval:
>
> interval in seconds to check for a response (default: 0.01 seconds)
>
> return:
>
> AwaitableResponse that can be awaited to get the result of the method call

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

**`get_client_data`**`(timeout: float = 1, check_interval: float = 0.01) -> List[Dict]`

Get the data from the client including any edits made by the client.

> This method is especially useful when the grid is configured with 'editable': True.
>
> See AG Grid API for more information.
>
> Note that when editing a cell, the row data is not updated until the cell exits the edit mode. This does not happen when the cell loses focus, unless stopEditingWhenCellsLoseFocus: True is set.
>
> timeout:
>
> timeout in seconds (default: 1 second)
>
> check_interval:
>
> interval in seconds to check for a response (default: 0.01 seconds)
>
> return:
>
> list of row data

**`get_selected_row`**`() -> Optional[Dict]`

Get the single currently selected row.

> This method is especially useful when the grid is configured with rowSelection: 'single'.
>
> return:
>
> row data of the first selection if any row is selected, otherwise None

**`get_selected_rows`**`() -> List[Dict]`

Get the currently selected rows.

> This method is especially useful when the grid is configured with rowSelection: 'multiple'.
>
> See AG Grid API for more information.
>
> return:
>
> list of selected row data

**`load_client_data`**`() -> None`

Obtain client data and update the element's row data with it.

> This syncs edits made by the client in editable cells to the server.
>
> Note that when editing a cell, the row data is not updated until the cell exits the edit mode. This does not happen when the cell loses focus, unless stopEditingWhenCellsLoseFocus: True is set.

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

**`tooltip`**`(text: str) -> Self`

Add a tooltip to the element.

> text:
>
> text of the tooltip

**`update`**`() -> None`

Inherited from

_link_

- `Element`

- `Visibility`

Connection lost. Trying to reconnect...
