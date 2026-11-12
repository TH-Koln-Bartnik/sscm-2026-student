# Kühlschrank-Daten (Liebherr CNc 5203, Werk Ochsenhausen)

Gleiche Dateien und Spaltennamen wie die UrbanRide-Bike-Daten. Jede Zahl, die wir eingetragen haben, hat eine Zeile in `sources.csv` (public, analogy oder guesstimate). Englische Version: `README.md`.

| Datei | Inhalt |
| --- | --- |
| products.csv | Liebherr CNc 5203, 69,7 kg, Preis 713,45 EUR netto (UVP 849 EUR / 1,19) |
| bom.csv | 8 Teile; Key Component = Kompressor (kommt an WC3 dazu) |
| workcenters.csv, routing.csv | 6 Stationen; Engpass ist die Endmontage (WC3) |
| process_environment.csv | Strom je Station; Abfall nach dem Liebherr-Werk in Marica |
| suppliers.csv | SUP-CN Jiaxipera (China, per Schiff) und SUP-SK Embraco (Slowakei, per LKW) |
| locations.csv, network_lanes.csv, freight_rates.csv | Werk, Lieferanten, Häfen; Route über Suez und ums Kap |
| transport_modes.csv, transport_emission_factors.csv | unverändert aus den Bike-Daten |
| emission_factors.csv | Strom-Zeile aus den Bike-Daten plus Stahl und Strommix China und Slowakei |

## Stand (05.11.2026)

- Checkpoint bestanden: Die offizielle Check Cell v1.0 gibt auf diesen Dateien 5 von 5 PASS.
- Die Stationszeiten in routing.csv sind Schätzungen (guesstimate). Das Liebherr-Werksvideo wurde Bild für Bild geprüft, aber keine Szene zeigt einen kompletten Arbeitsgang, deshalb kann man die Zeiten dort nicht ablesen (siehe sources.csv).
- Die drei LKW-Entfernungen stammen aus Google Maps (geprüft am 02.11.2026).
- In bom.csv hat nur der Kompressor eine `supplier_id`, genau wie in den Bike-Daten; die Check Cell erlaubt das.
- Dass Embraco Slovakia heute Kompressoren für Haushaltsgeräte baut, ist eine Annahme und in sources.csv so markiert.
