# Packing Pal

Packing Pal is a holiday packing assistant. It asks where you're going, when, and who's travelling. It then shows the usual weather for that time of year and builds a packing list, daily outfit ideas and a plan of things to do. You can change all of it.

It's a single `index.html` file with no build step, no server and no sign-up.

## Features

**Trip set-up in four steps**
1. **Where are you going?** Pick from a dropdown of 70 destinations (cities, beaches, countryside, winter breaks and ski resorts) or type anywhere. Choose the type of trip: Beach & sun, City break, Countryside & walking, Winter sightseeing or Ski / snowboard.
2. **Pick your dates.** A monthly calendar: tap the day you leave, then the day you come home.
3. **Who's travelling?** Name and age. The age sets the app's theme and adjusts the list:
   - **Sunny** (0–12): bigger, rounder, with kids' extras such as snacks and a comfort toy
   - **Night Flight** (13–19): a dark theme with teen extras such as headphones and a second power bank
   - **Classic** (20–59)
   - **Easy Read** (60+): larger text, stronger contrast and comfort items
4. **Weather.** Typical daytime highs and night-time lows for that destination and month.

**The trip folder.** Results open in a file-style folder with four tabs:

| Tab | What it does |
|---|---|
| **Packing List** | Clothes as a checklist. Tick items off, change any quantity with − / + (e.g. trousers 1 → 5), remove items or add your own. |
| **Essentials** | Toiletries, documents, tech and the extras for your age group, with the same checklist controls. |
| **Daily Outfits** | One page per trip day. Type what you're doing and get outfit ideas that match the activity and the weather. Add any idea to the Packing List in one tap, hide ideas, or add your own pieces. |
| **Things to Do** | A few quick questions (who's going, interests, pace, budget), then picture tiles of real places near the destination. Tap the heart to save one, or tap the tile for a full page with a description, quick facts, what to wear and links to Tripadvisor and Google Maps. Add any idea to a day, or type your own plans. |

**Other features**
- **Copy list:** copies the Packing List and Essentials as plain text to paste into Notes or a message.
- **App colour:** the palette button in the top-right corner recolours the whole app (background, cards, folder tabs and buttons). There are 12 preset colours or you can choose your own. Light text switches on automatically for dark colours.
- **Saves as you go:** progress, ticks, quantities, plans and the chosen colour are kept in the browser, so you can close the page and come back.
- **Works on phones:** the layout fits phone screens as well as desktops.

## Getting started

### Run it locally
Download `index.html` and open it in any modern browser. That's it.

### Publish with GitHub Pages
1. Create a new repository and upload `index.html` and this `README.md`.
2. Go to **Settings → Pages**.
3. Under **Build and deployment**, set the source to **Deploy from a branch**, choose `main` and `/ (root)`, then click **Save**.
4. After a minute or so, the app is live at `https://<your-username>.github.io/<repository-name>/`.

## How it works

- **Weather data:** each built-in destination has typical monthly high and low temperatures (climate averages) stored in the file. These are not live forecasts. The app reminds travellers to check a real forecast about 10 days before they fly.
- **Destinations not on the list:** the traveller picks the usual climate (Freezing, Cold, Mild, Warm or Hot) and the app plans from that.
- **Outfit ideas:** the Daily Outfits page looks for activity words in your plans, such as *hike*, *beach*, *dinner*, *museum*, *temple*, *spa*, *meeting* or *boat*. It combines them with the day's weather and the trip type to suggest clothes. With no plans entered, it suggests clothes from the weather and trip type alone, plus comfy travel clothes on the first and last days.
- **Things to Do ideas and photos:** when Packing Pal runs on its own (for example on GitHub Pages), it finds real places near the destination using Wikipedia's free API, ranks them by the traveller's interests, and shows their photos from Wikimedia Commons with a credit link on each details page. Places without a suitable photo are left out. Opening times and prices aren't included, so the app tells travellers to check before they go. When the app is opened inside Claude, Claude writes the ideas instead, and they show drawn illustrations because outside photos can't load there.
- **Storage:** everything is saved in the browser's `localStorage` on that device only. Nothing is sent to a server. Clearing browser data or using a private window starts fresh.

## Project structure

```
index.html   The whole app: markup, styles, scripts and the logo (embedded as an image)
README.md    This file
```

The only external resource is Google Fonts (Fredoka, Nunito and Atkinson Hyperlegible). Without an internet connection the app falls back to standard system fonts and still works.

## Customising

All the content lives in the `<script>` block inside `index.html`:

- **Add or edit destinations:** the `PLACES` object. Each entry has a trip type, altitude in metres, and 12 monthly highs and lows in °C (January to December):
  ```js
  "Lisbon, Portugal":{t:"city",alt:0,hi:[15,16,19,20,23,26,28,29,27,23,18,15],lo:[8,9,11,12,14,17,18,19,18,15,11,9]},
  ```
  Trip types are `city`, `beach`, `country`, `snow` and `ski`.
- **Change the starting packing list:** the `buildList()` function.
- **Change outfit ideas for activities:** the `RULES` list, which pairs activity words with suggested clothes.
- **Change the colour choices:** the `TILES` list (palette) and the `:root` colour settings at the top of the `<style>` block (age themes).

## Browser support

Works in current versions of Chrome, Edge, Safari and Firefox on desktop and mobile. Your own custom colours and the dark Night colour use the CSS `color-mix()` function, which needs a browser released in 2023 or later.

## Credits

Created by Vanita Rattan. The Packing Pal logo is part of the project.

## Licence

No licence has been chosen yet. Add one before sharing the code publicly, for example via **Add file → Create new file → `LICENSE`** on GitHub, which offers templates.
