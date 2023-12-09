

← Overview

**Demos**

Pages with Path ParametersWait for Client ConnectionModularize with APIRouter

 **Reference**

PropertiesMethods

Documentation

ui. _page_

This decorator marks a function to be a page builder. Each user accessing the given route will see a new instance of the page. This means it is private to the user and not shared with others (as it is
done when placing elements outside of a page decorator).

path:

    

route of the new page (path must start with '/')

title:

    

optional page title

viewport:

    

optional viewport meta tag content

favicon:

    

optional relative filepath or absolute URL to a favicon (default: None, NiceGUI icon will be used)

dark:

    

whether to use Quasar's dark mode (defaults to dark argument of run command)

language:

    

language of the page (defaults to language argument of run command)

response_timeout:

    

maximum time for the decorated function to build the page (default: 3.0 seconds)

reconnect_timeout:

    

maximum time the server waits for the browser to reconnect (default: 0.0 seconds)

api_router:

    

APIRouter instance to use, can be left None to use the default

kwargs:

    

additional keyword arguments passed to FastAPI's @app.get method

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

Pages with Path Parameters

Page routes can contain parameters like FastAPI. If type-annotated, they are automatically converted to bool, int, float and complex values. If the page function expects a `request` argument, the
request object is automatically provided. The `client` argument provides access to the websocket connection, layout, etc.

main.py

[code]
```python




    from nicegui import ui
    
    @ui.page('/repeat/{word}/{count}')
    def page(word: str, count: int):
        ui.label(word * count)
    
    ui.link('Say hi to Santa!', '/repeat/Ho! /3')
    
    ui.run()
    


```
[/code]


NiceGUI

Wait for Client Connection

To wait for a client connection, you can add a `client` argument to the decorated page function and await `client.connected()`. All code below that statement is executed after the websocket connection
between server and client has been established.

For example, this allows you to run JavaScript commands; which is only possible with a client connection (see #112). Also it is possible to do async stuff while the user already sees some content.

main.py

[code]
```python




    import asyncio
    from nicegui import Client, ui
    
    @ui.page('/wait_for_connection')
    async def wait_for_connection(client: Client):
        ui.label('This text is displayed immediately.')
        await client.connected()
        await asyncio.sleep(2)
        ui.label('This text is displayed 2 seconds after the page has been fully loaded.')
        ui.label(f'The IP address {client.ip} was obtained from the websocket.')
    
    ui.link('wait for connection', wait_for_connection)
    
    ui.run()
    


```
[/code]


NiceGUI

Modularize with APIRouter

You can use the NiceGUI specialization of FastAPI's APIRouter to modularize your code by grouping pages and other routes together. This is especially useful if you want to reuse the same prefix for
multiple pages. The router and its pages can be neatly tugged away in a separate module (e.g. file) and the router is simply imported and included in the main app. See our modularization example for a
multi-file app structure.

main.py

[code]
```python




    from nicegui import APIRouter, app, ui
    
    router = APIRouter(prefix='/sub-path')
    
    @router.page('/')
    def page():
        ui.label('This is content on /sub-path')
    
    @router.page('/sub-sub-path')
    def page():
        ui.label('This is content on /sub-path/sub-sub-path')
    
    ui.link('Visit sub-path', '/sub-path')
    ui.link('Visit sub-sub-path', '/sub-path/sub-sub-path')
    
    app.include_router(router)
    
    ui.run()
    


```
[/code]


/sub-path

## Reference

Properties

 **`path`**`: 'str'`

The path of the page including the APIRouter's prefix.

Methods

 **`resolve_dark`**`() -> Optional[bool]`

Return whether the page should use dark mode.

**`resolve_language`**`() -> Optional[str]`

Return the language of the page.

**`resolve_title`**`() -> str`

Return the title of the page.

**`resolve_viewport`**`() -> str`

Return the viewport of the page.

Connection lost. Trying to reconnect...

