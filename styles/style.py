APP_STYLE = """
QWidget {
    background-color: #0B1118;
    color: #E7EDF6;
    font-family: "Segoe UI";
    font-size: 12px;
}

/* --- Title bar --- */
#titleBar {
    background-color: #0B1118;
    border: none;
    border-bottom: 1px solid #1B2633;
}

#windowTitle {
    background: transparent;
    color: #AAB6C5;
    font-size: 11px;
}

#minimizeButton, #closeButton {
    background: transparent;
    border: none;
    border-radius: 0px;
    color: #C8D1DC;
    font-size: 15px;
}

#minimizeButton:hover {
    background-color: #18212C;
}

#minimizeButton:pressed {
    background-color: #202C38;
}

#closeButton:hover {
    background-color: #C42B1C;
    color: #FFFFFF;
}

#closeButton:pressed {
    background-color: #A62317;
}

#contentWidget {
    background-color: #0B1118;
    border: none;
}

/* --- Header --- */

#appIcon {
    background: transparent;
    color: #DBEAFE;
    font-size: 14px;
}

#titleLabel {
    background: transparent;
    color: #F8FAFC;
    font-size: 15px;
    font-weight: 600;
}

/* --- Password --- */

#passwordCard {
    background-color: #111820;
    border: 1px solid #293544;
    border-radius: 10px;
}

#passwordOutput {
    background: transparent;
    border: none;
    color: #F8FAFC;
    font-family: "Consolas";
    font-size: 19px;
    min-height: 34px;
    padding: 0px 6px;
}

#copyButton {
    background-color: #18212C;
    border: 1px solid #293748;
    border-radius: 7px;
    color: #DCE5F1;
    font-size: 12px;
    min-width: 58px;
    min-height: 32px;
    padding: 3px 8px;
}

#copyButton:hover {
    background-color: #202C3A;
    border-color: #3B82F6;
}

#copyButton:pressed {
    background-color: #162131;
}

/* --- Strength --- */

#strengthSegment {
    background-color: #27313E;
    border: none;
    border-radius: 2px;
}

#strengthSegment[active="true"] {
    background-color: #3B82F6;
}

#strengthInfo {
    background: transparent;
}

#strengthText {
    background: transparent;
    color: #8998AB;
    font-size: 10px;
}

#strengthValue {
    background: transparent;
    color: #60A5FA;
    font-size: 10px;
    font-weight: 600;
}

/* --- Settings --- */

#settingsCard {
    background-color: #111820;
    border: 1px solid #293544;
    border-radius: 10px;
}

#lengthTitle {
    background: transparent;
    color: #E7EDF6;
    font-size: 13px;
    font-weight: 500;
}

#lengthValue {
    background: transparent;
    color: #F8FAFC;
    font-size: 13px;
    font-weight: 600;
}

#rangeLabel {
    background: transparent;
    color: #7D8BA0;
    font-size: 10px;
}

/* --- Slider --- */

QSlider {
    background: transparent;
    min-height: 16px;
}

QSlider::groove:horizontal {
    background-color: #293340;
    height: 5px;
    border-radius: 2px;
}

QSlider::sub-page:horizontal {
    background-color: #3B82F6;
    border-radius: 2px;
}

QSlider::handle:horizontal {
    background-color: #4F8DF7;
    width: 14px;
    height: 14px;
    margin: -5px 0;
    border-radius: 7px;
}

QSlider::handle:horizontal:hover {
    background-color: #6CA2FF;
}

/* --- Option cards --- */

#optionCard {
    background-color: #121A23;
    border: 1px solid #2A3747;
    border-radius: 7px;
    min-height: 45px;
}

#optionCard:hover {
    background-color: #172230;
    border-color: #3B82F6;
}

#optionTitle {
    background: transparent;
    color: #F1F5F9;
    font-size: 12px;
    font-weight: 500;
}

#optionSubtitle {
    background: transparent;
    color: #8290A3;
    font-size: 10px;
}

/* --- Minimum count --- */

#minimumTitle {
    background: transparent;
    color: #AEBBD0;
    font-size: 12px;
}

#minimumOptional {
    background: transparent;
    color: #66758A;
    font-size: 10px;
}

#minimumLabel {
    background: transparent;
    color: #E7EDF6;
    font-size: 12px;
}

#minimumSpin {
    background-color: #0C131B;
    border: 1px solid #2C394A;
    border-radius: 6px;
    color: #F8FAFC;
    font-size: 12px;
    min-width: 90px;
    min-height: 28px;
    padding: 0px 8px;
}

#minimumSpin:hover {
    border-color: #3D4D63;
}

#minimumSpin:focus {
    border-color: #3B82F6;
}

#minimumSpin:disabled {
    background-color: #10161E;
    color: #526073;
    border-color: #202A37;
}

/* --- Generate --- */

#generateButton {
    background-color: #3478ED;
    border: 1px solid #4385F4;
    border-radius: 8px;
    color: #FFFFFF;
    font-size: 14px;
    font-weight: 600;
    min-height: 40px;
}

#generateButton:hover {
    background-color: #4285F4;
}

#generateButton:pressed {
    background-color: #2867D5;
}

/* --- Toast --- */

#toastLabel {
    background-color: #166534;
    border: 1px solid #22C55E;
    border-radius: 6px;
    color: #FFFFFF;
    font-weight: 600;
    padding: 6px 12px;
}
"""