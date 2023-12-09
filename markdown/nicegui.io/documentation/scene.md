InstallationFeaturesDemosDocumentationExamplesWhy?

_search_

_dark_mode_ _light_mode_ _brightness_auto_

_more_vert_

← Overview

**Demos**

Handling Click EventsDraggable objectsRendering point clouds

**Reference**

PropertiesMethodsInherited from

Documentation

ui. _scene_

Display a 3D scene using three.js. Currently NiceGUI supports boxes, spheres, cylinders/cones, extrusions, straight lines, curves and textured meshes. Objects can be translated, rotated and displayed
with different color, opacity or as wireframes. They can also be grouped to apply joint movements.

width:

width of the canvas

height:

height of the canvas

grid:

whether to display a grid

on_click:

callback to execute when a 3D object is clicked

on_drag_start:

callback to execute when a 3D object is dragged

on_drag_end:

callback to execute when a 3D object is dropped

drag_constraints:

comma-separated JavaScript expression for constraining positions of dragged objects (e.g. 'x = 0, z = y / 2')

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

Handling Click Events

_link_

You can use the `on_click` argument to `ui.scene` to handle click events. The callback receives a `SceneClickEventArguments` object with the following attributes:

- `click_type`: the type of click ("click" or "dblclick").
- `button`: the button that was clicked (1, 2, or 3).
- `alt`, `ctrl`, `meta`, `shift`: whether the alt, ctrl, meta, or shift key was pressed.
- `hits`: a list of `SceneClickEventHit` objects, sorted by distance from the camera.

The `SceneClickEventHit` object has the following attributes:

- `object_id`: the id of the object that was clicked.
- `object_name`: the name of the object that was clicked.
- `x`, `y`, `z`: the x, y and z coordinates of the click.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import events, ui
    
    def handle_click(e: events.SceneClickEventArguments):
        hit = e.hits[0]
        name = hit.object_name or hit.object_id
        ui.notify(f'You clicked on the {name} at ({hit.x:.2f}, {hit.y:.2f}, {hit.z:.2f})')
    
    with ui.scene(width=285, height=220, on_click=handle_click) as scene:
        scene.sphere().move(x=-1, z=1).with_name('sphere')
        scene.box().move(x=1, z=1).with_name('box')
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

Draggable objects

_link_

You can make objects draggable using the `.draggable` method. There is an optional `on_drag_start` and `on_drag_end` argument to `ui.scene` to handle drag events. The callbacks receive a
`SceneDragEventArguments` object with the following attributes:

- `type`: the type of drag event ("dragstart" or "dragend").
- `object_id`: the id of the object that was dragged.
- `object_name`: the name of the object that was dragged.
- `x`, `y`, `z`: the x, y and z coordinates of the dragged object.

You can also use the `drag_constraints` argument to set comma-separated JavaScript expressions for constraining positions of dragged objects.

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    from nicegui import events, ui
    
    def handle_drag(e: events.SceneDragEventArguments):
        ui.notify(f'You dropped the sphere at ({e.x:.2f}, {e.y:.2f}, {e.z:.2f})')
    
    with ui.scene(width=285, height=220,
                  drag_constraints='z = 1', on_drag_end=handle_drag) as scene:
        sphere = scene.sphere().move(z=1).draggable()
    
    ui.switch('draggable sphere',
              value=sphere.draggable_,
              on_change=lambda e: sphere.draggable(e.value))
    
    ui.run()
    
```

\[/code\]

_content_copy_

_circle_ _circle_ _circle_

NiceGUI

Rendering point clouds

_link_

You can render point clouds using the `point_cloud` method. The `points` argument is a list of point coordinates, and the `colors` argument is a list of RGB colors (0..1).

_circle_ _circle_ _circle_

main.py

\[code\]

```python


    import numpy as np
    from nicegui import ui
    
    with ui.scene().classes('w-full h-64') as scene:
        x, y = np.meshgrid(np.linspace(-3, 3), np.linspace(-3, 3))
        z = np.sin(x) * np.cos(y) + 1
        points = np.dstack([x, y, z]).reshape(-1, 3)
        scene.point_cloud(points=points, colors=points, point_size=0.1)
    
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

Remove all objects from the scene.

**`delete`**`() -> None`

Delete the element.

**`delete_objects`**`(predicate: Callable[[nicegui.elements.scene_object3d.Object3D], bool] = [...]) -> None`

Remove objects from the scene.

> predicate:
>
> function which returns True for objects which should be deleted

**`move`**`(target_container: Optional[Element] = None, target_index: int = -1)`

Move the element to another container.

> target_container:
>
> container to move the element to (default: the parent container)
>
> target_index:
>
> index within the target slot (default: append to the end)

**`move_camera`**`(x: Optional[float] = None, y: Optional[float] = None, z: Optional[float] = None, look_at_x: Optional[float] = None, look_at_y: Optional[float] = None, look_at_z: Optional[float] = None, up_x: Optional[float] = None, up_y: Optional[float] = None, up_z: Optional[float] = None, duration: float = 0.5) -> None`

Move the camera to a new position.

> x:
>
> camera x position
>
> y:
>
> camera y position
>
> z:
>
> camera z position
>
> look_at_x:
>
> camera look-at x position
>
> look_at_y:
>
> camera look-at y position
>
> look_at_z:
>
> camera look-at z position
>
> up_x:
>
> x component of the camera up vector
>
> up_y:
>
> y component of the camera up vector
>
> up_z:
>
> z component of the camera up vector
>
> duration:
>
> duration of the movement in seconds (default: 0.5)

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

**`run_method`**`(name: str, *args: Any, timeout: float = 1, check_interval: float = 0.01) -> nicegui.awaitable_response.AwaitableResponse`

Run a method on the client.

> name:
>
> name of the method
>
> args:
>
> arguments to pass to the method

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

- `Element`

- `Visibility`

Connection lost. Trying to reconnect...
