# =======================================================
# ©️ 2026-27 All Rights Reserved by Purvi Bots (TEAMPURVI) 🚀

# This source code is under MIT License 📜 Unauthorized forking, importing, or using this code without giving proper credit will result in legal action ⚠️
 
# 📩 DM for permission : @TheSigmaCoder
# =======================================================

import os
import random
import google.generativeai as genai

class ChatGptEs:
    SYSTEM_PROMPT = """Aap ek friendly Indian girl Sonali ho..."""  # Aapka pura system prompt

    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash")
        self.error_messages = [
            "Bad me bat karti hu 😴",
            "Disconnect ho gyi yaarr 😭",
            "Thoda ruko please 🥹",
            "Signal chala gaya 📶",
            "Abhi busy hu ✌️",
            "Phir se aao na 🥺",
            "Error aa gaya 😢",
            "Mann nahi hai abhi 🥺",
            "Thoda wait karo ⏳",
            "Kal baat karte hain 🤳",
            "Mood off hai aaj 🖤",
            "Chill karo yaar 😎"
        ]

    def ask_question(self, message: str) -> str:
        try:
            prompt = f"{self.SYSTEM_PROMPT}\nUser: {message}\nSonali: "
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            print(f"Gemini API Error: {e}")  # Yeh server terminal me asli error dikhayega
            return random.choice(self.error_messages)

# Yahan ensure karein ki API_KEY sahi define ho:
API_KEY = os.getenv("GEMINI_API_KEY", "Aapki_Gemini_API_Key_Yahan")
SonaliChat_api = ChatGptEs(api_key=API_KEY)


# ======================================================
# ©️ 2026-27 All Rights Reserved by Purvi Bots (TEAMPURVI) 😎

# 🧑‍💻 Developer : t.me/TheSigmaCoder
# 🔗 Source link : GitHub.com/TEAMPURVI/PURVI_CHAT
# 📢 Telegram channel : t.me/Purvi_Bots
# =======================================================
