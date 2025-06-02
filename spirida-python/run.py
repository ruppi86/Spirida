"""
run.py – Spirida launcher (CLI version)

This file serves as a reliable entry point into the Spirida system,
allowing you to initiate a spiral interaction from the command line.

Usage:
    python run.py --presence 7 --rhythm slow --singular False --log --visual --verbose
"""

import argparse
import sys
import os
from spirida.core import spiral_interaction

# Ensure the 'spirida' package is importable
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

def main():
    parser = argparse.ArgumentParser(description="🌿 Run a Spirida spiral interaction.")
    parser.add_argument("--presence", type=int, default=5, help="Number of presence cycles (default: 5)")
    parser.add_argument("--rhythm", type=str, default="slow", help="Rhythm: slow, fast, or a float in seconds")
    parser.add_argument("--singular", type=str, default="True", help="Singular mode (True/False)")
    parser.add_argument("--log", action="store_true", help="Log output to spirida_log.txt")
    parser.add_argument("--visual", action="store_true", help="Display spiral output as visual ASCII in console")
    parser.add_argument("--verbose", action="store_true", help="Enable narrative commentary for each cycle")

    args = parser.parse_args()
    singular = args.singular.lower() in ["true", "1", "yes", "y"]

    print("\n🌿 Welcome to Spirida via run.py 🌿")
    print(f"Initiating with presence={args.presence}, rhythm={args.rhythm}, singular={singular}\n")

    if args.log:
        with open("spirida_log.txt", "a", encoding="utf-8") as f:
            f.write(f"\n\n--- New Spirida Session ---\n")
            f.write(f"Presence: {args.presence}, Rhythm: {args.rhythm}, Singular: {singular}, Verbose: {args.verbose}\n")

    def log_callback(msg):
        if args.log:
            with open("spirida_log.txt", "a", encoding="utf-8") as f:
                f.write(msg + "\n")
        if args.visual:
            print(msg)

    spiral_interaction(
        presence=args.presence,
        rythm=args.rhythm,
        singular=singular,
        on_output=log_callback if (args.log or args.visual) else None,
        verbose=args.verbose
    )

    print("\n🌙 Spirida session complete.")
    if args.log:
        print("📝 Your session was saved to 'spirida_log.txt'.")

if __name__ == "__main__":
    main()
