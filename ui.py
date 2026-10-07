from PyQt6 import QtCore, QtWidgets

from config import MIN_LENGTH, MAX_LENGTH, DEFAULT_LENGTH
from widgets.widgets import BlueCheckBox, OptionCard
from widgets.titlebar import TitleBar



def createWidgets(app):

    # --- title bar ---
    app.titleBar = TitleBar(app)


    app.iconLabel = QtWidgets.QLabel("bonjerp")
    app.iconLabel.setObjectName("appIcon")

    app.titleLabel = QtWidgets.QLabel("Password Generator")
    app.titleLabel.setObjectName("titleLabel")

    app.passwordOutput = QtWidgets.QLineEdit()
    app.passwordOutput.setReadOnly(True)
    app.passwordOutput.setObjectName("passwordOutput")

    app.passwordEffect = QtWidgets.QGraphicsOpacityEffect(app.passwordOutput)
    app.passwordOutput.setGraphicsEffect(app.passwordEffect)
    app.passwordEffect.setOpacity(1.0)


    app.copyButton = QtWidgets.QPushButton("Copy")
    app.copyButton.setObjectName("copyButton")
    app.copyButton.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)

    # --- strength ---
    app.strengthSegments = []

    for i in range(5):
        segment = QtWidgets.QFrame()
        segment.setObjectName("strengthSegment")
        segment.setProperty("active", False)
        segment.setFixedHeight(5)
        app.strengthSegments.append(segment)

    app.strengthText = QtWidgets.QLabel("Strength:")
    app.strengthText.setObjectName("strengthText")

    app.strengthValue = QtWidgets.QLabel("Weak")
    app.strengthValue.setObjectName("strengthValue")

    app.strengthEffect = QtWidgets.QGraphicsOpacityEffect(app.strengthValue)
    app.strengthValue.setGraphicsEffect(app.strengthEffect)
    app.strengthEffect.setOpacity(1.0)

    app.lengthTitle = QtWidgets.QLabel("Length:")
    app.lengthTitle.setObjectName("lengthTitle")

    app.lengthValue = QtWidgets.QLabel(str(DEFAULT_LENGTH))
    app.lengthValue.setObjectName("lengthValue")

    app.lengthSlider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
    app.lengthSlider.setRange(MIN_LENGTH, MAX_LENGTH)
    app.lengthSlider.setValue(DEFAULT_LENGTH)

    app.minLengthLabel = QtWidgets.QLabel(str(MIN_LENGTH))
    app.minLengthLabel.setObjectName("rangeLabel")

    app.maxLengthLabel = QtWidgets.QLabel(str(MAX_LENGTH))
    app.maxLengthLabel.setObjectName("rangeLabel")

    app.upperCheck = BlueCheckBox()
    app.lowerCheck = BlueCheckBox()
    app.numberCheck = BlueCheckBox()
    app.symbolCheck = BlueCheckBox()

    app.upperCheck.setChecked(True)
    app.lowerCheck.setChecked(True)
    app.numberCheck.setChecked(True)
    app.symbolCheck.setChecked(True)

    app.upperCard = OptionCard(app.upperCheck, "Uppercase", "A-Z")
    app.lowerCard = OptionCard(app.lowerCheck, "Lowercase", "a-z")
    app.numberCard = OptionCard(app.numberCheck, "Numbers", "0-9")
    app.symbolCard = OptionCard(app.symbolCheck, "Symbols", "!@#$%...")

    # --- mini count ---
    app.minimumTitle = QtWidgets.QLabel("Minimum count")
    app.minimumTitle.setObjectName("minimumTitle")

    app.minimumOptional = QtWidgets.QLabel("(optional)")
    app.minimumOptional.setObjectName("minimumOptional")

    app.minimumNumbersLabel = QtWidgets.QLabel("Minimum numbers")
    app.minimumNumbersLabel.setObjectName("minimumLabel")

    app.minimumSymbolsLabel = QtWidgets.QLabel("Minimum symbols")
    app.minimumSymbolsLabel.setObjectName("minimumLabel")

    app.minNumbersSpin = QtWidgets.QSpinBox()
    app.minNumbersSpin.setRange(0, MAX_LENGTH)
    app.minNumbersSpin.setValue(1)
    app.minNumbersSpin.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
    app.minNumbersSpin.setObjectName("minimumSpin")

    app.minSymbolsSpin = QtWidgets.QSpinBox()
    app.minSymbolsSpin.setRange(0, MAX_LENGTH)
    app.minSymbolsSpin.setValue(1)
    app.minSymbolsSpin.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
    app.minSymbolsSpin.setObjectName("minimumSpin")

    # --- generate ---
    app.generateButton = QtWidgets.QPushButton("↻  Generate Password")
    app.generateButton.setObjectName("generateButton")
    app.generateButton.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)

    # --- toast ---
    app.toastLabel = QtWidgets.QLabel("Password Copied", app)
    app.toastLabel.setObjectName("toastLabel")
    app.toastLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    app.toastLabel.hide()


