# SnapBotter - Mouse Recorder

SnapBotter is a simple Python tool for recording and replaying mouse movements and clicks.

## Requirements
Before running the script, ensure that all necessary dependencies are installed.

### Required Packages:
The script uses the following Python libraries:
- `pyautogui`
- `keyboard`
- `colorama`

Install the dependencies with the following command:
```sh
pip install pyautogui keyboard colorama
```

## Usage
Run the script with Python:
```sh
python scriptname.py
```
Replace `scriptname.py` with the actual filename.

### Controls
- **[R]** Start recording
- **[F2]** Save a click at the current position
- **[F5]** Stop recording or playback
- **[P]** Play the recorded actions
- **[Q]** Quit the program

## Features
- **Record mouse actions:** The script saves mouse positions and clicks.
- **Playback with delay:** It can replay the recorded actions with variable delays.
- **Random pauses:** For a more realistic playback, random wait times are included.

## Note
This script is created for experimental purposes. Use it responsibly!
