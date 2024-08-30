# Prodigy-Infotech-CS-Tasks
# Password Strength Checker Tool

If you find this tool useful, don't forget to give it a star! ⭐

## Overview

The Password Strength Checker Tool is a user-friendly application developed with Python's PyQt5. This tool helps users evaluate the strength of their passwords, generate random passwords, and manage password visibility. It provides visual feedback on password strength and offers functionalities like copying and clearing passwords.

## Features

- **Check Password Strength**: Evaluates the strength of the entered password and provides a score along with detailed remarks.
- **Generate Password**: Generates a random password with a default length of 12 characters.
- **Copy to Clipboard**: Copies the current password to the clipboard.
- **Show/Hide Password**: Allows toggling the visibility of the password in the input field.
- **Clear Password**: Clears the password entry field.
- **User Interface**: Clean and intuitive interface with progress bar indicating password strength and clear feedback on password composition.

## Installation

1. **Clone or Download the Repository**:
   ```bash
   git clone https://github.com/YDTech06/PRODIGY_CS_03.git
2. **Install Dependencies**: Ensure you have PyQt5 and pyperclip installed
    ```bash
    pip install PyQt5 pyperclip
3. **Run the Script**: Execute the script using Python
    ```bash
    python password_strength_checker_tool.py

## How To Use
- **Enter the Password**: Type the password you want to evaluate into the provided password field.
- **Check Password Strength**: As you type, the tool will automatically assess the password strength and display the result along with a progress bar indicating strength.
- **Generate Password**: Click the "Generate Password" button to create a random password and populate the field.
- **Show/Hide Password**: Click the "Show Password" button to toggle between showing and hiding the password.
- **Copy Password**: Click the "Copy Password" button to copy the current password to the clipboard.
- **Clear Input**: Click the "Clear" button to clear the password entry field.
- **Close the Application**: The application will prompt you to confirm if you want to quit. Click "Yes" to close or "No" to continue.

## Notes
1. Ensure that the password length is at least 8 characters for an accurate strength evaluation.
2. The strength score is based on the inclusion of lowercase letters, uppercase letters, digits, whitespace characters, and special characters.
3. This tool is intended for general password strength evaluation and password management and should be used for personal or educational purposes.
