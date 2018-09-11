# Home-Automation Project 

Home Automation for the Raspberry Pi.  

#### Install Qt

This project uses Qt for development.. You can download Qt Creator from [here](https://www.qt.io/download-qt-installer) for free.

Our development is currently targeting Qt 5.10.1. When the Qt installer asks which Qt components to install, select the following components and a compiler suitable to your development environment:

- Qt 5.10.1 -> Qt Charts (Required)
- Qt 5.10.1 -> MinGW 5.3.0 32 bit  (Windows compiler)
- Tools -> MinGW 5.3.0 (Windows compiler)
- Qt 5.10.1 -> macOS (Mac components)
- Qt 5.10.1 -> iOS (iOS components)
- Qt 5.10.1 -> Android ARMv7 (Android physical device components)
- Qt 5.10.1 -> Android x86 (Android virtual device components)

After installing Qt, clone this repository and open HomeAutomation.pro using Qt Creator.

You can find instructions for cross-compiling to a Raspberry Pi [here](http://wiki.qt.io/Raspberry_Pi_Beginners_Guide)


