

← Overview

Pages & Routing

PageAuto-index pagePage LayoutParameter injectionOpenDownloadStatic filesMedia filesAPI Responses

 _Pages & Routing_

Page

This decorator marks a function to be a page builder. Each user accessing the given route will see a new instance of the page. This means it is private to the user and not shared with others (as it is
done when placing elements outside of a page decorator).

main.py

[code]
```python




    from nicegui import ui
    
    @ui.page('/other_page')
    def other_page():
        ui.label('Welcome to the other side')
        ui.link('Back to main page', '/documentation#page')
    
    @ui.page('/dark_page', dark=True)
    def dark_page():
        ui.label('Welcome to the dark side')
        ui.link('Back to main page', '/documentation#page')
    
    ui.link('Visit other page', other_page)
    ui.link('Visit dark page', dark_page)
    
    ui.run()
    


```
[/code]


NiceGUI

See more...

Auto-index page

Pages created with the `@ui.page` decorator are "private". Their content is re-created for each client. Thus, in the demo to the right, the displayed ID on the private page changes when the browser
reloads the page.

UI elements that are not wrapped in a decorated page function are placed on an automatically generated index page at route "/". This auto-index page is created once on startup and _shared_ across all
clients that might connect. Thus, each connected client will see the _same_ elements. In the demo to the right, the displayed ID on the auto-index page remains constant when the browser reloads the
page.

main.py

[code]
```python




    from nicegui import ui
    from uuid import uuid4
    
    @ui.page('/private_page')
    async def private_page():
        ui.label(f'private page with ID {uuid4()}')
    
    ui.label(f'shared auto-index page with ID {uuid4()}')
    ui.link('private page', private_page)
    
    ui.run()
    


```
[/code]


NiceGUI

Page Layout

With `ui.header`, `ui.footer`, `ui.left_drawer` and `ui.right_drawer` you can add additional layout elements to a page. The `fixed` argument controls whether the element should scroll or stay fixed on
the screen. The `top_corner` and `bottom_corner` arguments indicate whether a drawer should expand to the top or bottom of the page. See https://quasar.dev/layout/header-and-footer and
https://quasar.dev/layout/drawer for more information about possible props. With `ui.page_sticky` you can place an element "sticky" on the screen. See https://quasar.dev/layout/page-sticky for more
information.

main.py

[code]
```python




    from nicegui import ui
    
    @ui.page('/page_layout')
    def page_layout():
        ui.label('CONTENT')
        [ui.label(f'Line {i}') for i in range(100)]
        with ui.header(elevated=True).style('background-color: #3874c8').classes('items-center justify-between'):
            ui.label('HEADER')
            ui.button(on_click=lambda: right_drawer.toggle(), icon='menu').props('flat color=white')
        with ui.left_drawer(top_corner=True, bottom_corner=True).style('background-color: #d7e3f4'):
            ui.label('LEFT DRAWER')
        with ui.right_drawer(fixed=False).style('background-color: #ebf1fa').props('bordered') as right_drawer:
            ui.label('RIGHT DRAWER')
        with ui.footer().style('background-color: #3874c8'):
            ui.label('FOOTER')
    
    ui.link('show page with fancy layout', page_layout)
    
    ui.run()
    


```
[/code]


NiceGUI

Parameter injection

Thanks to FastAPI, a page function accepts optional parameters to provide path parameters, query parameters or the whole incoming request for accessing the body payload, headers, cookies and more.

main.py

[code]
```python




    from nicegui import ui
    
    @ui.page('/icon/{icon}')
    def icons(icon: str, amount: int = 1):
        ui.label(icon).classes('text-h3')
        with ui.row():
            [ui.icon(icon).classes('text-h3') for _ in range(amount)]
    ui.link('Star', '/icon/star?amount=5')
    ui.link('Home', '/icon/home')
    ui.link('Water', '/icon/water_drop?amount=3')
    
    ui.run()
    


```
[/code]


NiceGUI

Open

Can be used to programmatically trigger redirects for a specific client.

