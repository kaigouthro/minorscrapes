_menu_

InstallationFeaturesDemosDocumentationExamplesWhy?

_search_

_dark_mode_ _light_mode_ _brightness_auto_

_more_vert_

← Overview

Data Elements

TableAG GridHighcharts chartApache EChartPyplot ContextLine PlotPlotly ElementLinear ProgressCircular ProgressSpinner3D SceneTreeLog ViewEditorCodeJSONEditor

_Data Elements_

Table _link_

A table based on Quasar's QTable component.

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

See more...

AG Grid _link_

An element to create a grid using AG Grid.

The methods call_api_method and call_column_api_method can be used to interact with the AG Grid instance on the client.

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

See more...

Highcharts chart _link_

An element to create a chart using Highcharts. Updates can be pushed to the chart by changing the options property. After data has changed, call the update method to refresh the chart.

Due to Highcharts' restrictive license, this element is not part of the standard NiceGUI package. It is maintained in a separate repository and can be installed with pip install nicegui\[highcharts\].

By default, a Highcharts.chart is created. To use, e.g., Highcharts.stockChart instead, set the type property to "stockChart".

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    from random import random
    
    chart = ui.highchart({
        'title': False,
        'chart': {'type': 'bar'},
        'xAxis': {'categories': ['A', 'B']},
        'series': [
            {'name': 'Alpha', 'data': [0.1, 0.2]},
            {'name': 'Beta', 'data': [0.3, 0.4]},
        ],
    }).classes('w-full h-64')
    
    def update():
        chart.options['series'][0]['data'][0] = random()
        chart.update()
    
    ui.button('Update', on_click=update)
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

See more...

Apache EChart _link_

An element to create a chart using ECharts. Updates can be pushed to the chart by changing the options property. After data has changed, call the update method to refresh the chart.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    from random import random
    
    echart = ui.echart({
        'xAxis': {'type': 'value'},
        'yAxis': {'type': 'category', 'data': ['A', 'B'], 'inverse': True},
        'legend': {'textStyle': {'color': 'gray'}},
        'series': [
            {'type': 'bar', 'name': 'Alpha', 'data': [0.1, 0.2]},
            {'type': 'bar', 'name': 'Beta', 'data': [0.3, 0.4]},
        ],
    })
    
    def update():
        echart.options['series'][0]['data'][0] = random()
        echart.update()
    
    ui.button('Update', on_click=update)
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

See more...

Pyplot Context _link_

Create a context to configure a Matplotlib plot.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    import numpy as np
    from matplotlib import pyplot as plt
    from nicegui import ui
    
    with ui.pyplot(figsize=(3, 2)):
        x = np.linspace(0.0, 5.0)
        y = np.cos(2 * np.pi * x) * np.exp(-x)
        plt.plot(x, y, '-')
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

See more...

Line Plot _link_

Create a line plot using pyplot. The push method provides live updating when utilized in combination with ui.timer.

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

See more...

Plotly Element _link_

Renders a Plotly chart. There are two ways to pass a Plotly figure for rendering, see parameter figure:

- Pass a go.Figure object, see https://plotly.com/python/

- Pass a Python dict object with keys data, layout, config (optional), see https://plotly.com/javascript/

For best performance, use the declarative dict approach for creating a Plotly chart.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    import plotly.graph_objects as go
    from nicegui import ui
    
    fig = go.Figure(go.Scatter(x=[1, 2, 3, 4], y=[1, 2, 3, 2.5]))
    fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))
    ui.plotly(fig).classes('w-full h-40')
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

See more...

Linear Progress _link_

A linear progress bar wrapping Quasar's QLinearProgress component.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    slider = ui.slider(min=0, max=1, step=0.01, value=0.5)
    ui.linear_progress().bind_value_from(slider, 'value')
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

See more...

Circular Progress _link_

A circular progress bar wrapping Quasar's QCircularProgress.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    slider = ui.slider(min=0, max=1, step=0.01, value=0.5)
    ui.circular_progress().bind_value_from(slider, 'value')
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

See more...

Spinner _link_

This element is based on Quasar's QSpinner component.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    with ui.row():
        ui.spinner(size='lg')
        ui.spinner('audio', size='lg', color='green')
        ui.spinner('dots', size='lg', color='red')
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

