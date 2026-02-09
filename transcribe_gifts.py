import json
from datetime import datetime

OUTPUT_FILE = "charismata_data.json"

GIFT_DATA = [
    {"id": "weisheit",     "name_de": "Weisheit",      "description": "Um zur rechten Zeit das Richtige zu tun. Die Weisheit lässt uns die Dinge aus Gottes Perspektive sehen.", "icon": "🕊️", "grace_bonus": 15, "category": "Insight"},
    {"id": "einsicht",     "name_de": "Einsicht",      "description": "Um stets das große Ganze im Blick zu haben. Sie hilft uns, die tiefen Wahrheiten des Glaubens zu verstehen.", "icon": "📖", "grace_bonus": 12, "category": "Understanding"},
    {"id": "rat",          "name_de": "Rat",           "description": "Um Entscheidungen überlegt zu treffen und anderen beratend zur Seite zu stehen.", "icon": "🗣️", "grace_bonus": 10, "category": "Counsel"},
    {"id": "staerke",      "name_de": "Stärke",        "description": "Um allen Herausforderungen standzuhalten. Sie gibt Mut und Kraft, auch wenn es schwer wird.", "icon": "💪", "grace_bonus": 18, "category": "Fortitude"},
    {"id": "erkenntnis",   "name_de": "Erkenntnis",    "description": "Um zu unterscheiden, was richtig ist und was falsch. Sie lässt uns Gott in der Schöpfung entdecken.", "icon": "🔍", "grace_bonus": 14, "category": "Knowledge"},
    {"id": "froemmigkeit", "name_de": "Frömmigkeit",   "description": "Um den Kontakt zu Gott nicht zu verlieren. Sie lässt uns Gott als liebenden Vater verehren.", "icon": "🙏", "grace_bonus": 11, "category": "Piety"},
    {"id": "gottesfurcht", "name_de": "Gottesfurcht",  "description": "Um Ehrfurcht vor Gott und seiner gesamten Schöpfung zu haben. Sie hilft, die Sünde zu meiden.", "icon": "🌟", "grace_bonus": 20, "category": "Fear of the Lord"}
]

def generate_json():
    data = {
        "charismata": [
            {
                "id": g["id"],
                "name_de": g["name_de"],
                "description": g["description"],
                "icon": g["icon"],
                "stats": {
                    "grace_bonus": g["grace_bonus"],
                    "category": g["category"],
                    "daily_activations": 0,
                    "max_level": 7
                }
            } for g in GIFT_DATA
        ],
        "player": {
            "total_grace": 0,
            "level": 1,
            "last_activation": datetime.now().isoformat()
        }
    }
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"[✓] {OUTPUT_FILE} mit {len(GIFT_DATA)} Gaben erstellt!")
    print("   → Jetzt einfach `python transcribe_gifts.py` ausführen")

if __name__ == "__main__":
    generate_json()
