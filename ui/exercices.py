import flet as ft


class CounterComponentUI(ft.Row):
    def __init__(self, on_minus_click = None, on_plus_click = None):
        super().__init__()
        self._quantity_text = ft.TextField(label="1")
        self._minus_button = ft.IconButton(
            icon=ft.icons.REMOVE,
            tooltip="Decrease quantity",
            on_click=on_minus_click,
        )
        self._plus_button = ft.IconButton(
            icon=ft.icons.ADD,
            tooltip="Increase quantity",
            on_click=on_plus_click,
        )


class ExerciceComponentUI(ft.Card):

    def __init__(self, counter_ui: CounterComponentUI, title: str, description: str, image_url: str | None = None):
        self._title = title
        self._description = description
        self._image_url = image_url
        self._counter_ui = counter_ui
        super().__init__()