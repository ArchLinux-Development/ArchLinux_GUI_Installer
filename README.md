# Arch Linux GUI Installer

![Arch Linux](https://img.shields.io/badge/Arch%20Linux-1793D1?style=for-the-badge&logo=arch-linux&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-007ACC?style=for-the-badge&logo=python&logoColor=white)

## Introduction

Welcome to the Arch Linux GUI Installer! This project aims to simplify the installation process of Arch Linux by providing an easy-to-use graphical interface. Users can select their preferred desktop environment, configure system settings, and install Arch Linux with minimal hassle.

## Features

- **Desktop Environment Selection**: Choose from a variety of desktop environments including KDE Plasma, GNOME, XFCE, Cinnamon, and more.
- **Software Selection**: Customize the software to be installed based on the selected desktop environment.
- **Filesystem Configuration**: Support for multiple filesystems such as BTRFS, ZFS, EXT4, and more.
- **Hardware Detection**: Automatically detect and display system hardware information.
- **User Account Setup**: Create user accounts with options for administrative privileges and password strength verification.
- **Bootloader Configuration**: Select and configure your preferred bootloader.
- **Swap File Configuration**: Automatically suggest swap file size based on system memory with options for ZRAM.

## Screenshots

![Screenshot1](https://via.placeholder.com/800x400.png?text=Arch+Linux+GUI+Installer+Screenshot+1)
![Screenshot2](https://via.placeholder.com/800x400.png?text=Arch+Linux+GUI+Installer+Screenshot+2)

## Installation

### Prerequisites

- Python 3.x
- `psutil` library
- `archinstall` library

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/ArchLinux-Development/ArchLinux_GUI_Installer.git
    cd ArchLinux_GUI_Installer
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:

    ```bash
    python main.py
    ```

## Usage

1. Start the application by running `python main.py`.
2. Follow the on-screen instructions to configure your Arch Linux installation.
3. Select your preferred desktop environment, filesystem, and other settings.
4. Create user accounts and configure the bootloader.
5. Complete the installation process.

## Contributing

We welcome contributions! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or suggestions, please contact [Eliminater74](mailto:eliminater74@gmail.com).

---

*Thank you for using the Arch Linux GUI Installer! We hope this tool makes your Arch Linux installation process smooth and enjoyable.*

![Arch Linux Logo](https://upload.wikimedia.org/wikipedia/commons/a/a5/Archlinux-icon-crystal-64.svg)
