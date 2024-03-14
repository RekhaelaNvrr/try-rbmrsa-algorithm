Setting up the environment

Must have:
  - Python
  - Git
  - VS Code
  - GitHub Desktop
    
<br> </br>
Install Python
  - Download the `Python` installer from the official Python website: `https://www.python.org/downloads/`
  - `Run` the installer and follow the on-screen instructions to complete the installation.
  - Verify that Python is installed correctly by opening a command prompt or terminal and typing `python --version`.

<br> </br>
Install Git
  - Download the `Git` installer for your operating system from the official Git website: `https://git-scm.com/downloads`.
  - `Run` the installer and follow the on-screen instructions to complete the installation.

<br> </br>
Install Visual Studio Code
  - Download the `VSCode` installer from the official Microsoft website: `https://code.visualstudio.com/download`.
  - `Run` the installer and follow the on-screen instructions to complete the installation.
  - IMPORTANT: `Register Code as an editor for supported file types`and `Add to PATH (requires shell restart)` must both be CHECKED.
  - Launch VS Code app, go to `Extensions` (ctrl + shift + x), search and install `Python` with a Microsoft checkmark.
  - To check if python has been successfully installed: go to terminal and run `py --verson`.

<br> </br>
Install GitHub Desktop
  - Download the `GitHub Desktop` installer for your operating system from `https://desktop.github.com/`.
  - `Run` the installer and follow the on-screen instructions.
  - `Launch` GitHub Desktop and `configure` it (`sign in`).
  - You can now use the extension to connect to your GitHub repositories, clone projects, and manage your code.

<br> </br>
Clone the project via:
- git clone from GitHub Desktop

<br> </br>
Create a Python Project
  - Open VSCode and create a new folder for your Python project.
  - Open the Command Palette (Ctrl+Shift+P on Windows/Linux, Cmd+Shift+P on macOS) and type "Python: Create Environment".
  - Select the "Create Environment" option and choose the desired Python interpreter (Global is the most suitable one). 
  - This will create a virtual environment for your Python project, isolating it from other projects and ensuring compatibility with the installed Python version.

<br> </br>
How to Install rsa on Windows? (IMPORTANT-- !!)
- Type `cmd` in the search bar and hit Enter to open the command line.
- Type `pip install rsa` in the command line and hit Enter again. This installs rsa for your default Python installation.
- The previous command may not work if you have both Python versions 2 and 3 on your computer. In this case, try `pip3 install rsa` or `python -m pip install rsa`.
- Wait for the installation to terminate successfully. It is now installed on your Windows machine.

<br></br>
Install Crypto (always remember this, wag maging katulad ni Rekha)
- Open terminal
- Type "pip install pycryptodome"
- Wait for it to download.
- Run rbmrsa-reptil.

Install Streamlit: pip install streamlit

Install Option Menu: pip install streamlit-option-menu

Run Streamlit file: streamlit run streamlit-webapp.py