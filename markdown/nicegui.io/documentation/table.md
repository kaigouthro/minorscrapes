InstallationFeaturesDemosDocumentationExamplesWhy?

_search_

_dark_mode_ _light_mode_ _brightness_auto_

_more_vert_

← Overview

**Demos**

Table with expandable rowsShow and hide columnsTable with drop down selectionTable from Pandas DataFrameAdding rowsCustom sorting and formattingToggle fullscreenPaginationComputed fieldsConditional
formattingTable cells with links

**Reference**

PropertiesMethodsInherited from

Documentation

ui. _table_

A table based on Quasar's QTable component.

columns:

list of column objects

rows:

list of row objects

row_key:

name of the column containing unique data identifying the row (default: "id")

title:

title of the table

selection:

selection type ("single" or "multiple"; default: None)

pagination:

a dictionary correlating to a pagination object or number of rows per page (None hides the pagination, 0 means "infinite"; default: None).

on_select:

callback which is invoked when the selection changes

If selection is 'single' or 'multiple', then a selected property is accessible containing the selected rows.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    columns = [
        {'name': 'name', 'label': 'Name', 'field': 'name', 'required': True, 'align': 'left'},
        {'name': 'age', 'label': 'Age', 'field': 'age', 'sortable': True},
    ]
    rows = [
        {'name': 'Alice', 'age': 18},
        {'name': 'Bob', 'age': 21},
        {'name': 'Carol'},
    ]
    ui.table(columns=columns, rows=rows, row_key='name')
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

Table with expandable rows

_link_

Scoped slots can be used to insert buttons that toggle the expand state of a table row. See the Quasar documentation for more information.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    columns = [
        {'name': 'name', 'label': 'Name', 'field': 'name'},
        {'name': 'age', 'label': 'Age', 'field': 'age'},
    ]
    rows = [
        {'name': 'Alice', 'age': 18},
        {'name': 'Bob', 'age': 21},
        {'name': 'Carol'},
    ]
    
    table = ui.table(columns=columns, rows=rows, row_key='name').classes('w-72')
    table.add_slot('header', r'''
        <q-tr :props="props">
            <q-th auto-width />
            <q-th v-for="col in props.cols" :key="col.name" :props="props">
                {{ col.label }}
            </q-th>
        </q-tr>
    ''')
    table.add_slot('body', r'''
        <q-tr :props="props">
            <q-td auto-width>
                <q-btn size="sm" color="accent" round dense
                    @click="props.expand = !props.expand"
                    :icon="props.expand ? 'remove' : 'add'" />
            </q-td>
            <q-td v-for="col in props.cols" :key="col.name" :props="props">
                {{ col.value }}
            </q-td>
        </q-tr>
        <q-tr v-show="props.expand" :props="props">
            <q-td colspan="100%">
                <div class="text-left">This is {{ props.row.name }}.</div>
            </q-td>
        </q-tr>
    ''')
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

Show and hide columns

_link_

Here is an example of how to show and hide columns in a table.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    from typing import Dict
    
    columns = [
        {'name': 'name', 'label': 'Name', 'field': 'name', 'required': True, 'align': 'left'},
        {'name': 'age', 'label': 'Age', 'field': 'age', 'sortable': True},
    ]
    rows = [
        {'name': 'Alice', 'age': 18},
        {'name': 'Bob', 'age': 21},
        {'name': 'Carol'},
    ]
    table = ui.table(columns=columns, rows=rows, row_key='name')
    
    def toggle(column: Dict, visible: bool) -> None:
        column['classes'] = '' if visible else 'hidden'
        column['headerClasses'] = '' if visible else 'hidden'
        table.update()
    
    with ui.button(icon='menu'):
        with ui.menu(), ui.column().classes('gap-0 p-2'):
            for column in columns:
                ui.switch(column['label'], value=True, on_change=lambda e, column=column: toggle(column, e.value))
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

Table with drop down selection

_link_

