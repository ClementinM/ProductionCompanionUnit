from .pcu_widget_multithread import PCUwidgetMultithread


class PCUmenu(PCUwidgetMultithread):
    def __init__(self, parent, resize_to_parent=True):
        super(PCUmenu, self).__init__(parent=parent)
        self.parent = parent
        self.name = ''
        self.module_bar_name = ''
        self.module_bar_button = None

        if resize_to_parent:
            self.resize(self.parent.width(), self.parent.height())

    def load_menu(self):
        pass