When using the new_tab parameter, the browser might block the new tab. This is a browser setting and cannot be changed by the application. You might want to use ui.link and its new_tab parameter
instead.

Note: When using an auto-index page (e.g. no @page decorator), all clients (i.e. browsers) connected to the page will open the target URL unless a socket is specified. User events like button clicks
provide such a socket.

main.py

[code]
```python




    from nicegui import ui
    
    @ui.page('/yet_another_page')
    def yet_another_page():
        ui.label('Welcome to yet another page')
        ui.button('RETURN', on_click=lambda: ui.open('documentation#open'))
    
    ui.button('REDIRECT', on_click=lambda: ui.open(yet_another_page))
    
    ui.run()
    


```
[/code]


NiceGUI

See more...

Download

Function to trigger the download of a file.

main.py

[code]
```python




    from nicegui import ui
    
    ui.button('NiceGUI Logo', on_click=lambda: ui.download('https://nicegui.io/logo.png'))
    
    ui.run()
    


```
[/code]


NiceGUI

See more...

Static files

add_static_files() makes a local directory available at the specified endpoint, e.g. '/static'. This is useful for providing local data like images to the frontend. Otherwise the browser would not be
able to access the files. Do only put non-security-critical files in there, as they are accessible to everyone.

To make a single file accessible, you can use add_static_file(). For media files which should be streamed, you can use add_media_files() or add_media_file() instead.

url_path:

    

string that starts with a slash "/" and identifies the path at which the files should be served

local_directory:

    

local folder with files to serve as static content

main.py

[code]
```python




    from nicegui import app, ui
    
    app.add_static_files('/examples', 'examples')
    ui.label('Some NiceGUI Examples').classes('text-h5')
    ui.link('AI interface', '/examples/ai_interface/main.py')
    ui.link('Custom FastAPI app', '/examples/fastapi/main.py')
    ui.link('Authentication', '/examples/authentication/main.py')
    
    ui.run()
    


```
[/code]


NiceGUI

Media files

add_media_files() allows a local files to be streamed from a specified endpoint, e.g. '/media'. This should be used for media files to support proper streaming. Otherwise the browser would not be able
to access and load the the files incrementally or jump to different positions in the stream. Do only put non-security-critical files in there, as they are accessible to everyone.

To make a single file accessible via streaming, you can use add_media_file(). For small static files, you can use add_static_files() or add_static_file() instead.

url_path:

    

string that starts with a slash "/" and identifies the path at which the files should be served

local_directory:

    

local folder with files to serve as media content

main.py

[code]
```python




    import requests
    from nicegui import app, ui
    from pathlib import Path
    
    media = Path('media')
    media.mkdir(exist_ok=True)
    r = requests.get('https://cdn.coverr.co/videos/coverr-cloudy-sky-2765/1080p.mp4')
    (media  / 'clouds.mp4').write_bytes(r.content)
    app.add_media_files('/my_videos', media)
    ui.video('/my_videos/clouds.mp4')
    
    ui.run()
    


```
[/code]


NiceGUI

API Responses

NiceGUI is based on FastAPI. This means you can use all of FastAPI's features. For example, you can implement a RESTful API in addition to your graphical user interface. You simply import the `app`
object from `nicegui`. Or you can run NiceGUI on top of your own FastAPI app by using `ui.run_with(app)` instead of starting a server automatically with `ui.run()`.

You can also return any other FastAPI response object inside a page function. For example, you can return a `RedirectResponse` to redirect the user to another page if certain conditions are met. This
is used in our authentication demo.

main.py

[code]
```python




    import random
    from nicegui import app, ui
    
    @app.get('/random/{max}')
    def generate_random_number(max: int):
        return {'min': 0, 'max': max, 'value': random.randint(0, max)}
    
    max = ui.number('max', value=100)
    ui.button('generate random number', on_click=lambda: ui.open(f'/random/{max.value:.0f}'))
    
    ui.run()
    


```
[/code]


NiceGUI

Connection lost. Trying to reconnect...

