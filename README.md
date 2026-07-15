# Camperreis 2026 — Atlantische kust · Picos de Europa · Pyreneeën

Interactief reisoverzicht (één zelfstandig HTML-bestand) voor de camperreis van
**6 augustus t/m 1 september 2026**: een grote lus van ~4.322 km, met andere
wegen heen dan terug.

## Bekijken
Open **`index.html`** (of `Camperreis-2026-Picos-Pyreneeen.html`) in een browser.
Geen installatie nodig — kaart-tiles en de Leaflet-library laden via CDN, alle
reisdata staat inline.

De pagina heeft drie tabs:
- **Dagplanning** — etappes per dag met afstand + rijtijd.
- **POI's per categorie** — 81 bestemmingen in categorieën (bergpas, kabelbaan,
  wandeling, fietsen, water, uitzichtpunt, markt, terras/wijn, historie,
  overnachting), elk met de reden om er heen te gaan.
- **Over de reis** — beschrijving per fase met wat te doen.

## Reis in het kort
- **Heen (met de kinderen):** Champagne (2 nachten) → Sancerre → Marais Poitevin
  → strandweek Châtelaillon-Plage (La Rochelle).
- **Met z'n tweeën + hond Max:** San Sebastián (2 nachten, culinair) → Bilbao
  (tussenstop) → Picos de Europa (zwaartepunt, 6 nachten) → La Rioja → Bardenas →
  Olite/Irati → Ordesa (2 nachten, Cola de Caballo-hike).
- **Terug:** direct via Brive-la-Gaillarde → Reims → huis.

Alle bergpassen zijn getoetst op camper-geschiktheid (7 m / 2,9 m / 3.500 kg) en
alle POI's op hondvriendelijkheid.

## Bronnen / build
De kaart wordt gegenereerd door `build/build_trip.py` (routegeometrie in
`build/route_geo.js`, opgehaald via OSRM). Reisregels/POI-info via officiële
toerisme- en parkbronnen.

## Revisiehistorie
Bijgehouden via git. Elke wijziging aan de reis is een aparte commit.
