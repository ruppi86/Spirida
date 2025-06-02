"""
check_environment.py – Simple diagnostic for Spirida environment

This script verifies:
1. That Spirida can be imported.
2. That spiral_interaction is available.
3. That basic execution works without error.
"""

try:
    from spirida.core import spiral_interaction
    print("✅ spirida.core imported successfully.")

    # Test a single pulse run (very minimal)
    print("🔍 Running spiral_interaction test with 1 presence...")
    spiral_interaction(presence=1, rythm="fast", singular=True)
    print("✅ spiral_interaction ran successfully.")

except ModuleNotFoundError as e:
    print(f"❌ ModuleNotFoundError: {e}")
except ImportError as e:
    print(f"❌ ImportError: {e}")
except Exception as e:
    print(f"⚠️ Unexpected error during test: {e}")
