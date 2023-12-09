

← Overview

Configuration & Deployment

URLsui.runNative ModeEnvironment VariablesServer HostingPackage for InstallationNiceGUI On Air

 _Configuration & Deployment_

URLs

You can access the list of all URLs on which the NiceGUI app is available via `app.urls`. The URLs are not available in `app.on_startup` because the server is not yet running. Instead, you can access
them in a page function or register a callback with `app.urls.on_change`.

main.py

[code]
```python




    from nicegui import app, ui
    
    @ui.page('/')
    def index():
        for url in app.urls:
            ui.link(url, target=url)
    
    ui.run()
    


```
[/code]


NiceGUI

ui.run

You can call ui.run() with optional arguments. Most of them only apply after stopping and fully restarting the app and do not apply with auto-reloading.

main.py

[code]
```python




    from nicegui import ui
    
    ui.label('page with custom title')
    
    ui.run(title='My App')
    


```
[/code]


My App

See more...

Native Mode

You can enable native mode for NiceGUI by specifying `native=True` in the `ui.run` function. To customize the initial window size and display mode, use the `window_size` and `fullscreen` parameters
respectively. Additionally, you can provide extra keyword arguments via `app.native.window_args` and `app.native.start_args`. Pick any parameter as it is defined by the internally used pywebview
module for the `webview.create_window` and `webview.start` functions. Note that these keyword arguments will take precedence over the parameters defined in `ui.run`.

In native mode the `app.native.main_window` object allows you to access the underlying window. It is an async version of `Window` from pywebview.

main.py

[code]
```python




    from nicegui import app, ui
    
    app.native.window_args['resizable'] = False
    app.native.start_args['debug'] = True
    
    ui.label('app running in native mode')
    ui.button('enlarge', on_click=lambda: app.native.main_window.resize(1000, 700))
    
    ui.run(native=True, window_size=(400, 300), fullscreen=False)
    


```
[/code]


NiceGUI

If webview has trouble finding required libraries, you may get an error relating to "WebView2Loader.dll". To work around this issue, try moving the DLL file up a directory, e.g.:

  * from `.venv/Lib/site-packages/webview/lib/x64/WebView2Loader.dll`
  * to `.venv/Lib/site-packages/webview/lib/WebView2Loader.dll`

Environment Variables

You can set the following environment variables to configure NiceGUI:

  * `MATPLOTLIB` (default: true) can be set to `false` to avoid the potentially costly import of Matplotlib. This will make `ui.pyplot` and `ui.line_plot` unavailable.
  * `NICEGUI_STORAGE_PATH` (default: local ".nicegui") can be set to change the location of the storage files.
  * `MARKDOWN_CONTENT_CACHE_SIZE` (default: 1000): The maximum number of Markdown content snippets that are cached in memory.

main.py

[code]
```python




    from nicegui import ui
    from nicegui.elements import markdown
    
    ui.label(f'Markdown content cache size is {markdown.prepare_content.cache_info().maxsize}')
    
    ui.run()
    


```
[/code]


NiceGUI

Server Hosting

To deploy your NiceGUI app on a server, you will need to execute your `main.py` (or whichever file contains your `ui.run(...)`) on your cloud infrastructure. You can, for example, just install the
NiceGUI python package via pip and use systemd or similar service to start the main script. In most cases, you will set the port to 80 (or 443 if you want to use HTTPS) with the `ui.run` command to
make it easily accessible from the outside.

A convenient alternative is the use of our pre-built multi-arch Docker image which contains all necessary dependencies. With this command you can launch the script `main.py` in the current directory
on the public port 80:

bash

[code]
```python




    docker run -it --restart always \
      -p 80:8080 \
      -e PUID=$(id -u) \
      -e PGID=$(id -g) \
      -v $(pwd)/:/app/ \
      zauberzeug/nicegui:latest
    


```
[/code]


The demo assumes `main.py` uses the port 8080 in the `ui.run` command (which is the default). The `-d` tells docker to run in background and `--restart always` makes sure the container is restarted if
the app crashes or the server reboots. Of course this can also be written in a Docker compose file:

docker-compose.yml

[code]
```python




    app:
        image: zauberzeug/nicegui:latest
        restart: always
        ports:
            - 80:8080
        environment:
            - PUID=1000 # change this to your user id
            - PGID=1000 # change this to your group id
        volumes:
            - ./:/app/
    


```
[/code]


There are other handy features in the Docker image like non-root user execution and signal pass-through. For more details we recommend to have a look at our Docker example.

You can provide SSL certificates directly using FastAPI. In production we also like using reverse proxies like Traefik or NGINX to handle these details for us. See our development docker-compose.yml
as an example.

You may also have a look at our demo for using a custom FastAPI app. This will allow you to do very flexible deployments as described in the FastAPI documentation. Note that there are additional steps
required to allow multiple workers.

