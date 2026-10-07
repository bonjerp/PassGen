from PyQt6 import QtCore


def animatePassword(app):
    if hasattr(app, "passwordAnimation"):
        app.passwordAnimation.stop()

    app.passwordAnimation = QtCore.QPropertyAnimation(app.passwordEffect, b"opacity")
    app.passwordAnimation.setDuration(200)
    app.passwordAnimation.setStartValue(0.25)
    app.passwordAnimation.setEndValue(1.0)
    app.passwordAnimation.setEasingCurve(QtCore.QEasingCurve.Type.OutCubic)
    app.passwordAnimation.start()

def animateStrength(app, oldScore, newScore):
    for timer in app.strengthTimers:
        timer.stop()

    app.strengthTimers.clear()

    # --- increase ---
    if newScore > oldScore:
        for delay, index in enumerate(range(oldScore, newScore)):
            timer = QtCore.QTimer(app)
            timer.setSingleShot(True)
            timer.timeout.connect(lambda i=index: setStrengthSegment(app, i, True))
            timer.start(delay * 55)
            app.strengthTimers.append(timer)

    # --- decrease ---
    else:
        for delay, index in enumerate(range(oldScore - 1, newScore - 1, -1)):
            timer = QtCore.QTimer(app)
            timer.setSingleShot(True)
            timer.timeout.connect(lambda i=index: setStrengthSegment(app, i, False))
            timer.start(delay * 55)
            app.strengthTimers.append(timer)

    # --- text fade ---
    if hasattr(app, "strengthTextAnimation"):
        app.strengthTextAnimation.stop()

    app.strengthTextAnimation = QtCore.QPropertyAnimation(app.strengthEffect, b"opacity")
    app.strengthTextAnimation.setDuration(180)
    app.strengthTextAnimation.setStartValue(0.25)
    app.strengthTextAnimation.setEndValue(1.0)
    app.strengthTextAnimation.setEasingCurve(QtCore.QEasingCurve.Type.OutCubic)
    app.strengthTextAnimation.start()


def setStrengthSegment(app, index, active):
    segment = app.strengthSegments[index]
    segment.setProperty("active", active)
    segment.style().unpolish(segment)
    segment.style().polish(segment)



def showToast(app, message): # <- copy notif/toast
    app.toastLabel.setText(message)
    app.toastLabel.adjustSize()

    x = (app.width() - app.toastLabel.width()) // 2
    startPosition = QtCore.QPoint(x, -app.toastLabel.height())
    endPosition = QtCore.QPoint(x, 38)

    if hasattr(app, "toastDownAnimation"):
        app.toastDownAnimation.stop()

    if hasattr(app, "toastUpAnimation"):
        app.toastUpAnimation.stop()

    if hasattr(app, "toastTimer"):
        app.toastTimer.stop()

    app.toastLabel.move(startPosition)
    app.toastLabel.show()
    app.toastLabel.raise_()

    # --- slide down ---
    app.toastDownAnimation = QtCore.QPropertyAnimation(app.toastLabel, b"pos")
    app.toastDownAnimation.setDuration(250)
    app.toastDownAnimation.setStartValue(startPosition)
    app.toastDownAnimation.setEndValue(endPosition)
    app.toastDownAnimation.setEasingCurve(QtCore.QEasingCurve.Type.OutCubic)
    app.toastDownAnimation.start()

    app.toastTimer = QtCore.QTimer(app)
    app.toastTimer.setSingleShot(True)
    app.toastTimer.timeout.connect(lambda: hideToast(app))
    app.toastTimer.start(1200)


def hideToast(app):
    x = (app.width() - app.toastLabel.width()) // 2
    startPosition = app.toastLabel.pos()
    endPosition = QtCore.QPoint(x, -app.toastLabel.height())

    # --- slide up ---
    app.toastUpAnimation = QtCore.QPropertyAnimation(app.toastLabel, b"pos")
    app.toastUpAnimation.setDuration(250)
    app.toastUpAnimation.setStartValue(startPosition)
    app.toastUpAnimation.setEndValue(endPosition)
    app.toastUpAnimation.setEasingCurve(QtCore.QEasingCurve.Type.InCubic)
    app.toastUpAnimation.finished.connect(app.toastLabel.hide)
    app.toastUpAnimation.start()