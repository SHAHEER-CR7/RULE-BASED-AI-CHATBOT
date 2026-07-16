"""
main.py
-------
Entry Point for the Rule-Based AI Chatbot.

Run this file to launch the application:
    python main.py

Dependencies:
    customtkinter   (pip install customtkinter)
    Pillow          (pip install Pillow)  -- optional, for window icon
"""

import sys
import os

# Fix Windows terminal Unicode/emoji encoding issues
if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

# ── Dependency Check ─────────────────────────────────────────────────────────
def check_dependencies():
    """
    Verify that required packages are installed.
    Provides a user-friendly error message if not.
    """
    missing = []

    try:
        import customtkinter
    except ImportError:
        missing.append("customtkinter")

    if missing:
        print("=" * 60)
        print("  ❌  Missing Required Package(s)")
        print("=" * 60)
        for pkg in missing:
            print(f"  • {pkg}")
        print()
        print("  Please install them by running:")
        print(f"  pip install {' '.join(missing)}")
        print("=" * 60)
        sys.exit(1)


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    """
    Application entry point.
    Checks dependencies and launches the GUI.
    """
    check_dependencies()

    # Import here (after dependency check)
    from ui import ChatbotApp

    print("=" * 50)
    print("  [BOT]  Rule-Based AI Chatbot  |  Starting...")
    print("=" * 50)
    print("  [OK]  No ML / No AI APIs - Pure Python Logic")
    print("  [OK]  GUI powered by CustomTkinter")
    print("  [OK]  Close the window or type exit to quit")
    print("=" * 50)

    app = ChatbotApp()
    app.mainloop()

    print("\n  Chatbot session ended. Goodbye!")


if __name__ == "__main__":
    main()
