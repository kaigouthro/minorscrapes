

Reference, Demos and more

 _NiceGUI_ Documentation

### Overview

NiceGUI is an open-source Python library to write graphical user interfaces which run in the browser. It has a very gentle learning curve while still offering the option for advanced customizations.
NiceGUI follows a backend-first philosophy: It handles all the web development details. You can focus on writing Python code. This makes it ideal for a wide range of projects including short scripts,
dashboards, robotics projects, IoT solutions, smart home automation, and machine learning.

### How to use this guide

This documentation explains how to use NiceGUI. Each of the tiles covers a NiceGUI topic in detail. It is recommended to start by reading this entire introduction page, then refer to other sections as
needed.

### Basic concepts

NiceGUI provides UI _components_ (or _elements_ ) such as buttons, sliders, text, images, charts, and more. Your app assembles these components into _pages_. When the user interacts with an item on a
page, NiceGUI triggers an _event_ (or _action_ ). You define code to _handle_ each event, such as what to do when a user clicks a button named "Go".

Components are arranged on a page using _layouts_. Layouts provide things like grids, tabs, carousels, expansions, menus, and other tools to arrange your components. Many components are linked to a
_model_ (data object) in your code, which automatically updates the user interface when the value changes.

Styling and appearance can be controlled in several ways. NiceGUI accepts optional arguments for certain styling, such as icons on buttons. Other styling can be set with functions such as `.styles`,
`.classes`, or `.props` that you'll learn about later. Global styles like colors and fonts can be set with dedicated properties. Or if you prefer, almost anything can be styled with CSS.

Text Elements

Elements like `ui.label`, `ui.markdown` and `ui.html` can be used to display text and other content.

Controls

NiceGUI provides a variety of elements for user interaction, e.g. `ui.button`, `ui.slider`, `ui.inputs`, etc.

Audiovisual Elements

You can use elements like `ui.image`, `ui.audio`, `ui.video`, etc. to display audiovisual content.

Data Elements

There are several elements for displaying data, e.g. `ui.table`, `ui.aggrid`, `ui.highchart`, `ui.echart`, etc.

Binding Properties

To update UI elements automatically, you can bind them to each other or to your data model.

Page Layout

This section covers fundamental techniques as well as several elements to structure your UI.

Styling & Appearance

NiceGUI allows to customize the appearance of UI elements in various ways, including CSS, Tailwind CSS and Quasar properties.

Action & Events

This section covers timers, UI events, and the lifecycle of NiceGUI apps.

Pages & Routing

A NiceGUI app can consist of multiple pages and other FastAPI endpoints.

Configuration & Deployment

Whether you want to run your app locally or on a server, native or in a browser, we got you covered.

### Actions

NiceGUI runs an event loop to handle user input and other events like timers and keyboard bindings. You can write asynchronous functions for long-running tasks to keep the UI responsive. The _Actions_
section covers how to work with events.

### Implementation

NiceGUI is implemented with HTML components served by an HTTP server (FastAPI), even for native windows. If you already know HTML, everything will feel very familiar. If you don't know HTML, that's
fine too! NiceGUI abstracts away the details, so you can focus on creating beautiful interfaces without worrying about how they are implemented.

### Running NiceGUI Apps

There are several options for deploying NiceGUI. By default, NiceGUI runs a server on localhost and runs your app as a private web page on the local machine. When run this way, your app appears in a
web browser window. You can also run NiceGUI in a native window separate from a web browser. Or you can run NiceGUI on a server that handles many clients - the website you're reading right now is
served from NiceGUI.

After creating your app pages with components, you call `ui.run()` to start the NiceGUI server. Optional parameters to `ui.run` set things like the network address and port the server binds to,
whether the app runs in native mode, initial window size, and many other options. The section _Configuration and Deployment_ covers the options to the `ui.run()` function and the FastAPI framework it
is based on.

### Customization

If you want more customization in your app, you can use the underlying Tailwind classes and Quasar components to control the style or behavior of your components. You can also extend the available
components by subclassing existing NiceGUI components or importing new ones from Quasar. All of this is optional. Out of the box, NiceGUI provides everything you need to make modern, stylish,
responsive user interfaces.

Connection lost. Trying to reconnect...