def createLayouts(app):
    mainLayout = QtWidgets.QVBoxLayout(app)
    mainLayout.setContentsMargins(0, 0, 0, 0)
    mainLayout.setSpacing(0)
    mainLayout.addWidget(app.titleBar)

    contentWidget = QtWidgets.QWidget()
    contentWidget.setObjectName("contentWidget")

    contentLayout = QtWidgets.QVBoxLayout(contentWidget)
    contentLayout.setContentsMargins(10, 10, 10, 10)
    contentLayout.setSpacing(10)


    headerLayout = QtWidgets.QHBoxLayout()
    headerLayout.setSpacing(8)
    headerLayout.addWidget(app.iconLabel)
    headerLayout.addWidget(app.titleLabel)
    headerLayout.addStretch()
    contentLayout.addLayout(headerLayout)

    # ---passcard ---
    passwordCard = QtWidgets.QFrame()
    passwordCard.setObjectName("passwordCard")

    passwordLayout = QtWidgets.QVBoxLayout(passwordCard)
    passwordLayout.setContentsMargins(14, 12, 14, 12)
    passwordLayout.setSpacing(9)

    passwordTop = QtWidgets.QHBoxLayout()
    passwordTop.setSpacing(8)
    passwordTop.addWidget(app.passwordOutput, 1)
    passwordTop.addWidget(app.copyButton)
    passwordLayout.addLayout(passwordTop)


    strengthLayout = QtWidgets.QHBoxLayout()
    strengthLayout.setSpacing(5)

    for segment in app.strengthSegments:
        strengthLayout.addWidget(segment, 1)

    strengthLayout.addSpacing(5)


    strengthInfo = QtWidgets.QWidget()
    strengthInfo.setObjectName("strengthInfo")
    strengthInfo.setFixedWidth(105)

    strengthInfoLayout = QtWidgets.QHBoxLayout(strengthInfo)
    strengthInfoLayout.setContentsMargins(0, 0, 0, 0)
    strengthInfoLayout.setSpacing(4)
    strengthInfoLayout.addWidget(app.strengthText)
    strengthInfoLayout.addWidget(app.strengthValue)
    strengthInfoLayout.addStretch()

    strengthLayout.addWidget(strengthInfo)
    passwordLayout.addLayout(strengthLayout)
    contentLayout.addWidget(passwordCard)


    settingsCard = QtWidgets.QFrame()
    settingsCard.setObjectName("settingsCard")

    settingsLayout = QtWidgets.QVBoxLayout(settingsCard)
    settingsLayout.setContentsMargins(14, 12, 14, 12)
    settingsLayout.setSpacing(9)


    lengthHeader = QtWidgets.QHBoxLayout()
    lengthHeader.setSpacing(6)
    lengthHeader.addWidget(app.lengthTitle)
    lengthHeader.addWidget(app.lengthValue)
    lengthHeader.addStretch()

    settingsLayout.addLayout(lengthHeader)
    settingsLayout.addWidget(app.lengthSlider)

    rangeLayout = QtWidgets.QHBoxLayout()
    rangeLayout.addWidget(app.minLengthLabel)
    rangeLayout.addStretch()
    rangeLayout.addWidget(app.maxLengthLabel)
    settingsLayout.addLayout(rangeLayout)


    optionLayout = QtWidgets.QGridLayout()
    optionLayout.setHorizontalSpacing(8)
    optionLayout.setVerticalSpacing(8)
    optionLayout.addWidget(app.upperCard, 0, 0)
    optionLayout.addWidget(app.lowerCard, 0, 1)
    optionLayout.addWidget(app.numberCard, 1, 0)
    optionLayout.addWidget(app.symbolCard, 1, 1)
    settingsLayout.addLayout(optionLayout)


    minimumHeader = QtWidgets.QHBoxLayout()
    minimumHeader.setSpacing(5)
    minimumHeader.addWidget(app.minimumTitle)
    minimumHeader.addWidget(app.minimumOptional)
    minimumHeader.addStretch()
    settingsLayout.addLayout(minimumHeader)

    numberMinimum = QtWidgets.QHBoxLayout()
    numberMinimum.addWidget(app.minimumNumbersLabel)
    numberMinimum.addStretch()
    numberMinimum.addWidget(app.minNumbersSpin)
    settingsLayout.addLayout(numberMinimum)

    symbolMinimum = QtWidgets.QHBoxLayout()
    symbolMinimum.addWidget(app.minimumSymbolsLabel)
    symbolMinimum.addStretch()
    symbolMinimum.addWidget(app.minSymbolsSpin)
    settingsLayout.addLayout(symbolMinimum)

    contentLayout.addWidget(settingsCard)

    # generate
    contentLayout.addWidget(app.generateButton)
    mainLayout.addWidget(contentWidget)