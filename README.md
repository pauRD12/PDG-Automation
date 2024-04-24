# PDG-Automation
HDA to create multiple versions of a simulation, cache them, set up a comparison video and send an email notification. All automated in a single node
### Prerequisites:
- Have `FFmpeg` installed: https://ffmpeg.org/download.html
- Have `ImageMagick` installed: https://imagemagick.org/script/download.php
- Generate a Gmail app password following [these steps](https://support.google.com/accounts/answer/185833?hl=en). That app password is what you should enter in your `email_password.json` file, not the usual one!
### Installation:
1. Modify the file `email_password.json` with your password (app passwprd) and save it to a secure location on your computer. This is the file you have to refer to from the HDA `Password File` parameter
2. Download the `.hda` file and put it in your `otls` directory (on Windows, that's usually `\Documents\houdinixx.x\otls)`.
4. Launch Houdini and the HDA should appear in the TAB Menu under the name `Comparative Video Generator` (only in the SOP context).
