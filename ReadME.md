# win11_setup

This script allows you to easily install, update, or uninstall a list of applications using the Windows package manager, `winget`. It provides a simple command-line interface to perform these actions.

## Requirements

Before running the script, ensure that you have the following:

- Windows operating system
- `winget` package manager installed on your system
- Python 3.x
- Git

## Usage

1. Open a terminal or command prompt.
2. Run the script using the Python interpreter: `python win11_setup.py`.
3. The script will display a banner and a list of available applications for installation, update, or uninstallation.
4. Choose an action from the menu by entering the corresponding number:
   - `1`: Install selected applications
   - `2`: Update selected applications
   - `3`: Uninstall selected applications
   - `4`: Exit the script
5. Depending on your choice, the script will execute the selected action for each application.
6. After completing the action, the script will clear the terminal and return to the main menu.

**Note:** The script pauses for 10 seconds after each action to allow you to review the output. If you wish to change this duration, you can modify the `time.sleep()` value in the script.

## List of Applications

The script includes the following list of applications:

- Google Chrome
- Mozilla Firefox
- Bitwarden
- AnyDesk
- 7-Zip
- Notepad++
- Obsidian
- KeePass
- Everything
- OBS Studio
- Brave Browser
- Greenshot
- Spotify
- Git
- Revo Uninstaller

## License

[LICENSE](LICENSE)


## Acknowledgements

This script was created by [github.com/ic3man31](https://github.com/ic3man31).

Please feel free to provide any feedback or suggestions for improvement.
