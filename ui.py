"""
ui.py
-----
GUI Module for the Rule-Based AI Chatbot.

Builds the entire interface using CustomTkinter.
Handles:
  - Chat bubble rendering (user right, bot left)
  - Typing animation
  - Dark / Light mode toggle
  - Timestamps on every message
  - Scrollable chat area
  - Keyboard shortcut (Enter to send)
  - Auto-scroll to latest message
  - Chat history clear with confirmation
"""

import customtkinter as ctk
from tkinter import messagebox
import threading
import time
from datetime import datetime

from chatbot import get_response


# ─────────────────────────────────────────────────────────────────────────────
#  Color Palette
# ─────────────────────────────────────────────────────────────────────────────

LIGHT_THEME = {
    "bg":            "#F0F2F5",
    "chat_bg":       "#FFFFFF",
    "header_bg":     "#4F46E5",
    "header_fg":     "#FFFFFF",
    "user_bubble":   "#4F46E5",
    "user_fg":       "#FFFFFF",
    "bot_bubble":    "#EAECF0",
    "bot_fg":        "#1E293B",
    "input_bg":      "#FFFFFF",
    "input_fg":      "#1E293B",
    "input_border":  "#CBD5E1",
    "send_btn":      "#4F46E5",
    "send_fg":       "#FFFFFF",
    "clear_btn":     "#F1F5F9",
    "clear_fg":      "#64748B",
    "exit_btn":      "#FEE2E2",
    "exit_fg":       "#EF4444",
    "time_fg":       "#94A3B8",
    "footer_bg":     "#F8FAFC",
    "typing_fg":     "#6366F1",
    "scrollbar":     "#CBD5E1",
}

DARK_THEME = {
    "bg":            "#0F172A",
    "chat_bg":       "#1E293B",
    "header_bg":     "#312E81",
    "header_fg":     "#E2E8F0",
    "user_bubble":   "#4F46E5",
    "user_fg":       "#FFFFFF",
    "bot_bubble":    "#334155",
    "bot_fg":        "#E2E8F0",
    "input_bg":      "#1E293B",
    "input_fg":      "#E2E8F0",
    "input_border":  "#475569",
    "send_btn":      "#4F46E5",
    "send_fg":       "#FFFFFF",
    "clear_btn":     "#334155",
    "clear_fg":      "#94A3B8",
    "exit_btn":      "#450a0a",
    "exit_fg":       "#FCA5A5",
    "time_fg":       "#64748B",
    "footer_bg":     "#1E293B",
    "typing_fg":     "#818CF8",
    "scrollbar":     "#475569",
}


# ─────────────────────────────────────────────────────────────────────────────
#  ChatbotApp Class
# ─────────────────────────────────────────────────────────────────────────────

