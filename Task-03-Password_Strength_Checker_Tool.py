# IMPORTS
import sys
import string
import secrets
import pyperclip
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QTextEdit,
    QProgressBar, QVBoxLayout, QHBoxLayout, QWidget, QMessageBox
)
from PyQt5.QtCore import Qt

# CLASS DEFINITION AND INITIALIZATION
# PASSWORD STRENGTH CHECKER APP CLASS
class PasswordStrengthChecker(QMainWindow):
    # INITIALIZATION
    def __init__(self):
        
        # Initializes the main window and its widgets.
        super().__init__()
        self.initUI()

    # UI INITIALIZATION
    # USER INTERFACE SETUP
    def initUI(self):

        # Set up the user interface components
        self.setWindowTitle("Password Strength Checker Tool")
        self.setGeometry(100, 100, 500, 300)

        # Central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()

        # Input layout for password entry
        self.password_entry = QLineEdit(self)
        self.password_entry.setEchoMode(QLineEdit.Password)
        self.password_entry.setPlaceholderText("Enter the Password...")
        self.password_entry.textChanged.connect(self.check_password)

        input_layout = QHBoxLayout()
        input_layout.addWidget(QLabel("Password:", self))
        input_layout.addWidget(self.password_entry)

        # Buttons layout
        button_style = "background-color: green; color: white; font-weight: bold;"
        button_layout = QHBoxLayout()

        # Show Password Button
        self.show_password_button = QPushButton("Show Password", self)
        self.show_password_button.setStyleSheet(button_style)
        self.show_password_button.setCheckable(True)
        self.show_password_button.toggled.connect(self.toggle_password_visibility)
        button_layout.addWidget(self.show_password_button)

        # Generate Password Button
        self.generate_button = QPushButton("Generate Password", self)
        self.generate_button.setStyleSheet(button_style)
        self.generate_button.clicked.connect(self.generate_password)
        button_layout.addWidget(self.generate_button)

        # Copy Password Button
        self.copy_button = QPushButton("Copy Password", self)
        self.copy_button.setStyleSheet(button_style)
        self.copy_button.clicked.connect(self.copy_password)
        button_layout.addWidget(self.copy_button)

        # Clear Password Button
        self.clear_button = QPushButton("Clear", self)
        self.clear_button.setStyleSheet(button_style)
        self.clear_button.clicked.connect(self.clear_input)
        button_layout.addWidget(self.clear_button)

        # Output text area for results
        self.output_text = QTextEdit(self)
        self.output_text.setReadOnly(True)

        # Password strength meter (progress bar)
        self.strength_meter = QWidget(self)
        self.progress_bar = QProgressBar(self.strength_meter)
        self.label = QLabel(self.strength_meter)
        self.label.setAlignment(Qt.AlignCenter)

        # Layout for the progress bar and label
        meter_layout = QVBoxLayout()
        meter_layout.addWidget(self.progress_bar)
        meter_layout.addWidget(self.label)
        meter_layout.setAlignment(Qt.AlignCenter)
        self.strength_meter.setLayout(meter_layout)
        self.strength_meter.setMinimumSize(200, 30)  # Set size for the progress bar

        # Set progress bar range
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setTextVisible(False)  # Hide text display on the progress bar

        # Add widgets to the main layout
        layout.addLayout(input_layout)
        layout.addLayout(button_layout)
        layout.addWidget(self.output_text)
        layout.addWidget(self.strength_meter)

        central_widget.setLayout(layout)

    # PASSWORD CHECKING 
    def check_password(self):
        
        # Check the password strength and update the UI elements accordingly.
        password = self.password_entry.text()
        result, strength = self.check_password_strength(password)
        self.output_text.setHtml(result)  # Display results with HTML formatting

        # Update progress bar based on strength
        color = {
            0: "gray",
            1: "red",
            2: "red",
            3: "orange",
            4: "orange",
            5: "green"
        }.get(strength, "gray")

        self.progress_bar.setStyleSheet(f"QProgressBar::chunk {{ background: {color}; }}")
        self.progress_bar.setValue(strength * 20)
        self.label.setText(f"{strength * 20}%")

    # STRENGTH CALCULATION
    def check_password_strength(self, password):
        
        # Evaluate the strength of the given password and return a result string and strength score.
        strength = 0
        remarks = ''
        lower_count = upper_count = num_count = wspace_count = special_count = 0

        # Check minimum length
        if len(password) < 8:
            return "Password is too short. It should be at least 8 characters long.", 0

        # Count character types
        for char in password:
            if char in string.ascii_lowercase:
                lower_count += 1
            elif char in string.ascii_uppercase:
                upper_count += 1
            elif char in string.digits:
                num_count += 1
            elif char == ' ':
                wspace_count += 1
            else:
                special_count += 1

        # Calculate strength score based on character types
        if lower_count >= 1:
            strength += 1
        if upper_count >= 1:
            strength += 1
        if num_count >= 1:
            strength += 1
        if wspace_count >= 1:
            strength += 1
        if special_count >= 1:
            strength += 1

        # Determine remarks based on strength
        remarks = [
            "That's a very bad password.<br>Change it as soon as possible.",
            "That's a weak password.<br>You should consider using a tougher password.",
            "Your password is okay, but it can be improved.",
            "Your password is hard to guess.<br>But you could make it even more secure.",
            "Now that's one hell of a strong password!!!<br>Hackers don't have a chance guessing that password!"
        ][strength - 1]

        result = (
            f'<b>Your Password has:</b>'
            f'<ul>'
            f'<li>{lower_count} lowercase letters</li>'
            f'<li>{upper_count} uppercase letters</li>'
            f'<li>{num_count} digits</li>'
            f'<li>{wspace_count} whitespaces</li>'
            f'<li>{special_count} special characters</li>'
            f'</ul>'
            f'<b>Password Score:</b> <b>{strength}/5</b><br><br>'
            f'<b>Remarks:</b> {remarks}'
        )
        return result, strength

    # PASSWORD MANAGEMENT FUNCTIONS
    # GENERATE PASSWORD
    def generate_password(self):
        
        # Generate a random password and set it in the password entry field.
        length = 12
        password = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
        self.password_entry.setText(password)

    # COPY PASSWORD
    def copy_password(self):
        
        # Copy the current password to the clipboard and show a confirmation message.
        password = self.password_entry.text()
        if password:
            pyperclip.copy(password)
            QMessageBox.information(self, "Password Copied", "Password copied to clipboard!")
        else:
            QMessageBox.warning(self, "No Password", "No password to copy!")

    # CLEAR PASSWORD INPUT
    def clear_input(self):
        
        # Clear the password entry field.
        self.password_entry.clear()

    # PASSWORD VISIBILITY TOGGLE
    def toggle_password_visibility(self, checked):
        
        # Toggle the visibility of the password in the entry field.
        if checked:
            self.password_entry.setEchoMode(QLineEdit.Normal)
            self.show_password_button.setText("Hide Password")
        else:
            self.password_entry.setEchoMode(QLineEdit.Password)
            self.show_password_button.setText("Show Password")

    # APPLICATION EXIT 
    # CLOSE EVENT HANDLING
    def closeEvent(self, event):
        
        # Handle the window close event and ask for confirmation.
        reply = QMessageBox.question(self, 'Quit', "Do you want to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

# MAIN EXECUTION
# MAIN BLOCK
if __name__ == '__main__':
    # Create the application and main window, then start the event loop
    app = QApplication(sys.argv)
    window = PasswordStrengthChecker()
    window.show()
    sys.exit(app.exec_())
