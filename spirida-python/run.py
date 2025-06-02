"""
run.py – Spirida launcher

This file serves as a reliable entry point into the Spirida system,
allowing you to initiate a spiral interaction from the command line.

Usage:
    python run.py --presence 7 --rhythm slow --singular False
"""
 
import argparse
import sys
import os

# Ensure the 'spirida' package is importable
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from spirida.core import spiral_interaction

def main():
    parser = argparse.ArgumentParser(description="🌿 Run a Spirida spiral interaction.")
    parser.add_argument("--presence", type=int, default=5, help="Number of presence cycles (default: 5)")
    parser.add_argument("--rhythm", type=str, default="slow", help="Rhythm: slow, fast, or a float in seconds")
    parser.add_argument("--singular", type=str, default="True", help="Singular mode (True/False)")

    args = parser.parse_args()

    # Convert singular argument from string to boolean
    singular = args.singular.lower() in ["true", "1", "yes", "y"]

    print("\n🌿 Welcome to Spirida via run.py 🌿")
    print(f"Initiating with presence={args.presence}, rhythm={args.rhythm}, singular={singular}\n")

    spiral_interaction(presence=args.presence, rythm=args.rhythm, singular=singular)

    print("\n🌙 Spirida session complete.")

if __name__ == "__main__":
    main()
