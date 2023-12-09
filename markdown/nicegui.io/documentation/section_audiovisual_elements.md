

← Overview

Audiovisual Elements

ImageCaptions and OverlaysInteractive ImageAudioVideoIconAvatarSVG

 _Audiovisual Elements_

Image

Displays an image. This element is based on Quasar's QImg component.

main.py

[code]
```python




    from nicegui import ui
    
    ui.image('https://picsum.photos/id/377/640/360')
    
    ui.run()
    


```
[/code]


NiceGUI

See more...

Captions and Overlays

By nesting elements inside a `ui.image` you can create augmentations.

Use Quasar classes for positioning and styling captions. To overlay an SVG, make the `viewBox` exactly the size of the image and provide `100%` width/height to match the actual rendered size.

main.py

[code]
```python




    from nicegui import ui
    
    with ui.image('https://picsum.photos/id/29/640/360'):
        ui.label('Nice!').classes('absolute-bottom text-subtitle2 text-center')
    
    with ui.image('https://cdn.stocksnap.io/img-thumbs/960w/airplane-sky_DYPWDEEILG.jpg'):
        ui.html('''
            <svg viewBox="0 0 960 638" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
            <circle cx="445" cy="300" r="100" fill="none" stroke="red" stroke-width="20" />
            </svg>
        ''').classes('bg-transparent')
    
    ui.run()
    


```
[/code]


NiceGUI

Interactive Image

Create an image with an SVG overlay that handles mouse events and yields image coordinates. It is also the best choice for non-flickering image updates. If the source URL changes faster than images
can be loaded by the browser, some images are simply skipped. Thereby repeatedly updating the image source will automatically adapt to the available bandwidth. See OpenCV Webcam for an example.

main.py

[code]
```python




    from nicegui import ui
    from nicegui.events import MouseEventArguments
    
    def mouse_handler(e: MouseEventArguments):
        color = 'SkyBlue' if e.type == 'mousedown' else 'SteelBlue'
        ii.content += f'<circle cx="{e.image_x}" cy="{e.image_y}" r="15" fill="none" stroke="{color}" stroke-width="4" />'
        ui.notify(f'{e.type} at ({e.image_x:.1f}, {e.image_y:.1f})')
    
    src = 'https://picsum.photos/id/565/640/360'
    ii = ui.interactive_image(src, on_mouse=mouse_handler, events=['mousedown', 'mouseup'], cross=True)
    
    ui.run()
    


```
[/code]


NiceGUI

See more...

Audio

Displays an audio player.

See here for a list of events you can subscribe to using the generic event subscription on().

main.py

[code]
```python




    from nicegui import ui
    
    a = ui.audio('https://cdn.pixabay.com/download/audio/2022/02/22/audio_d1718ab41b.mp3')
    a.on('ended', lambda _: ui.notify('Audio playback completed'))
    
    ui.button(on_click=lambda: a.props('muted'), icon='volume_off').props('outline')
    ui.button(on_click=lambda: a.props(remove='muted'), icon='volume_up').props('outline')
    
    ui.run()
    


```
[/code]


NiceGUI

See more...

Video

Displays a video.

See here for a list of events you can subscribe to using the generic event subscription on().

main.py

[code]
```python




    from nicegui import ui
    
    v = ui.video('https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4')
    v.on('ended', lambda _: ui.notify('Video playback completed'))
    
    ui.run()
    


```
[/code]


NiceGUI

See more...

Icon

This element is based on Quasar's QIcon component.

Here is a reference of possible names.

main.py

[code]
```python




    from nicegui import ui
    
    ui.icon('thumb_up', color='primary').classes('text-5xl')
    
    ui.run()
    


```
[/code]


NiceGUI

See more...

Avatar

A avatar element wrapping Quasar's QAvatar component.

main.py

[code]
```python




    from nicegui import ui
    
    ui.avatar('favorite_border', text_color='grey-11', square=True)
    ui.avatar('img:https://nicegui.io/logo_square.png', color='blue-2')
    
    ui.run()
    


```
[/code]


NiceGUI

See more...

SVG

You can add Scalable Vector Graphics using the `ui.html` element.

main.py

[code]
```python




    from nicegui import ui
    
    content = '''
        <svg viewBox="0 0 200 200" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
        <circle cx="100" cy="100" r="78" fill="#ffde34" stroke="black" stroke-width="3" />
        <circle cx="80" cy="85" r="8" />
        <circle cx="120" cy="85" r="8" />
        <path d="m60,120 C75,150 125,150 140,120" style="fill:none; stroke:black; stroke-width:8; stroke-linecap:round" />
        </svg>'''
    ui.html(content)
    
    ui.run()
    


```
[/code]


NiceGUI

Connection lost. Trying to reconnect...