Here is an example of how to use a drop down selection in a table. After emitting a `rename` event from the scoped slot, the `rename` function updates the table rows.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import events, ui
    
    columns = [
        {'name': 'name', 'label': 'Name', 'field': 'name'},
        {'name': 'age', 'label': 'Age', 'field': 'age'},
    ]
    rows = [
        {'id': 0, 'name': 'Alice', 'age': 18},
        {'id': 1, 'name': 'Bob', 'age': 21},
        {'id': 2, 'name': 'Carol'},
    ]
    name_options = ['Alice', 'Bob', 'Carol']
    
    def rename(e: events.GenericEventArguments) -> None:
        for row in rows:
            if row['id'] == e.args['id']:
                row['name'] = e.args['name']
        ui.notify(f'Table.rows is now: {table.rows}')
    
    table = ui.table(columns=columns, rows=rows, row_key='name').classes('w-full')
    table.add_slot('body', r'''
        <q-tr :props="props">
            <q-td key="name" :props="props">
                <q-select
                    v-model="props.row.name"
                    :options="''' + str(name_options) + r'''"
                    @update:model-value="() => $parent.$emit('rename', props.row)"
                />
            </q-td>
            <q-td key="age" :props="props">
                {{ props.row.age }}
            </q-td>
        </q-tr>
    ''')
    table.on('rename', rename)
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

Table from Pandas DataFrame

_link_

You can create a table from a Pandas DataFrame using the `from_pandas` method. This method takes a Pandas DataFrame as input and returns a table.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    import pandas as pd
    from nicegui import ui
    
    df = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
    ui.table.from_pandas(df).classes('max-h-40')
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

Adding rows

_link_

