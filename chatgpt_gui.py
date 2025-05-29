import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QCheckBox,
    QPushButton, QTextEdit, QLabel, QScrollArea, QGroupBox
)
from PyQt6.QtCore import Qt

class ModalityApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modality Quality Control Viewer")
        self.setGeometry(100, 100, 800, 600)
        self.init_ui()

    def init_ui(self):
        main_layout = QHBoxLayout()

        # Left Panel - Modality Panel
        modality_panel = QGroupBox("Modality Panel")
        modality_layout = QVBoxLayout()

        self.checkboxes = {}
        modalities = ["EEG", "Eye Tracking", "ECG", "EDA", "RSP", "Graphomotor", "Audio", "Video"]
        for modality in modalities:
            checkbox = QCheckBox(modality)
            checkbox.stateChanged.connect(self.display_qc_output)
            self.checkboxes[modality] = checkbox
            modality_layout.addWidget(checkbox)

        self.go_button = QPushButton("Go")
        self.go_button.clicked.connect(self.display_qc_output)
        modality_layout.addWidget(self.go_button)
        modality_panel.setLayout(modality_layout)

        # Right Panel - Scrollable Output
        self.output_area = QTextEdit()
        self.output_area.setReadOnly(True)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.output_area)

        # Combine both panels
        main_layout.addWidget(modality_panel, 1)
        main_layout.addWidget(scroll_area, 3)
        self.setLayout(main_layout)

    def display_qc_output(self):
        output_text = "Quality Control Measures for selected modalities:\n"
        for modality, checkbox in self.checkboxes.items():
            if checkbox.isChecked():
                output_text += f"- {modality}: QC metrics and plots placeholder...\n"
        self.output_area.setText(output_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModalityApp()
    window.show()
    sys.exit(app.exec())