from PyQt6 import QtCore, QtWidgets

from config import MAX_LENGTH
from generator import generatePassword
from styles.style import APP_STYLE
from ui import createWidgets, createLayouts
from anims.animations import animatePassword, animateStrength, showToast


class Application(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # --- Window ---
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setMinimumSize(460, 560)

        self.generatedPassword = ""
        self.currentStrengthScore = 0
        self.strengthTimers = []

        createWidgets(self)
        createLayouts(self)
        self.createConnections()
        self.setStyleSheet(APP_STYLE)

        self.generate() # gen when init

    def createConnections(self):
        self.generateButton.clicked.connect(self.generate)
        self.copyButton.clicked.connect(self.copyPassword)

        self.lengthSlider.valueChanged.connect(self.updateLength)
        self.lengthSlider.valueChanged.connect(self.updateStrength)

        self.upperCheck.toggled.connect(self.updateStrength)
        self.lowerCheck.toggled.connect(self.updateStrength)
        self.numberCheck.toggled.connect(self.updateStrength)
        self.symbolCheck.toggled.connect(self.updateStrength)

        self.numberCheck.toggled.connect(self.updateMinimums)
        self.symbolCheck.toggled.connect(self.updateMinimums)

    def generate(self):
        self.generatedPassword = generatePassword(
            self.lengthSlider.value(),
            self.upperCheck.isChecked(),
            self.lowerCheck.isChecked(),
            self.numberCheck.isChecked(),
            self.symbolCheck.isChecked(),
            self.minNumbersSpin.value() if self.numberCheck.isChecked() else 0,
            self.minSymbolsSpin.value() if self.symbolCheck.isChecked() else 0
        )

        self.passwordOutput.setText(self.generatedPassword)
        animatePassword(self)
        self.updateStrength()

    def copyPassword(self):
        password = self.passwordOutput.text()

        if not password:
            return

        QtWidgets.QApplication.clipboard().setText(password)
        showToast(self, "Password Copied")

    # --- settings ---
    def updateLength(self, value):
        self.lengthValue.setText(str(value))
        self.minNumbersSpin.setMaximum(value)
        self.minSymbolsSpin.setMaximum(value)

    def updateMinimums(self):
        numbersEnabled = self.numberCheck.isChecked()
        symbolsEnabled = self.symbolCheck.isChecked()

        self.minNumbersSpin.setEnabled(numbersEnabled)
        self.minSymbolsSpin.setEnabled(symbolsEnabled)

        if not numbersEnabled:
            self.minNumbersSpin.setValue(0)
        elif self.minNumbersSpin.value() == 0:
            self.minNumbersSpin.setValue(1)

        if not symbolsEnabled:
            self.minSymbolsSpin.setValue(0)
        elif self.minSymbolsSpin.value() == 0:
            self.minSymbolsSpin.setValue(1)

    # --- anims for strength info ---
    def updateStrength(self):
        length = self.lengthSlider.value()

        characterTypes = sum([
            self.upperCheck.isChecked(),
            self.lowerCheck.isChecked(),
            self.numberCheck.isChecked(),
            self.symbolCheck.isChecked()
        ])

        score = 0

        if length >= 8:
            score += 1
        if length >= 12:
            score += 1
        if length >= 16:
            score += 1
        if characterTypes >= 3:
            score += 1
        if characterTypes == 4 and length >= 20:
            score += 1

        score = min(score, 5)
        strengths = ["Weak", "Weak", "Fair", "Good", "Strong", "Very Strong"]
        strength = strengths[score]

        if score == self.currentStrengthScore:
            self.strengthValue.setText(strength)
            return

        oldScore = self.currentStrengthScore
        self.currentStrengthScore = score
        self.strengthValue.setText(strength)

        animateStrength(self, oldScore, score)

    # --- window only ---
    def resizeEvent(self, event):
        super().resizeEvent(event)
        print("Width:", self.width(), "Height:", self.height())