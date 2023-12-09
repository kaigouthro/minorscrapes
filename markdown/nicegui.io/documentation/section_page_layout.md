_menu_

InstallationFeaturesDemosDocumentationExamplesWhy?

_search_

_dark_mode_ _light_mode_ _brightness_auto_

_more_vert_

← Overview

Page Layout

Auto-contextCardColumn ElementRow ElementGrid ElementClear ContainersExpansion ElementScroll AreaSeparatorSplitterTabsStepperTimelineCarouselPaginationMenuContext MenuTooltipsNotificationDialog

_Page Layout_

Auto-context

_link_

In order to allow writing intuitive UI descriptions, NiceGUI automatically tracks the context in which elements are created. This means that there is no explicit `parent` parameter. Instead the parent
context is defined using a `with` statement. It is also passed to event handlers and timers.

In the demo, the label "Card content" is added to the card. And because the `ui.button` is also added to the card, the label "Click!" will also be created in this context. The label "Tick!", which is
added once after one second, is also added to the card.

This design decision allows for easily creating modular components that keep working after moving them around in the UI. For example, you can move label and button somewhere else, maybe wrap them in
another container, and the code will still work.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    with ui.card():
        ui.label('Card content')
        ui.button('Add label', on_click=lambda: ui.label('Click!'))
        ui.timer(1.0, lambda: ui.label('Tick!'), once=True)
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

Card _link_

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

See more...

Column Element _link_

Provides a container which arranges its child in a column.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    with ui.column():
        ui.label('label 1')
        ui.label('label 2')
        ui.label('label 3')
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

See more...

Row Element _link_

Provides a container which arranges its child in a row.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    with ui.row():
        ui.label('label 1')
        ui.label('label 2')
        ui.label('label 3')
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

See more...

Grid Element _link_

Provides a container which arranges its child in a grid.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    with ui.grid(columns=2):
        ui.label('Name:')
        ui.label('Tom')
    
        ui.label('Age:')
        ui.label('42')
    
        ui.label('Height:')
        ui.label('1.80m')
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

See more...

Clear Containers

_link_

To remove all elements from a row, column or card container, use can call

\[code\]

```python


    container.clear()
    
```

\[/code\]

Alternatively, you can remove individual elements by calling

- `container.remove(element: Element)`,
- `container.remove(index: int)`, or
- `element.delete()`.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    container = ui.row()
    
    def add_face():
        with container:
            ui.icon('face')
    add_face()
    
    ui.button('Add', on_click=add_face)
    ui.button('Remove', on_click=lambda: container.remove(0) if list(container) else None)
    ui.button('Clear', on_click=container.clear)
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

Expansion Element _link_

Provides an expandable container based on Quasar's QExpansionItem component.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    with ui.expansion('Expand!', icon='work').classes('w-full'):
        ui.label('inside the expansion')
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

See more...

Scroll Area _link_

A way of customizing the scrollbars by encapsulating your content. This element exposes the Quasar ScrollArea component.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    with ui.row():
        with ui.scroll_area().classes('w-32 h-32 border'):
            ui.label('I scroll. ' * 20)
        with ui.column().classes('p-4 w-32 h-32 border'):
            ui.label('I will not scroll. ' * 10)
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

See more...

Separator _link_

This element is based on Quasar's QSeparator component.

It serves as a separator for cards, menus and other component containers and is similar to HTML's <hr> tag.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    ui.label('text above')
    ui.separator()
    ui.label('text below')
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

See more...

Splitter _link_

The ui.splitter element divides the screen space into resizable sections, allowing for flexible and responsive layouts in your application.

Based on Quasar's Splitter component: Splitter

It provides three customizable slots, before, after, and separator, which can be used to embed other elements within the splitter.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    with ui.splitter() as splitter:
        with splitter.before:
            ui.label('This is some content on the left hand side.').classes('mr-2')
        with splitter.after:
            ui.label('This is some content on the right hand side.').classes('ml-2')
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

See more...

Tabs _link_

The elements ui.tabs, ui.tab, ui.tab_panels, and ui.tab_panel resemble Quasar's tabs and tab panels API.

ui.tabs creates a container for the tabs. This could be placed in a ui.header for example. ui.tab_panels creates a container for the tab panels with the actual content. Each ui.tab_panel is associated
with a ui.tab element.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    with ui.tabs().classes('w-full') as tabs:
        one = ui.tab('One')
        two = ui.tab('Two')
    with ui.tab_panels(tabs, value=two).classes('w-full'):
        with ui.tab_panel(one):
            ui.label('First tab')
        with ui.tab_panel(two):
            ui.label('Second tab')
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