See more...

3D Scene _link_

Display a 3D scene using three.js. Currently NiceGUI supports boxes, spheres, cylinders/cones, extrusions, straight lines, curves and textured meshes. Objects can be translated, rotated and displayed
with different color, opacity or as wireframes. They can also be grouped to apply joint movements.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    with ui.scene().classes('w-full h-64') as scene:
        scene.sphere().material('#4488ff')
        scene.cylinder(1, 0.5, 2, 20).material('#ff8800', opacity=0.5).move(-2, 1)
        scene.extrusion([[0, 0], [0, 1], [1, 0.5]], 0.1).material('#ff8888').move(-2, -2)
    
        with scene.group().move(z=2):
            scene.box().move(x=2)
            scene.box().move(y=2).rotate(0.25, 0.5, 0.75)
            scene.box(wireframe=True).material('#888888').move(x=2, y=2)
    
        scene.line([-4, 0, 0], [-4, 2, 0]).material('#ff0000')
        scene.curve([-4, 0, 0], [-4, -1, 0], [-3, -1, 0], [-3, -2, 0]).material('#008800')
    
        logo = 'https://avatars.githubusercontent.com/u/2843826'
        scene.texture(logo, [[[0.5, 2, 0], [2.5, 2, 0]],
                             [[0.5, 0, 0], [2.5, 0, 0]]]).move(1, -2)
    
        teapot = 'https://upload.wikimedia.org/wikipedia/commons/9/93/Utah_teapot_(solid).stl'
        scene.stl(teapot).scale(0.2).move(-3, 4)
    
        scene.text('2D', 'background: rgba(0, 0, 0, 0.2); border-radius: 5px; padding: 5px').move(z=2)
        scene.text3d('3D', 'background: rgba(0, 0, 0, 0.2); border-radius: 5px; padding: 5px').move(y=-2).scale(.05)
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

See more...

Tree _link_

Display hierarchical data using Quasar's QTree component.

If using IDs, make sure they are unique within the whole tree.

To use checkboxes and on_tick, set the tick_strategy parameter to "leaf", "leaf-filtered" or "strict".

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    ui.tree([
        {'id': 'numbers', 'children': [{'id': '1'}, {'id': '2'}]},
        {'id': 'letters', 'children': [{'id': 'A'}, {'id': 'B'}]},
    ], label_key='id', on_select=lambda e: ui.notify(e.value))
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

See more...

Log View _link_

Create a log view that allows to add new lines without re-transmitting the whole history to the client.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from datetime import datetime
    from nicegui import ui
    
    log = ui.log(max_lines=10).classes('w-full h-20')
    ui.button('Log time', on_click=lambda: log.push(datetime.now().strftime('%X.%f')[:-5]))
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

See more...

Editor _link_

A WYSIWYG editor based on Quasar's QEditor. The value is a string containing the formatted text as HTML code.

_circle_ _circle_ _circle_

main.py

\[code\]

````python


    from nicegui import ui
    
    editor = ui.editor(placeholder='Type something here')
    ui.markdown().bind_content_from(editor, 'value',
                                    backward=lambda v: f'HTML code:\n```\n{v}\n```')
    
    ui.run()
    
````

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

See more...

Code _link_

This element displays a code block with syntax highlighting.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    ui.code('''
        from nicegui import ui
    
        ui.label('Code inception!')
    
        ui.run()
    ''').classes('w-full')
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

See more...

JSONEditor _link_

An element to create a JSON editor using JSONEditor. Updates can be pushed to the editor by changing the properties property. After data has changed, call the update method to refresh the editor.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    json = {
        'array': [1, 2, 3],
        'boolean': True,
        'color': '#82b92c',
        None: None,
        'number': 123,
        'object': {
            'a': 'b',
            'c': 'd',
        },
        'time': 1575599819000,
        'string': 'Hello World',
    }
    ui.json_editor({'content': {'json': json}},
                   on_select=lambda e: ui.notify(f'Select: {e}'),
                   on_change=lambda e: ui.notify(f'Change: {e}'))
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

See more...

Connection lost. Trying to reconnect...
