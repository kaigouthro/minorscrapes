

← Overview

Text Elements

LabelLinkChat MessageGeneric ElementMarkdown ElementMermaid DiagramsHTML Element

 _Text Elements_

Label

Displays some text.

main.py

[code]
```python




    from nicegui import ui
    
    ui.label('some label')
    
    ui.run()
    


```
[/code]


NiceGUI

See more...

Link

Create a hyperlink.

To jump to a specific location within a page you can place linkable anchors with ui.link_target("name") and link to it with ui.link(target="#name").

main.py

[code]
```python




    from nicegui import ui
    
    ui.link('NiceGUI on GitHub', 'https://github.com/zauberzeug/nicegui')
    
    ui.run()
    


```
[/code]


NiceGUI

See more...

Chat Message

Based on Quasar's Chat Message component.

main.py

[code]
```python




    from nicegui import ui
    
    ui.chat_message('Hello NiceGUI!',
                    name='Robot',
                    stamp='now',
                    avatar='https://robohash.org/ui')
    
    ui.run()
    


```
[/code]


NiceGUI

See more...

Generic Element

This class is the base class for all other UI elements. But you can use it to create elements with arbitrary HTML tags.

main.py

[code]
```python




    from nicegui import ui
    
    with ui.element('div').classes('p-2 bg-blue-100'):
        ui.label('inside a colored div')
    
    ui.run()
    


```
[/code]


NiceGUI

See more...

Markdown Element

Renders Markdown onto the page.

main.py

[code]
```python




    from nicegui import ui
    
    ui.markdown('''This is **Markdown**.''')
    
    ui.run()
    


```
[/code]


NiceGUI

See more...

Mermaid Diagrams

Renders diagrams and charts written in the Markdown-inspired Mermaid language. The mermaid syntax can also be used inside Markdown elements by providing the extension string 'mermaid' to the
ui.markdown element.

main.py

[code]
```python




    from nicegui import ui
    
    ui.mermaid('''
    graph LR;
        A --> B;
        A --> C;
    ''')
    
    ui.run()
    


```
[/code]


NiceGUI

See more...

HTML Element

Renders arbitrary HTML onto the page. Tailwind can be used for styling. You can also use ui.add_head_html to add html code into the head of the document and ui.add_body_html to add it into the body.

main.py

[code]
```python




    from nicegui import ui
    
    ui.html('This is <strong>HTML</strong>.')
    
    ui.run()
    


```
[/code]


NiceGUI

See more...

Connection lost. Trying to reconnect...

