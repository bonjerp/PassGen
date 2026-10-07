from PyQt6 import QtCore, QtGui, QtWidgets


class BlueCheckBox(QtWidgets.QCheckBox): # <- custom checkbox 
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        self.setFixedSize(24, 24)

    # --- draw checkbox ---
    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
        rect = QtCore.QRectF(2, 2, 20, 20)

        if self.isChecked():
            painter.setBrush(QtGui.QColor("#3B82F6"))
            painter.setPen(QtGui.QPen(QtGui.QColor("#5794FF"), 1))
            painter.drawRoundedRect(rect, 5, 5)

            pen = QtGui.QPen(QtGui.QColor("#FFFFFF"), 2)
            pen.setCapStyle(QtCore.Qt.PenCapStyle.RoundCap)
            pen.setJoinStyle(QtCore.Qt.PenJoinStyle.RoundJoin)
            painter.setPen(pen)

            path = QtGui.QPainterPath()
            path.moveTo(6, 12)
            path.lineTo(10, 16)
            path.lineTo(18, 7)
            painter.drawPath(path)

        else:
            painter.setBrush(QtGui.QColor("#151E29"))
            painter.setPen(QtGui.QPen(QtGui.QColor("#445269"), 1))
            painter.drawRoundedRect(rect, 5, 5)


class OptionCard(QtWidgets.QFrame): # <- option cards in the settings section
    def __init__(self, checkbox, title, subtitle):
        super().__init__()
        self.checkbox = checkbox

        self.setObjectName("optionCard")
        self.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)

        titleLabel = QtWidgets.QLabel(title)
        titleLabel.setObjectName("optionTitle")
        titleLabel.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents)

        subtitleLabel = QtWidgets.QLabel(subtitle)
        subtitleLabel.setObjectName("optionSubtitle")
        subtitleLabel.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents)

        checkbox.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents)

        textLayout = QtWidgets.QVBoxLayout()
        textLayout.setSpacing(0)
        textLayout.addWidget(titleLabel)
        textLayout.addWidget(subtitleLabel)

        layout = QtWidgets.QHBoxLayout(self)
        layout.setContentsMargins(9, 6, 9, 6)
        layout.setSpacing(7)
        layout.addWidget(checkbox)
        layout.addLayout(textLayout)
        layout.addStretch()

    def mousePressEvent(self, event): # <- toggling check box when clicking the whole button
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.checkbox.setChecked(not self.checkbox.isChecked())

        super().mousePressEvent(event)