# TRIP-Sense — AI Travel Planner 

> *Travel Smarter. Explore Deeper.*

TRIP-Sense is a single-page AI-powered travel planning web app for Indian destinations. Type a natural language query — it handles everything: destination recommendations, day-by-day itineraries, budget breakdowns, hotel suggestions, and live route maps.

---

## Live Demo

Open `TRIP-Sense-UI.html` directly in any browser — no server, no build step, no dependencies to install.

---

## Features

### Natural Language Search
Type like you'd tell a friend — *"3 days in Goa under ₹20,000 for beaches"*. A custom NLP parser extracts destination, duration, budget and interests automatically.

### Destination Recommendations
A rule-based scoring engine matches destinations from a 16-city database against your budget, duration and interests — returning ranked cards with match percentages.

### Day-by-Day Itineraries
City-specific itinerary engine with real landmark names, opening hours, entry costs and local food recommendations. Weather-aware — adjusts tips based on the current month. Covers:
- Hyderabad · Goa · Jaipur · Mumbai · Varanasi
- Ladakh · Kerala · Manali · Rishikesh *(+ 7 more via fallback)*

### Live Interactive Maps
- **OpenStreetMap tiles** via Leaflet.js — full realistic map rendering
- **Overpass API** — fetches real attractions (forts, museums, parks, monuments) near the searched city and pins them on the map
- Custom emoji markers per attraction type (🏰 forts, 🏛️ museums, 🌳 parks, etc.)

### Smart Budget Planner
Auto-splits your total budget across accommodation, food, transport and activities — visualised as an animated breakdown bar chart.

### Hotel & Package Recommendations
City-specific hotel picks across budget, comfort and luxury tiers, with area, price/night, amenities and a "why this hotel" note. Package builder with three travel styles (Budget / Comfort / Luxury).

### AI Travel Chatbot
Floating chat assistant powered by the Claude API (Anthropic). Falls back to a rule-based local engine when no API key is provided — handles questions about hotels, budgets, best time to visit, itineraries and general travel advice.

### Trending Destinations Strip
Horizontally scrollable destination cards with real city photography (Unsplash). Click any card to auto-fill the search.

---

## Tech Stack

| Technology | Usage |
|---|---|
| HTML / CSS / JavaScript | Entire UI, logic, animations |
| [Leaflet.js](https://leafletjs.com/) | Interactive map rendering |
| [OpenStreetMap](https://www.openstreetmap.org/) | Realistic map tiles |
| [Overpass API](https://overpass-api.de/) | Live real-world attraction data |
| [Claude API (Anthropic)](https://www.anthropic.com/) | AI itinerary & chat (optional) |
| [Unsplash](https://unsplash.com/) | Destination photography |
| [Google Fonts](https://fonts.google.com/) | Fraunces (display) + Outfit (body) |

> **No frameworks. No build tools. No npm.** Pure vanilla JS — open the HTML file and it works.

---

## Setup

### Without Claude API (works immediately)
```bash
# Just open the file
open TRIP-Sense-UI.html
```
All features work — itineraries, maps, recommendations and chat use the built-in local engine.

### With Claude API (enhanced AI responses)
1. Get an API key from [console.anthropic.com](https://console.anthropic.com/)
2. Open the app in your browser
3. Click the **Add API Key** pill in the navbar
4. Paste your key — it's stored only in memory for the session

The AI itinerary generator and chatbot will now use Claude `claude-sonnet-4-20250514` for real responses.

---

## Project Structure

```
TRIP-Sense/
└── TS-UI.html        # Entire application — UI, logic, data, styles
└── README.md
```

Everything lives in one self-contained HTML file:
- **CSS** (~600 lines) — design system, dark theme, animations
- **HTML** (~200 lines) — semantic layout and sections
- **JavaScript** (~1,000 lines) — NLP parser, recommendation engine, itinerary builder, map integration, chat system

---

## How the Recommendation Engine Works

```
User Input  ->  NLP Parser  ->  Extracted: { dest, days, budget, interests }
                                    |
                          Score each of 16 destinations:
                          - Budget fit          (40 pts)
                          - Interest tag match  (30 pts)
                          - Rating              (20 pts)
                          - Duration suitability (10 pts)
                                    |
                          Return ranked cards + itinerary + map
```

---

## Supported Destinations

| City | State | Best For |
|---|---|---|
| Hyderabad | Telangana | Heritage, Food, Culture |
| Goa | Goa | Beach, Nightlife, Food |
| Manali | Himachal Pradesh | Mountains, Adventure |
| Kerala | Kerala | Backwaters, Nature |
| Jaipur | Rajasthan | Heritage, Culture |
| Ladakh | Ladakh | Trekking, Landscapes |
| Rishikesh | Uttarakhand | Adventure, Spiritual |
| Varanasi | Uttar Pradesh | Spiritual, Heritage |
| Udaipur | Rajasthan | Romantic, Lakes |
| Mumbai | Maharashtra | Food, Nightlife |
| Andaman | A&N Islands | Diving, Beach |
| Coorg | Karnataka | Nature, Hill Station |
| Ooty | Tamil Nadu | Hill Station, Nature |
| Mysore | Karnataka | Heritage, Culture |
| Hampi | Karnataka | History, Adventure |
| Darjeeling | West Bengal | Tea, Mountains |

---

## Author

**Manaswi Priya**
- GitHub: [@manaswipriyaa](https://github.com/manaswipriyaa)
