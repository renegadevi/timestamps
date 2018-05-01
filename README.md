Timestamps
=========
Quick to use cross-platform time stamp software written in Python3 and Qt.

Timestamps is a very simple and quick to use time calculator. It was an evolution of a simple CLI-script I wrote a while back and by making it into a "app" it would be more accessible to more people as well adding some new features such as localization and a way to easy calculate time difference.


Screenshots
-------------
![MacOS, Swedish](https://gitlab.com/renegadevi/timestamps/raw/master/screenshots/macos_timestamps_week.png)
![Windows, Swedish](https://gitlab.com/renegadevi/timestamps/raw/master/screenshots/windows_timestamps_month.png)
![Linux, English](https://gitlab.com/renegadevi/timestamps/raw/master/screenshots/ubuntu_timestamps_date_differerence.png)

For more screenshots, check the *screenshots* folder.

TODOs
-------------
- Software packaging
- Support for more languages

How to install
-------------

### Prerequisites
Python 3 (Tested on 3.6)
Homebrew (Brew) (On Mac)


### Ubuntu 18.04 LTS
```bash
sudo apt install python3-pip git
git clone https://gitlab.com/renegadevi/Timestamps.git
cd Timestamps
python3 -m pip install -r requirements.txt
chmod +x timestamps/main.py
./timestamps/main.py
```

### MacOS 10.13 (High Sierra)
```bash
sudo homebrew install python3 pyqt5 qt5 git
git clone https://gitlab.com/renegadevi/Timestamps.git
cd Timestamps/timestamps
chmod +x main.py
./main.py
```

### Windows (8.1 + 10)
1. Download and install Python 3 (Check "Add Python 3.6 to PATH")
https://www.python.org/downloads

2. Open command prompt as Administrator and type:
`py -m pip install PyQt5 pendulum`

3. Download Timestamps as a zip and extract the folder
4. Open Timestamps folder, navigate to main.py file and double click it to run.
5. Rename main.py to main.pyw (to remove the command prompt in the background)

***Optional: Create a shortcut***

1. Right click on the desktop, 'New -> Create shortcut'
2. navigate and select `main.pyw`
Enter "Timestamps" as name of the shortcut.

3. Right-click on the shortcut and choose 'preferences'
4. Click 'Change icon',  navigate and select the file 'timestamps/resouces/icons/icon.ico'
5. Press OK, Apply then OK.


Built with Open-source
-------------
Python 3 – https://github.com/python
PyQt5 – https://github.com/pyqt
Pendulum – https://github.com/sdispater/pendulum


Licence
-------------
**Timestamps** is licensed under the GPLv3 licence. See LICENCE for details.
