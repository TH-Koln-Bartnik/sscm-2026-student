# Refrigerator data (Liebherr CNc 5203, plant Ochsenhausen)

Same files and column names as the UrbanRide bike data. Every number we entered has one row in `sources.csv` (public, analogy or guesstimate). German version: `README_DE.md`.

| File | Content |
| --- | --- |
| products.csv | Liebherr CNc 5203, 69.7 kg, price 713.45 EUR net (list price 849 EUR / 1.19) |
| bom.csv | 8 parts; key component = compressor (added at WC3) |
| workcenters.csv, routing.csv | 6 stations; bottleneck is final assembly (WC3) |
| process_environment.csv | electricity per station; waste based on the Liebherr plant in Marica |
| suppliers.csv | SUP-CN Jiaxipera (China, by ship) and SUP-SK Embraco (Slovakia, by truck) |
| locations.csv, network_lanes.csv, freight_rates.csv | plant, suppliers, ports; Suez route and Cape route |
| transport_modes.csv, transport_emission_factors.csv | unchanged from the bike data |
| emission_factors.csv | electricity row from the bike data plus steel and the grids of China and Slovakia |

## Status (5 Nov 2026)

- Checkpoint passed: the official check cell v1.0 gives 5 of 5 PASS on these files.
- Station times in routing.csv are guesstimates. The Liebherr factory video was checked frame by frame, but no shot shows a full cycle, so the times cannot be read off it (see sources.csv).
- The three truck distances are from Google Maps (checked 2 Nov 2026).
- In bom.csv only the compressor has a `supplier_id`, exactly as in the bike data; the check cell allows this.
- Embraco Slovakia making household compressors today is an assumption, marked as such in sources.csv.