Package for Installation

NiceGUI apps can also be bundled into an executable with PyInstaller. This allows you to distribute your app as a single file that can be executed on any computer.

Just take care your `ui.run` command does not use the `reload` argument. Running the `build.py` below will create an executable `myapp` in the `dist` folder:

main.py

[code]
```python




    from nicegui import native, ui
    
    ui.label('Hello from PyInstaller')
    
    ui.run(reload=False, port=native.find_open_port())
    


```
[/code]


build.py

[code]
```python




    import os
    import subprocess
    from pathlib import Path
    import nicegui
    
    cmd = [
        'python',
        '-m', 'PyInstaller',
        'main.py', # your main file with ui.run()
        '--name', 'myapp', # name of your app
        '--onefile',
        #'--windowed', # prevent console appearing, only use with ui.run(native=True, ...)
        '--add-data', f'{Path(nicegui.__file__).parent}{os.pathsep}nicegui'
    ]
    subprocess.call(cmd)
    


```
[/code]


**Packaging Tips**

  * When building a PyInstaller app, your main script can use a native window (rather than a browser window) by using `ui.run(reload=False, native=True)`. The `native` parameter can be `True` or `False` depending on whether you want a native window or to launch a page in the user's browser - either will work in the PyInstaller generated app.

  * Specifying `--windowed` to PyInstaller will prevent a terminal console from appearing. However you should only use this option if you have also specified `native=True` in your `ui.run` command. Without a terminal console the user won't be able to exit the app by pressing Ctrl-C. With the `native=True` option, the app will automatically close when the window is closed, as expected.

  * Specifying `--windowed` to PyInstaller will create an `.app` file on Mac which may be more convenient to distribute. When you double-click the app to run it, it will not show any console output. You can also run the app from the command line with `./myapp.app/Contents/MacOS/myapp` to see the console output.

  * Specifying `--onefile` to PyInstaller will create a single executable file. Whilst convenient for distribution, it will be slower to start up. This is not NiceGUI's fault but just the way Pyinstaller zips things into a single file, then unzips everything into a temporary directory before running. You can mitigate this by removing `--onefile` from the PyInstaller command, and zip up the generated `dist` directory yourself, distribute it, and your end users can unzip once and be good to go, without the constant expansion of files due to the `--onefile` flag.

  * Summary of user experience for different options:

PyInstaller | `ui.run(...)` | Explanation  
---|---|---  
`onefile` | `native=False` | Single executable generated in `dist/`, runs in browser  
`onefile` | `native=True` | Single executable generated in `dist/`, runs in popup window  
`onefile` and `windowed` | `native=True` | Single executable generated in `dist/` (on Mac a proper `dist/myapp.app` generated incl. icon), runs in popup window, no console appears  
`onefile` and `windowed` | `native=False` | Avoid (no way to exit the app)  
Specify neither |  | A `dist/myapp` directory created which can be zipped manually and distributed; run with `dist/myapp/myapp`  
  * If you are using a Python virtual environment, ensure you `pip install pyinstaller` within your virtual environment so that the correct PyInstaller is used, or you may get broken apps due to the wrong version of PyInstaller being picked up. That is why the build script invokes PyInstaller using `python -m PyInstaller` rather than just `pyinstaller`.

bash

[code]
```python




    python -m venv venv
    source venv/bin/activate
    pip install nicegui
    pip install pyinstaller
    


```
[/code]


**Note:** If you're getting an error "TypeError: a bytes-like object is required, not 'str'", try adding the following lines to the top of your `main.py` file:

[code]
```python




    import sys
    sys.stdout = open('logs.txt', 'w')
    


```
[/code]


See https://github.com/zauberzeug/nicegui/issues/681 for more information.

NiceGUI On Air

By using `ui.run(on_air=True)` you can share your local app with others over the internet 🧞.

When accessing the on-air URL, all libraries (like Vue, Quasar, ...) are loaded from our CDN. Thereby only the raw content and events need to be transmitted by your local app. This makes it blazing
fast even if your app only has a poor internet connection (e.g. a mobile robot in the field).

By setting `on_air=True` you will get a random URL which is valid for 1 hour. If you sign-up at https://on-air.nicegui.io you get a token which could be used to identify your device:
`ui.run(on_air='<your token>'`). This will give you a fixed URL and the possibility to protect remote access with a passphrase.

Currently On Air is available as a tech preview and can be used free of charge (for now). We will gradually improve stability, introduce payment options and extend the service with multi-device
management, remote terminal access and more. Please let us know your feedback on GitHub, Reddit, or Discord.

**Data Privacy:** We take your privacy very serious. NiceGUI On Air does not log or store any content of the relayed data.

Connection lost. Trying to reconnect...