It's simple to add new rows with the `add_rows(dict)` method.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    import os
    import random
    from nicegui import ui
    
    def add():
        item = os.urandom(10 // 2).hex()
        table.add_rows({'id': item, 'count': random.randint(0, 100)})
    
    ui.button('add', on_click=add)
    columns = [
        {'name': 'id', 'label': 'ID', 'field': 'id'},
        {'name': 'count', 'label': 'Count', 'field': 'count'},
    ]
    table = ui.table(columns=columns, rows=[], row_key='id').classes('w-full')
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

Custom sorting and formatting

_link_

You can define dynamic column attributes using a `:` prefix. This way you can define custom sorting and formatting functions.

The following example allows sorting the `name` column by length. The `age` column is formatted to show the age in years.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    columns = [
        {
            'name': 'name',
            'label': 'Name',
            'field': 'name',
            'sortable': True,
            ':sort': '(a, b, rowA, rowB) => b.length - a.length',
        },
        {
            'name': 'age',
            'label': 'Age',
            'field': 'age',
            ':format': 'value => value + " years"',
        },
    ]
    rows = [
        {'name': 'Alice', 'age': 18},
        {'name': 'Bob', 'age': 21},
        {'name': 'Carl', 'age': 42},
    ]
    ui.table(columns=columns, rows=rows, row_key='name')
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

Toggle fullscreen

_link_

You can toggle the fullscreen mode of a table using the `toggle_fullscreen()` method.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    table = ui.table(
        columns=[{'name': 'name', 'label': 'Name', 'field': 'name'}],
        rows=[{'name': 'Alice'}, {'name': 'Bob'}, {'name': 'Carol'}],
    ).classes('w-full')
    
    with table.add_slot('top-left'):
        def toggle() -> None:
            table.toggle_fullscreen()
            button.props('icon=fullscreen_exit' if table.is_fullscreen else 'icon=fullscreen')
        button = ui.button('Toggle fullscreen', icon='fullscreen', on_click=toggle).props('flat')
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

Pagination

_link_

You can provide either a single integer or a dictionary to define pagination.

The dictionary can contain the following keys:

- `rowsPerPage`: The number of rows per page.
- `sortBy`: The column name to sort by.
- `descending`: Whether to sort in descending order.
- `page`: The current page (1-based).

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    columns = [
        {'name': 'name', 'label': 'Name', 'field': 'name', 'required': True, 'align': 'left'},
        {'name': 'age', 'label': 'Age', 'field': 'age', 'sortable': True},
    ]
    rows = [
        {'name': 'Elsa', 'age': 18},
        {'name': 'Oaken', 'age': 46},
        {'name': 'Hans', 'age': 20},
        {'name': 'Sven'},
        {'name': 'Olaf', 'age': 4},
        {'name': 'Anna', 'age': 17},
    ]
    ui.table(columns=columns, rows=rows, pagination=3)
    ui.table(columns=columns, rows=rows, pagination={'rowsPerPage': 4, 'sortBy': 'age', 'page': 2})
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

Computed fields

_link_

You can use functions to compute the value of a column. The function receives the row as an argument. See the Quasar documentation for more information.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    columns = [
        {'name': 'name', 'label': 'Name', 'field': 'name', 'align': 'left'},
        {'name': 'length', 'label': 'Length', ':field': 'row => row.name.length'},
    ]
    rows = [
        {'name': 'Alice'},
        {'name': 'Bob'},
        {'name': 'Christopher'},
    ]
    ui.table(columns=columns, rows=rows, row_key='name')
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

Conditional formatting

_link_

You can use scoped slots to conditionally format the content of a cell. See the Quasar documentation for more information about body-cell slots.

In this demo we use a `q-badge` to display the age in red if the person is under 21 years old. We use the `body-cell-age` slot to insert the `q-badge` into the `age` column. The ":color" attribute of
the `q-badge` is set to "red" if the age is under 21, otherwise it is set to "green". The colon in front of the "color" attribute indicates that the value is a JavaScript expression.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    columns = [
        {'name': 'name', 'label': 'Name', 'field': 'name'},
        {'name': 'age', 'label': 'Age', 'field': 'age'},
    ]
    rows = [
        {'name': 'Alice', 'age': 18},
        {'name': 'Bob', 'age': 21},
        {'name': 'Carol', 'age': 42},
    ]
    table = ui.table(columns=columns, rows=rows, row_key='name')
    table.add_slot('body-cell-age', '''
        <q-td key="age" :props="props">
            <q-badge :color="props.value < 21 ? 'red' : 'green'">
                {{ props.value }}
            </q-badge>
        </q-td>
    ''')
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

Table cells with links

_link_

Here is a demo of how to insert links into table cells. We use the `body-cell-link` slot to insert an `<a>` tag into the `link` column.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    columns = [
        {'name': 'name', 'label': 'Name', 'field': 'name', 'align': 'left'},
        {'name': 'link', 'label': 'Link', 'field': 'link', 'align': 'left'},
    ]
    rows = [
        {'name': 'Google', 'link': 'https://google.com'},
        {'name': 'Facebook', 'link': 'https://facebook.com'},
        {'name': 'Twitter', 'link': 'https://twitter.com'},
    ]
    table = ui.table(columns=columns, rows=rows, row_key='name')
    table.add_slot('body-cell-link', '''
        <q-td :props="props">
            <a :href="props.value">{{ props.value }}</a>
        </q-td>
    ''')
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

## Reference

Properties

_link_

**`columns`**`: 'List[Dict]' (settable)`

List of columns.

**`filter`**`: BindableProperty`

**`is_deleted`**`: 'bool'`

Whether the element has been deleted.

**`is_fullscreen`**`: 'bool' (settable)`

Whether the table is in fullscreen mode.

**`is_ignoring_events`**`: 'bool'`

Return whether the element is currently ignoring events.

**`row_key`**`: 'str' (settable)`

Name of the column containing unique data identifying the row.

**`rows`**`: 'List[Dict]' (settable)`

List of rows.

**`selected`**`: 'List[Dict]' (settable)`

List of selected rows.

**`visible`**`: BindableProperty`

Methods

_link_

**`add_rows`**`(*rows: Dict) -> None`

Add rows to the table.

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

**`bind_filter`**`(target_object: Any, target_name: str = 'filter', forward: Callable[..., Any] = [...], backward: Callable[..., Any] = [...]) -> Self`

Bind the filter of this element to the target object's target_name property.

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

**`bind_filter_from`**`(target_object: Any, target_name: str = 'filter', backward: Callable[..., Any] = [...]) -> Self`

Bind the filter of this element from the target object's target_name property.

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

**`bind_filter_to`**`(target_object: Any, target_name: str = 'filter', forward: Callable[..., Any] = [...]) -> Self`

Bind the filter of this element to the target object's target_name property.

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

**`remove_rows`**`(*rows: Dict) -> None`

Remove rows from the table.

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

**`set_filter`**`(filter_: str) -> None`

Set the filter of this element.

> filter:
>
> The new filter.

**`set_fullscreen`**`(value: bool) -> None`

Set fullscreen mode.

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

**`toggle_fullscreen`**`() -> None`

Toggle fullscreen mode.

**`tooltip`**`(text: str) -> Self`

Add a tooltip to the element.

> text:
>
> text of the tooltip

**`update`**`() -> None`

Update the element on the client side.

Inherited from

_link_

- `FilterElement`

- `Element`

- `Visibility`

Connection lost. Trying to reconnect...