See more...

Stepper _link_

This element represents Quasar's QStepper component. It contains individual steps.

To avoid issues with dynamic elements when switching steps, this element uses Vue's keep-alive component. If client-side performance is an issue, you can disable this feature.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    with ui.stepper().props('vertical').classes('w-full') as stepper:
        with ui.step('Preheat'):
            ui.label('Preheat the oven to 350 degrees')
            with ui.stepper_navigation():
                ui.button('Next', on_click=stepper.next)
        with ui.step('Ingredients'):
            ui.label('Mix the ingredients')
            with ui.stepper_navigation():
                ui.button('Next', on_click=stepper.next)
                ui.button('Back', on_click=stepper.previous).props('flat')
        with ui.step('Bake'):
            ui.label('Bake for 20 minutes')
            with ui.stepper_navigation():
                ui.button('Done', on_click=lambda: ui.notify('Yay!', type='positive'))
                ui.button('Back', on_click=stepper.previous).props('flat')
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

See more...

Timeline _link_

This element represents Quasar's QTimeline component.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    with ui.timeline(side='right'):
        ui.timeline_entry('Rodja and Falko start working on NiceGUI.',
                          title='Initial commit',
                          subtitle='May 07, 2021')
        ui.timeline_entry('The first PyPI package is released.',
                          title='Release of 0.1',
                          subtitle='May 14, 2021')
        ui.timeline_entry('Large parts are rewritten to remove JustPy '
                          'and to upgrade to Vue 3 and Quasar 2.',
                          title='Release of 1.0',
                          subtitle='December 15, 2022',
                          icon='rocket')
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

See more...

Carousel _link_

This element represents Quasar's QCarousel component. It contains individual carousel slides.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    with ui.carousel(animated=True, arrows=True, navigation=True).props('height=180px'):
        with ui.carousel_slide().classes('p-0'):
            ui.image('https://picsum.photos/id/30/270/180').classes('w-[270px]')
        with ui.carousel_slide().classes('p-0'):
            ui.image('https://picsum.photos/id/31/270/180').classes('w-[270px]')
        with ui.carousel_slide().classes('p-0'):
            ui.image('https://picsum.photos/id/32/270/180').classes('w-[270px]')
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

See more...

Pagination _link_

A pagination element wrapping Quasar's QPagination component.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    p = ui.pagination(1, 5, direction_links=True)
    ui.label().bind_text_from(p, 'value', lambda v: f'Page {v}')
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

See more...

Menu _link_

Creates a menu based on Quasar's QMenu component. The menu should be placed inside the element where it should be shown.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    with ui.row().classes('w-full items-center'):
        result = ui.label().classes('mr-auto')
        with ui.button(icon='menu'):
            with ui.menu() as menu:
                ui.menu_item('Menu item 1', lambda: result.set_text('Selected item 1'))
                ui.menu_item('Menu item 2', lambda: result.set_text('Selected item 2'))
                ui.menu_item('Menu item 3 (keep open)',
                             lambda: result.set_text('Selected item 3'), auto_close=False)
                ui.separator()
                ui.menu_item('Close', on_click=menu.close)
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

See more...

Context Menu _link_

Creates a context menu based on Quasar's QMenu component. The context menu should be placed inside the element where it should be shown. It is automatically opened when the user right-clicks on the
element and appears at the mouse position.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    with ui.image('https://picsum.photos/id/377/640/360'):
        with ui.context_menu():
            ui.menu_item('Flip horizontally')
            ui.menu_item('Flip vertically')
            ui.separator()
            ui.menu_item('Reset')
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

See more...

Tooltips

_link_

Simply call the `tooltip(text:str)` method on UI elements to provide a tooltip.

For more artistic control you can nest tooltip elements and apply props, classes and styles.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    ui.label('Tooltips...').tooltip('...are shown on mouse over')
    with ui.button(icon='thumb_up'):
        ui.tooltip('I like this').classes('bg-green')
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

Notification _link_

Displays a notification on the screen.

Note: You can pass additional keyword arguments according to Quasar's Notify API.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    ui.button('Say hi!', on_click=lambda: ui.notify('Hi!', close_button='OK'))
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

See more...

Dialog _link_

Creates a dialog based on Quasar's QDialog component. By default it is dismissible by clicking or pressing ESC. To make it persistent, set .props('persistent') on the dialog element.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import ui
    
    with ui.dialog() as dialog, ui.card():
        ui.label('Hello world!')
        ui.button('Close', on_click=dialog.close)
    
    ui.button('Open a dialog', on_click=dialog.open)
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

See more...

Connection lost. Trying to reconnect...
