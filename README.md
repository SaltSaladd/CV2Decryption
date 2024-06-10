## CV2Decryption
A tool that automates the decryption of the fall guys file content_v2.

## How to get it working (Windows only, for now.)
1) Put the python script in \Downloads\. Edit the python script, with Visual Studio Code. Install it if you haven't already.
2) At the top of the script, there's a thingy (i forgot the name) it says "your_windows_username". Replace that with your actual windows username.
3) Save the script.
4) Run the script.
5) 3 files will appear. a .json, a .gdata and a .gz. Ignore the .gz, it's useless. I don't know why i even implemented it.
6) Edit the .json however you'd like.
7) Once you have made your changes, re-launch the python script.
8) In a new file explorer window, go to C:\Users\{user_name}\AppData\LocalLow\Mediatonic\FallGuys_client
9) In your downloads folder, copy the .gdata to the FallGuys_client folder.
10) Launch the game and your changes will be there!

## Licensing
This project is licensed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html). 

If you use **ANY** code from the source:
- You must disclose the source code of your modified work and the source code you took from this project. This means you are not allowed to use code from this project (even partially) in a closed-source and/or obfuscated application.
- You must state clearly and obviously to all end users that you are using code from this project.
- Your application must also be licensed under the same license.
