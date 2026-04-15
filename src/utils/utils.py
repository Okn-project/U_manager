from PyQt5.QtWidgets import QLayout


def clear_layout(layout: QLayout) -> None:
    if layout is None:
        return

    while layout.count():

        item = layout.takeAt(0)

        widget = item.widget()
        if widget is not None:
            widget.deleteLater()

        child_layout = item.layout()
        if child_layout is not None:
            clear_layout(child_layout)


def remove_stretch(layout: QLayout):
    for i in range(layout.count() - 1, -1, -1):
        item = layout.itemAt(i)
        if item.widget() is None and item.layout() is None:
            layout.takeAt(i)
            del item
