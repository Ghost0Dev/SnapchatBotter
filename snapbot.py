import pyautogui
import keyboard
import time
import os
import random
from colorama import init, Fore, Style
from collections import deque

# Initialize colorama for colored console output
init()

class MouseRecorder:
    def __init__(self):
        self.actions = deque()
        self.recording = False
        self.last_time = None
        pyautogui.FAILSAFE = False

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_header(self):
        print(Fore.MAGENTA + """
███████╗███╗   ██╗ █████╗ ██████╗  ██████╗██╗  ██╗ █████╗ ████████╗
██╔════╝████╗  ██║██╔══██╗██╔══██╗██╔════╝██║  ██║██╔══██╗╚══██╔══╝
███████╗██╔██╗ ██║███████║██████╔╝██║     ███████║███████║   ██║   
╚════██║██║╚██╗██║██╔══██║██╔═══╝ ██║     ██╔══██║██╔══██║   ██║   
███████║██║ ╚████║██║  ██║██║     ╚██████╗██║  ██║██║  ██║   ██║   
╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝      ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
                                                                   
███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗      
██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗     
███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝     
╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗     
███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║     
╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝     
                                                by ghost.techx
        """ + Style.RESET_ALL)

    def print_status(self, status="", recorded_points=0):
        self.clear_console()
        self.print_header()
        print(f"\n{Fore.RED}Status: {Fore.RED}{status}")
        print(f"{Fore.RED}Recorded Actions: {Fore.RED}{recorded_points}")
        print(f"\n{Fore.RED}Controls:")
        print(f"{Fore.RED}[R] Start Recording")
        print(f"{Fore.RED}[F2] Record Click at Current Position")
        print(f"{Fore.RED}[F5] Stop Recording")
        print(f"{Fore.RED}[P] Play Recording")
        print(f"{Fore.RED}[Q] Quit")

    def record_action(self):
        current_pos = pyautogui.position()
        current_time = time.time()
        
        # Calculate delay since last action (max 0.25 seconds)
        delay = min(current_time - self.last_time, 0.25) if self.last_time else 0
            
        self.actions.append({
            'x': current_pos.x,
            'y': current_pos.y,
            'delay': delay,
            'click': True
        })
        self.last_time = current_time
        self.print_status(f"Recording... Mouse at ({current_pos.x}, {current_pos.y})", len(self.actions))

    def start_recording(self):
        self.recording = True
        self.actions.clear()
        self.last_time = None
        self.print_status("Recording started! Press F2 to record clicks, F5 to stop.", 0)
        
        while self.recording:
            if keyboard.is_pressed('f2'):
                self.record_action()
                time.sleep(0.1)
            elif keyboard.is_pressed('f5'):
                self.recording = False
                self.print_status("Recording stopped!", len(self.actions))
                break

    def play_recording(self):
        if not self.actions:
            print(f"\n{Fore.RED}No actions recorded yet!")
            time.sleep(1)
            return

        self.print_status("Playing recording! Press F5 to stop.", len(self.actions))
        
        try:
            while True:
                for action in self.actions:
                    if keyboard.is_pressed('f5'):
                        self.print_status("Playback stopped!", len(self.actions))
                        return

                    # Random chance for a 3-second pause (10% chance)
                    if random.random() < 0.1:
                        time.sleep(3)
                    
                    # Random chance to modify delay (20% chance)
                    if random.random() < 0.2:
                        delay = random.choice([0.2, 0.3])
                    else:
                        delay = action['delay']
                    
                    time.sleep(delay)
                    pyautogui.moveTo(action['x'], action['y'])
                    if action['click']:
                        pyautogui.click()
                
                self.print_status("Restarting playback...", len(self.actions))

        except Exception as e:
            print(f"\n{Fore.RED}Error during playback: {e}")
        
    def run(self):
        self.print_status("Ready to start!")
        
        while True:
            if keyboard.is_pressed('r'):
                self.start_recording()
                time.sleep(0.1)
            elif keyboard.is_pressed('p'):
                self.play_recording()
                time.sleep(0.1)
            elif keyboard.is_pressed('q'):
                self.clear_console()
                print(f"{Fore.RED}Thanks for using SnapBotter !")
                break

if __name__ == "__main__":
    recorder = MouseRecorder()
    recorder.run()