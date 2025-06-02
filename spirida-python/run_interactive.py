"""
run_interactive.py – Spirida launcher with interactive terminal dialog

Guides the user through a slow-technology ritual, asking for parameters,
logging the spiral memory trace, and optionally visualizing the spiral.
"""

import sys
import os
import time
from spirida.core import spiral_interaction
from spirida.spiralbase import print_memory_trace

# Ensure spirida is importable even if run from subfolder
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

def prompt_bool(question):
    return input(question + " (y/n): ").strip().lower() in ["y", "yes"]

def main():
    print("\n🌿 Welcome to Spirida Interactive 🌿")
    print("Let's set the spiral...\n")

    try:
        presence = int(input("How many presence cycles? (e.g., 5, 8): "))
    except ValueError:
        presence = 5

    rhythm = input("Rhythm? (slow / fast / or seconds like 0.8): ").strip() or "slow"
    singular = not prompt_bool("Allow symbolic variation (i.e. not singular)?")
    do_log = prompt_bool("Would you like to save this session to log.txt?")
    do_visual = prompt_bool("Visual spiral output with ASCII symbols?")

    print("\n🌬️ Preparing your spiral journey...")
    time.sleep(1)

    if do_log:
        with open("spirida_log.txt", "a", encoding="utf-8") as f:
            f.write(f"\n\n--- New Spirida Session ---\n")
            f.write(f"Presence: {presence}, Rhythm: {rhythm}, Singular: {singular}\n")

    def log_callback(msg):
        if do_log:
            with open("spirida_log.txt", "a", encoding="utf-8") as f:
                f.write(msg + "\n")
        if do_visual:
            print(msg)

    # Wrap spiral_interaction with visual+log hook
    original_print = print
    try:
        if do_visual or do_log:
            def hooked_print(*args, **kwargs):
                msg = " ".join(str(a) for a in args)
                log_callback(msg)
            globals()["print"] = hooked_print

        spiral_interaction(presence=presence, rythm=rhythm, singular=singular)

    finally:
        globals()["print"] = original_print

    print("\n🌙 The spiral rests. Thank you for being present.\n")
    if do_log:
        print("📝 Your session was saved to 'spirida_log.txt'.")

if __name__ == "__main__":
    main()
