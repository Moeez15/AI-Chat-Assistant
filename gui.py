from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QLineEdit, QPushButton
from ai_assistant import stream_ai_response
from PyQt5.QtCore import QTimer

class ChatBotGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AI Chat Assistant 🤖")
        self.setGeometry(100, 100, 400, 500)

        self.layout = QVBoxLayout()

        self.chat_area = QTextEdit()
        self.chat_area.setReadOnly(True)
        self.layout.addWidget(self.chat_area)

        self.input_field = QLineEdit()
        self.layout.addWidget(self.input_field)

        self.button_layout = QHBoxLayout()

        # Send button
        self.send_button = QPushButton("Send")
        self.send_button.setStyleSheet("background-color: #4CAF50; color: white; font-weight: bold;")
        self.send_button.clicked.connect(self.handle_send)
        self.button_layout.addWidget(self.send_button)
        
        # Clear Chat button
        self.clear_button = QPushButton("Clear Chat")
        self.clear_button.setStyleSheet("background-color: #f44336; color: white; font-weight: bold;")
        self.clear_button.clicked.connect(self.clear_chat)
        self.button_layout.addWidget(self.clear_button)

        self.layout.addLayout(self.button_layout)

        self.setLayout(self.layout)

        self.response_generator = None
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_response)

    def clear_chat(self):
        self.chat_area.clear()

    def handle_send(self):
        user_text = self.input_field.text()
        if user_text:
            self.chat_area.append(f"You: {user_text}")

            self.response_generator = stream_ai_response(user_text)
            self.chat_area.append("AI: ")  # Start AI message
            self.input_field.clear()
            self.timer.start(50)  # Speed of typing (50ms)

    def update_response(self):
        try:
            chunk = next(self.response_generator)
            self.chat_area.insertPlainText(chunk)  # Append live!
            self.chat_area.moveCursor(self.chat_area.textCursor().End)  # Keep scroll at bottom
        except StopIteration:
            self.timer.stop()

if __name__ == "__main__":
    app = QApplication([])
    window = ChatBotGUI()
    window.show()
    app.exec()
