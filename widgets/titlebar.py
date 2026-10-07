from PyQt6 import QtCore, QtWidgets


class TitleBar(QtWidgets.QFrame): # <- custom title bar, no assets, just because
    def __init__(self, window):
        super().__init__()

        self.window = window
        self.dragPosition = None

        self.setObjectName("titleBar")
        self.setFixedHeight(32)

        self.titleLabel = QtWidgets.QLabel("Password Generator")
        self.titleLabel.setObjectName("windowTitle")
        self.titleLabel.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents)

        self.minimizeButton = QtWidgets.QPushButton("-")
        self.minimizeButton.setObjectName("minimizeButton")
        self.minimizeButton.setFixedSize(42, 32)
        self.minimizeButton.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)

        self.closeButton = QtWidgets.QPushButton("×")
        self.closeButton.setObjectName("closeButton")
        self.closeButton.setFixedSize(42, 32)
        self.closeButton.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)

        self.minimizeButton.clicked.connect(self.window.showMinimized)
        self.closeButton.clicked.connect(self.window.close)

        # --- layouts  ---
        layout = QtWidgets.QHBoxLayout(self)
        layout.setContentsMargins(12, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(self.titleLabel)
        layout.addStretch()
        layout.addWidget(self.minimizeButton)
        layout.addWidget(self.closeButton)

    # --- window dragging ---
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.dragPosition = event.globalPosition().toPoint() - self.window.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() & QtCore.Qt.MouseButton.LeftButton and self.dragPosition is not None:
            self.window.move(event.globalPosition().toPoint() - self.dragPosition)
            event.accept()

    def mouseReleaseEvent(self, event):
        self.dragPosition = None
        event.accept()