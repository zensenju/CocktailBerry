# Installation

Here you can find all the requirements and installation steps. 

## Prerequisites

These are the minimal tools needed to get started:

- [Python 3.7](https://www.python.org/) or newer
- [Git](https://git-scm.com/)
- recommended: **latest** [Rasperry Pi OS](https://www.raspberrypi.com/software/) (Desktop, Bullseye)

The dektop version of Raspberry Pi OS is recommended, but if you just want to have a peak into the project, any OS having Python and Git will work just fine. The RPi is needed to control the Pumps in a real machine, but the program will work fine even without any physical machine.

## Set Up

After flashing the OS, you can use the provided shell scripts to set everything automatically up on your Raspberry Pi, or just install [the requirements](#installing-requirements), when you want to have a look into the program on your pc. You can always install the other things later, the docs provide information within each according section. To clone and setup this project run:

```bash
cd ~
git clone https://github.com/AndreWohnsland/CocktailBerry.git
cd ~/CocktailBerry
# Setup for the RPi
# Docker is optional but needed for some cool extra features
sh scripts/install_docker.sh
# This will set up everything important on your RPi
cd ~/CocktailBerry
sh scripts/setup.sh
# now we are good to go
python3 runme.py
```

## Installing Requirements
The best way is to use the provided `requirements.txt` file. If Python is installed, just run: 

```bash
pip install -r requirements.txt
``` 

to get all requirements. Optionally, you can install the single needed dependenicies:

- PyQt5, requests, pyyaml, GitPython, typer, pyfiglet

## Install PyQt5 on RaspberryPi

The PyQt5 installation of pip will probably fail on your RaspberryPi. To install PyQt5 on your Pi run:

```
sudo apt-get update
sudo apt-get install qt5-default pyqt5-dev pyqt5-dev-tools
```

More information can be found at [riverbank](https://riverbankcomputing.com/software/pyqt/intro).

## Development on Non-Pi Hardware

When you are working on another hardware (for example on a Windows or macOS engine) it is recommended (but not necessary) to set `UI_DEVENVIRONMENT` to `true`. This will enable your cursor, for example. All configuration can be customized under `custom_config.yaml`:

```yaml
UI_DEVENVIRONMENT: true
```

It's worth mentioning that I optimized the UI for a touch display with a 800x480 or a 1024x800 resolution ([this is my display](https://www.amazon.de/gp/product/B071XT9Z7H/ref=ppx_yo_dt_b_asin_title_o05_s00?ie=UTF8&psc=1)). By default, the full screen is also limited to 800x480. So usually you won't have any problems with the usual HD or uHD screens. But some screens (like my little 13' Laptop screen) don't show the proper fonts/UI placements. You can change the application size with the according config settings, if you want to use a different screen size. See [Setting up the Machine / Modifying other Values](setup.md#setting-up-the-machine-modifying-other-values) for more information.