class ChatbotApp(ctk.CTk):
    """
    Main application window for the Rule-Based AI Chatbot.
    Inherits from CTk (CustomTkinter root window).
    """

    def __init__(self):
        super().__init__()

        # ── App State ────────────────────────────────────────────
        self.is_dark_mode = False
        self.theme = LIGHT_THEME
        self.typing_label = None        # reference to the "Bot is typing…" widget
        self.message_count = 0          # track number of messages displayed

        # ── Window Configuration ─────────────────────────────────
        self.title("🤖 Rule-Based AI Chatbot")
        self.geometry("820x680")
        self.minsize(640, 520)
        self.resizable(True, True)

        # Center window on screen
        self._center_window(820, 680)

        # Set CustomTkinter appearance
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        # Try to set a window icon (silently skip if assets missing)
        self._set_window_icon()

        # ── Build UI ─────────────────────────────────────────────
        self._build_ui()

        # ── Show Welcome Message ─────────────────────────────────
        self.after(400, self._show_welcome)

    # ─────────────────────────────────────────────────────────────
    #  Private Helpers
    # ─────────────────────────────────────────────────────────────

    def _center_window(self, w: int, h: int):
        """Center the window on the user's screen."""
        self.update_idletasks()
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw - w) // 2
        y = (sh - h) // 2
        self.geometry(f"{w}x{h}+{x}+{y}")

    def _set_window_icon(self):
        """Set the window icon from assets/ folder if it exists."""
        try:
            import os
            icon_path = os.path.join(os.path.dirname(__file__), "assets", "robot.png")
            if os.path.exists(icon_path):
                from PIL import Image, ImageTk
                img = Image.open(icon_path).resize((32, 32))
                self._icon = ImageTk.PhotoImage(img)
                self.iconphoto(True, self._icon)
        except Exception:
            pass  # Silently skip if PIL not installed or icon missing

    def _ts(self) -> str:
        """Return the current time as a short formatted string."""
        return datetime.now().strftime("%I:%M %p")

    def _t(self, key: str) -> str:
        """Return a theme color value by key."""
        return self.theme[key]

    # ─────────────────────────────────────────────────────────────
    #  UI Builder
    # ─────────────────────────────────────────────────────────────

    def _build_ui(self):
        """Construct all UI widgets and layouts."""
        t = self.theme

        self.configure(fg_color=t["bg"])

        # ── Root grid ────────────────────────────────────────────
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # ── HEADER ───────────────────────────────────────────────
        self.header_frame = ctk.CTkFrame(
            self, fg_color=t["header_bg"], corner_radius=0, height=68
        )
        self.header_frame.grid(row=0, column=0, sticky="ew")
        self.header_frame.grid_propagate(False)
        self.header_frame.grid_columnconfigure(0, weight=1)

        # Title label
        self.title_label = ctk.CTkLabel(
            self.header_frame,
            text="🤖  Rule-Based AI Chatbot",
            font=ctk.CTkFont(family="Segoe UI", size=20, weight="bold"),
            text_color=t["header_fg"],
        )
        self.title_label.grid(row=0, column=0, padx=20, pady=14, sticky="w")

        # Dark-mode toggle button (top-right)
        self.mode_btn = ctk.CTkButton(
            self.header_frame,
            text="🌙 Dark",
            width=90,
            height=32,
            corner_radius=16,
            font=ctk.CTkFont(size=13),
            fg_color="#6366F1",
            hover_color="#4338CA",
            text_color="#FFFFFF",
            command=self._toggle_dark_mode,
        )
        self.mode_btn.grid(row=0, column=1, padx=16, pady=14, sticky="e")

        # Subtitle / status label
        self.status_label = ctk.CTkLabel(
            self.header_frame,
            text="● Online  —  Rule-Based Logic  |  No AI APIs",
            font=ctk.CTkFont(family="Segoe UI", size=11),
            text_color="#A5B4FC",
        )
        self.status_label.grid(row=1, column=0, padx=22, pady=(0, 10), sticky="w")

        # ── CHAT AREA (scrollable canvas frame) ──────────────────
        self.chat_outer = ctk.CTkFrame(
            self, fg_color=t["bg"], corner_radius=0
        )
        self.chat_outer.grid(row=1, column=0, sticky="nsew", padx=0, pady=0)
        self.chat_outer.grid_rowconfigure(0, weight=1)
        self.chat_outer.grid_columnconfigure(0, weight=1)

        self.chat_scroll = ctk.CTkScrollableFrame(
            self.chat_outer,
            fg_color=t["chat_bg"],
            corner_radius=0,
            scrollbar_button_color=t["scrollbar"],
            scrollbar_button_hover_color=t["header_bg"],
        )
        self.chat_scroll.grid(row=0, column=0, sticky="nsew",
                              padx=12, pady=(12, 0))
        self.chat_scroll.grid_columnconfigure(0, weight=1)

        # ── FOOTER (Input area) ───────────────────────────────────
        self.footer_frame = ctk.CTkFrame(
            self, fg_color=t["footer_bg"],
            corner_radius=0, height=80
        )
        self.footer_frame.grid(row=2, column=0, sticky="ew", padx=0, pady=0)
        self.footer_frame.grid_propagate(False)
        self.footer_frame.grid_columnconfigure(0, weight=1)

        # Separator line
        sep = ctk.CTkFrame(self.footer_frame, fg_color="#E2E8F0", height=1)
        sep.grid(row=0, column=0, columnspan=4, sticky="ew", padx=0, pady=0)
        self._sep = sep

        # Text input field
        self.input_var = ctk.StringVar()
        self.input_field = ctk.CTkEntry(
            self.footer_frame,
            textvariable=self.input_var,
            placeholder_text="Type a message…  (Enter to send)",
            font=ctk.CTkFont(family="Segoe UI", size=14),
            fg_color=t["input_bg"],
            text_color=t["input_fg"],
            border_color=t["input_border"],
            border_width=2,
            corner_radius=24,
            height=44,
        )
        self.input_field.grid(row=1, column=0, padx=(14, 6), pady=18, sticky="ew")
        self.input_field.bind("<Return>", self._on_enter_pressed)
        self.input_field.focus()

        # SEND button
        self.send_btn = ctk.CTkButton(
            self.footer_frame,
            text="Send ➤",
            width=90,
            height=44,
            corner_radius=22,
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color=t["send_btn"],
            hover_color="#4338CA",
            text_color=t["send_fg"],
            command=self._send_message,
        )
        self.send_btn.grid(row=1, column=1, padx=4, pady=18)

        # CLEAR button
        self.clear_btn = ctk.CTkButton(
            self.footer_frame,
            text="🗑 Clear",
            width=90,
            height=44,
            corner_radius=22,
            font=ctk.CTkFont(size=13),
            fg_color=t["clear_btn"],
            hover_color="#E2E8F0",
            text_color=t["clear_fg"],
            command=self._clear_chat,
        )
        self.clear_btn.grid(row=1, column=2, padx=4, pady=18)

        # EXIT button
        self.exit_btn = ctk.CTkButton(
            self.footer_frame,
            text="✕ Exit",
            width=80,
            height=44,
            corner_radius=22,
            font=ctk.CTkFont(size=13),
            fg_color=t["exit_btn"],
            hover_color="#FECACA",
            text_color=t["exit_fg"],
            command=self._confirm_exit,
        )
        self.exit_btn.grid(row=1, column=3, padx=(4, 14), pady=18)

    # ─────────────────────────────────────────────────────────────
    #  Message Rendering
    # ─────────────────────────────────────────────────────────────

    def _add_message(self, text: str, sender: str):
        """
        Add a message bubble to the chat area.

        Args:
            text   (str): The message text content.
            sender (str): "user" or "bot".
        """
        t = self.theme
        is_user = (sender == "user")

        # ── Outer row frame ───────────────────────────────────────
        row_frame = ctk.CTkFrame(self.chat_scroll, fg_color="transparent")
        row_frame.grid(sticky="ew", padx=6, pady=4)
        row_frame.grid_columnconfigure(0, weight=1)

        # ── Avatar + Bubble column layout ─────────────────────────
        inner = ctk.CTkFrame(row_frame, fg_color="transparent")
        inner.grid(sticky="e" if is_user else "w")

        # Bot avatar (emoji label) on the left
        if not is_user:
            avatar = ctk.CTkLabel(
                inner,
                text="🤖",
                font=ctk.CTkFont(size=22),
                fg_color="transparent",
                width=36,
            )
            avatar.grid(row=0, column=0, sticky="s", padx=(0, 6), pady=(0, 4))

        # Message bubble
        bubble_bg = t["user_bubble"] if is_user else t["bot_bubble"]
        bubble_fg = t["user_fg"] if is_user else t["bot_fg"]

        bubble = ctk.CTkLabel(
            inner,
            text=text,
            font=ctk.CTkFont(family="Segoe UI", size=13),
            text_color=bubble_fg,
            fg_color=bubble_bg,
            corner_radius=18,
            justify="left",
            wraplength=440,
            padx=16,
            pady=10,
            anchor="w",
        )
        bubble_col = 1 if not is_user else 0
        bubble.grid(row=0, column=bubble_col, sticky="nsew")

        # Timestamp label below bubble
        ts_label = ctk.CTkLabel(
            inner,
            text=self._ts(),
            font=ctk.CTkFont(size=10),
            text_color=t["time_fg"],
            fg_color="transparent",
        )
        ts_label.grid(
            row=1,
            column=bubble_col,
            sticky="e" if is_user else "w",
            padx=6,
            pady=(2, 0),
        )

        self.message_count += 1

        # Auto-scroll to bottom after a short delay (allows widget to render)
        self.after(50, self._scroll_to_bottom)

    def _show_typing_indicator(self):
        """Display a 'Bot is typing…' animated label in the chat."""
        t = self.theme
        self.typing_label = ctk.CTkLabel(
            self.chat_scroll,
            text="🤖  Bot is typing…",
            font=ctk.CTkFont(family="Segoe UI", size=12, slant="italic"),
            text_color=t["typing_fg"],
            fg_color="transparent",
            anchor="w",
        )
        self.typing_label.grid(sticky="w", padx=16, pady=(4, 2))
        self.after(50, self._scroll_to_bottom)

    def _remove_typing_indicator(self):
        """Remove the 'Bot is typing…' label from the chat."""
        if self.typing_label:
            self.typing_label.destroy()
            self.typing_label = None

    def _scroll_to_bottom(self):
        """Scroll the chat area to show the latest message."""
        try:
            self.chat_scroll._parent_canvas.yview_moveto(1.0)
        except Exception:
            pass

    # ─────────────────────────────────────────────────────────────
    #  Event Handlers
    # ─────────────────────────────────────────────────────────────

    def _on_enter_pressed(self, event=None):
        """Keyboard shortcut: Enter key sends the message."""
        self._send_message()

    def _send_message(self):
        """
        Read user input, display it, then trigger bot response
        with a typing animation in a background thread.
        """
        raw = self.input_var.get().strip()
        if not raw:
            return

        # Display user message
        self._add_message(raw, "user")

        # Clear input field
        self.input_var.set("")
        self.input_field.focus()

        # Disable send button to prevent double-send
        self.send_btn.configure(state="disabled")

        # Show typing indicator, then fetch bot reply in background
        self._show_typing_indicator()
        threading.Thread(
            target=self._process_response,
            args=(raw,),
            daemon=True
        ).start()

    def _process_response(self, user_input: str):
        """
        Run in a background thread.
        Simulates a brief 'typing' delay then shows bot response.
        """
        # Simulate typing delay (0.8 – 1.4 seconds)
        time.sleep(0.9)

        response_text, should_exit = get_response(user_input)

        # Update UI from main thread
        self.after(0, self._display_bot_response, response_text, should_exit)

    def _display_bot_response(self, response_text: str, should_exit: bool):
        """
        Called from main thread after typing delay.
        Removes indicator, shows response, re-enables send button.
        """
        self._remove_typing_indicator()
        self._add_message(response_text, "bot")
        self.send_btn.configure(state="normal")

        # If exit command was given, close app after brief delay
        if should_exit:
            self.after(1800, self.destroy)

    # ─────────────────────────────────────────────────────────────
    #  Welcome Message
    # ─────────────────────────────────────────────────────────────

    def _show_welcome(self):
        """Display the welcome message from the bot on startup."""
        from chatbot import get_time_greeting
        welcome = (
            f"{get_time_greeting()} Welcome! 🎉\n\n"
            "I'm your Rule-Based AI Chatbot.\n"
            "I'm here to chat and share knowledge!\n\n"
            "💡 Try asking me about:\n"
            "   Python  •  AI  •  Programming\n"
            "   Technology  •  Computers  •  Chatbots\n\n"
            "Type 'help' to see all my commands.\n"
            "Type 'exit' or 'bye' to say goodbye. 👋"
        )
        self._add_message(welcome, "bot")

    # ─────────────────────────────────────────────────────────────
    #  Clear Chat
    # ─────────────────────────────────────────────────────────────

    def _clear_chat(self):
        """Prompt user for confirmation, then clear all chat messages."""
        confirmed = messagebox.askyesno(
            title="Clear Chat",
            message="Are you sure you want to clear the entire chat history?\n"
                    "This action cannot be undone.",
            icon="warning",
        )
        if confirmed:
            # Destroy all children widgets in the scrollable frame
            for widget in self.chat_scroll.winfo_children():
                widget.destroy()
            self.message_count = 0
            self.typing_label = None
            # Show a fresh welcome after clearing
            self.after(200, self._show_welcome)

    # ─────────────────────────────────────────────────────────────
    #  Dark Mode Toggle
    # ─────────────────────────────────────────────────────────────

    def _toggle_dark_mode(self):
        """Switch between Light and Dark themes."""
        self.is_dark_mode = not self.is_dark_mode

        if self.is_dark_mode:
            self.theme = DARK_THEME
            ctk.set_appearance_mode("dark")
            self.mode_btn.configure(text="☀️ Light")
        else:
            self.theme = LIGHT_THEME
            ctk.set_appearance_mode("light")
            self.mode_btn.configure(text="🌙 Dark")

        self._apply_theme()

    def _apply_theme(self):
        """Re-apply theme colors to all major widgets after a mode switch."""
        t = self.theme

        self.configure(fg_color=t["bg"])
        self.header_frame.configure(fg_color=t["header_bg"])
        self.title_label.configure(text_color=t["header_fg"])
        self.status_label.configure(text_color="#A5B4FC" if self.is_dark_mode else "#A5B4FC")
        self.chat_outer.configure(fg_color=t["bg"])
        self.chat_scroll.configure(
            fg_color=t["chat_bg"],
            scrollbar_button_color=t["scrollbar"],
        )
        self.footer_frame.configure(fg_color=t["footer_bg"])
        self._sep.configure(fg_color="#334155" if self.is_dark_mode else "#E2E8F0")
        self.input_field.configure(
            fg_color=t["input_bg"],
            text_color=t["input_fg"],
            border_color=t["input_border"],
        )
        self.send_btn.configure(fg_color=t["send_btn"], text_color=t["send_fg"])
        self.clear_btn.configure(
            fg_color=t["clear_btn"],
            text_color=t["clear_fg"],
            hover_color="#475569" if self.is_dark_mode else "#E2E8F0",
        )
        self.exit_btn.configure(
            fg_color=t["exit_btn"],
            text_color=t["exit_fg"],
            hover_color="#7f1d1d" if self.is_dark_mode else "#FECACA",
        )

    # ─────────────────────────────────────────────────────────────
    #  Exit Confirmation
    # ─────────────────────────────────────────────────────────────

    def _confirm_exit(self):
        """Ask user before closing the application."""
        confirmed = messagebox.askyesno(
            title="Exit Chatbot",
            message="Are you sure you want to exit the chatbot?\n"
                    "All chat history will be lost.",
            icon="question",
        )
        if confirmed:
            self.destroy()
