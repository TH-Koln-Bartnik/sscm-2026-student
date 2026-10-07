# UrbanRide bike data — worked example for the group project

These twelve tables describe the fictional bike maker UrbanRide: its product, its five-station line and the frame suppliers that feed it. Your group builds the same files, with the same column names, for your own product. Column meanings and units are in `data_dictionary.csv`.

| File | What it describes | For your project |
| --- | --- | --- |
| products.csv | The product and its price | Build your own |
| bom.csv | Parts per product, and where each enters the line | Build your own |
| workcenters.csv | Stations: servers, shifts, availability, variation, fixed cost | Build your own |
| routing.csv | Process time per station | Build your own |
| process_environment.csv | Electricity per station, running and idle | Build your own |
| suppliers.csv | Sourcing options for the key component | Build your own |
| locations.csv | Plant, suppliers, ports | Build your own |
| network_lanes.csv | Transport legs: distance, mode, transit time | Build your own |
| freight_rates.csv | Transport cost per leg | Build your own |
| transport_modes.csv | Truck, van, ship, rail | Reuse unchanged |
| transport_emission_factors.csv | g CO₂e per tonne-km per mode | Reuse unchanged |
| emission_factors.csv | Electricity and material factors | Reuse the electricity row; add your own material row |

The bike numbers are partly real and partly invented for teaching: the `source_*` and `class` columns in the emission tables show which. Your own numbers each need a row in `sources.csv`, as the project brief explains.
