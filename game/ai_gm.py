"""Gemini API AI Game Master Integration for Starveil RPG.
Provides dynamic ambient narration, atmospheric descriptions, dynamic NPC responses, and AI event generation.
"""

import os
import json
import httpx

class AIGameMaster:
    def __init__(self, api_key: str | None = None):
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY", "")
        self.system_prompt = (
            "You are a Senior Narrative AI Game Master for 'STARVEIL', a dark, immersive science-fiction text RPG. "
            "Write vivid, concise, atmospheric narrative responses (2-4 sentences max). "
            "Focus on cyberpunk tones, ancient alien mysteries, corporate intrigue, and cosmic space exploration."
        )

    def generate_narration(self, context_prompt: str) -> str:
        """Generates dynamic atmospheric text using Gemini REST API."""
        if not self.api_key:
            return ""

        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={self.api_key}"
        headers = {"Content-Type": "application/json"}
        
        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": f"{self.system_prompt}\n\nContext:\n{context_prompt}"}
                    ]
                }
            ],
            "generationConfig": {
                "temperature": 0.8,
                "maxOutputTokens": 200
            }
        }

        try:
            resp = httpx.post(url, json=payload, headers=headers, timeout=8.0)
            if resp.status_code == 200:
                data = resp.json()
                candidates = data.get("candidates", [])
                if candidates:
                    parts = candidates[0].get("content", {}).get("parts", [])
                    if parts:
                        return parts[0].get("text", "").strip()
        except Exception as e:
            # Fallback quietly
            pass
        return ""
