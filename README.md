# File Size Checker Application

The **File Size Checker Application** is a simple Python program that allows users to check the size of a selected file. The program provides a graphical user interface (GUI) for ease of use and displays the size of the chosen file in bytes. This documentation provides an overview of the application's functionality and how to use it.

## Prerequisites

Before using the File Size Checker Application, ensure that you have the following prerequisites:

1. **Python**: The program is written in Python. You need to have Python installed on your system. You can download Python from the official website: [Python.org](https://www.python.org/downloads/).

2. **Tkinter Library**: Tkinter is the standard GUI library for Python and is typically included with Python installations. Ensure that Tkinter is available on your system. Most Python installations come with Tkinter pre-installed.
```bash
pip install Tkinter
```

## Installation

1. Clone or download the project files from the [GitHub repository](https://github.com/Freddy155/file-checker-gui).
```bash
git clone https://github.com/Freddy155/file-checker-gui.git
```

2. Navigate to the project directory.
```bash
cd file-checker-gui
```
3. Run the `app.py` script using Python.

```bash
python app.py
```

Usage
-----

1.  When you run the application, a graphical window will appear with a button labeled "Select File."

2.  Click the "Select File" button to open a file dialog.

3.  Choose a file from your system. The program will display the selected file's size in bytes below the button.

4.  To check the size of another file, simply click the "Select File" button again and choose a different file.

5.  The program provides the file size in bytes, and it does not perform any unit conversions.

How It Works
------------

The File Size Checker Application is a Python script that utilizes the Tkinter library for the graphical user interface (GUI) and the `os` library for checking the size of a selected file. Here's how it works:

-   The application defines three functions:

    -   `get_file_size(file_path)`: This function takes a file path as input and uses the `os` library to retrieve the size of the file in bytes. If the file is not found, it returns -1.

    -   `open_file_dialog()`: This function opens a file dialog, allowing the user to select a file from their system. When a file is chosen, it calls `get_file_size()` to retrieve the file's size and then updates the GUI with the result.

    -   `update_result_label(file_path, file_size)`: This function updates the GUI label with the selected file's path and size.

-   The main part of the script creates a Tkinter GUI window with a "Select File" button and a label for displaying the file's size.

-   When the "Select File" button is clicked, it triggers the `open_file_dialog()` function.

-   The selected file's size is retrieved using `get_file_size()` and displayed on the label.

-   The GUI window runs in a main loop, allowing the user to interact with the application.

Contributing
------------

If you would like to contribute to the development of the File Size Checker Application, feel free to fork the repository, make your changes, and create a pull request. We welcome any improvements, bug fixes, or feature additions.