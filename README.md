# Awesome Energy Datasets

A curated list of energy-relevant datasets for modelling tasks such as forecasting, simulation, and optimisation.

## Legend

**Data Type:** 📈 Timeseries · 🗺️ Geospatial · 🏷️ Metadata · 📊 Tabular

**Energy Sector:** ☀️ Solar · 🌬️ Wind · 💦 Hydro · 🔌 Demand · 💰 Price · 🌤️ Weather · ⚡ Grid · 🏭 Fossil · ☢️ Nuclear · 🏠 Building · 🔋 Battery · 🚗 Transport

**Format:** 📄 CSV · 🗂️ Parquet · 🔗 API · 📋 JSON · 📑 Excel · 🌐 NetCDF

**Coverage:** 🌍 Global · 🗺️ Continental · 🏳️ Country · 📍 Region · 🏙️ City · 📌 Site

## Datasets

| Name | Description | Data Type | Energy Sector | Format | Coverage | Links |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| `CO2 Monitor Netherlands` | National Energy Dashboard for the Netherlands providing hourly electricity production by source, gas consumption, and CO₂ emission intensity data from 2021 onward, jointly developed by Gasunie, TenneT, and partners. | 📈 | 🏭 ⚡ ☢️ ☀️ 🌬️ | 🔗 📋 | 🏳️ | [[url]](https://co2monitor.nl/energiebronnen), [[api]](https://nedapi.ned.nl) |
| `Common European Energy Data Space (CEEDS)` | EU initiative building a federated cross-border energy data space across Europe, coordinated through Horizon Europe projects (Enershare, Omega-X, EDDIE, DATA CELLAR, SYNERGIES) with pilots covering distributed energy resources, flexibility services, and smart EV charging in 10+ member states. | 🏷️ | 🏠 🔌 ⚡ 🚗 | 🔗 | 🗺️ | [[url]](https://enershare.eu/), [[docs]](https://energy.ec.europa.eu/publications/common-european-energy-data-space_en) |
| `Demand.ninja` | Daily temperature, heating degree days, and cooling degree days data spanning 1980-2022 for modelling heating and cooling energy demand in buildings at global scale. | 📈 | 🏠 🔌 | 📄 | 🌍 | [[url]](https://www.demand.ninja), [[code]](https://github.com/renewables-ninja/demand-ninja) |
| `diyepw` | Python package for generating Actual Meteorological Year (AMY) EnergyPlus weather files by merging TMY baselines with hourly observations from NOAA's Integrated Surface Database (ISD Lite), covering dry-bulb temperature, dew point, pressure, wind direction, and wind speed for WMO stations worldwide. | 📈 | 🏠 🌤️ | 📄 | 🌍 | [[url]](https://github.com/IMMM-SFA/diyepw), [[paper]](https://doi.org/10.21105/joss.03313) |
| `Ember Open Data` | Global yearly and monthly electricity data covering generation by fuel type, demand, capacity, imports, and power sector emissions for over 200 countries from 2000 to present, published by Ember. | 📊 📈 | 🔌 🏭 ⚡ 💦 ☢️ ☀️ 🌬️ | 🔗 📄 | 🌍 | [[url]](https://ember-energy.org/data/), [[docs]](https://ember-energy.org/data/data-tools/data-explorer/) |
| `EnergyData.dk (Denmark)` | Danish energy data hub operated by DTU providing real-time and historical datasets including smart meter electricity consumption, district heating supply, transformer station power measurements, building automation data, city battery operations, EV charging station data, weather station observations and forecasts, and CO₂ emissions from Danish electricity production, primarily covering Copenhagen's Nordhavn district and Bornholm island. | 📈 | 🔋 🏠 🔌 ⚡ 🚗 🌤️ | 🔗 📄 📋 | 🏳️ | [[url]](https://energydata.dk/en/), [[api]](https://admin.energydata.dk/api/v1), [[docs]](https://energydata.dk/en/dokumentation/api-documentation/) |
| `Helen Open Data (Finland)` | Hourly district heating power production data for Helsinki from 2015 to 2024, published by Helen Oy as downloadable CSV, with additional electricity, district cooling, and solar production data accessible via APIs on the Helen partner platform. | 📈 | 🔌 ⚡ ☀️ | 🔗 📄 | 🏙️ | [[url]](https://www.helen.fi/en/company/responsibility/current-topics/open-data), [[api]](https://open.helen.fi) |
| `Hill of Towie Wind Farm Data` | Operational data from the Hill of Towie wind farm (21 Siemens SWT-2.3-VS-82 turbines, 48.3 MW total) in Scotland, including over 8 years of 10-minute SCADA data and alarm logs from January 2016 through August 2024, turbine coordinates, static specifications, and shutdown duration calculations. | 🏷️ 📈 | 🌬️ | 📄 | 📌 | [[url]](https://zenodo.org/records/14870023), [[code]](https://github.com/resgroup/hill-of-towie-open-source-analysis) |
| `Kelmarsh Wind Farm Data` | Operational data from the Kelmarsh wind farm (six Senvion MM92 turbines, 12.3 MW total) in the UK, including 10-minute SCADA and events data from 2016 to mid-2021, turbine coordinates, static specifications, signal mappings, and substation meter readings. | 🏷️ 📈 | 🌬️ | 📄 | 📌 | [[url]](https://zenodo.org/records/5841834) |
| `MV-LV Networks` | Medium-voltage and low-voltage network models for distribution system studies. | 🗺️ 🏷️ | ⚡ | 📄 | 📍 | [[code]](https://github.com/Team-Nando/MV-LV-Networks) |
| `NVE Wind Power Generation Data` | Hourly power generation time series and metadata for 72 Norwegian wind parks (425 turbines), covering 1991-2023. | 🏷️ 📈 | 🌬️ | 📄 🗂️ | 🏳️ | [[url]](https://huggingface.co/datasets/rebase-energy/nve-windpower-data) |
| `Penmanshiel Wind Farm Data` | Operational data from the Penmanshiel wind farm (14 Senvion MM82 turbines, 28.7 MW total) in Scotland, including 10-minute SCADA and events data from 2016 to mid-2021, turbine coordinates, static specifications, signal mappings, and grid connection phasor measurement unit readings. | 🏷️ 📈 | 🌬️ | 📄 | 📌 | [[url]](https://zenodo.org/records/5946808) |
| `PG&E Distribution Resource Planning Data` | PG&E's Grid Resource Integration Portal (GRIP) providing hosting capacity, load forecasts, and grid needs assessments for distributed energy resource planning across PG&E's California service territory. | 🗺️ 📊 | 🔋 ⚡ ☀️ | 📄 | 📍 | [[url]](https://www.pge.com/en/about/doing-business-with-pge/interconnections/distributed-resource-planning-data-and-maps.html) |
| `PowerTAC` | Open-source competitive simulation platform for retail electricity markets where autonomous broker agents trade in wholesale markets, manage tariffs, and balance supply and demand, producing detailed game logs with market transactions, customer behaviour, weather, and grid operations data. | 📊 📈 | 🔌 💰 ☀️ 🌬️ | 📄 | 🌍 | [[url]](https://powertac.org), [[code]](https://github.com/powertac) |
| `STOREtrack` | Database of over 4,000 energy storage projects across 29 European countries, tracking project specifications, timelines, technology types, and key stakeholders. | 🗺️ 📊 | 🔋 | 📄 | 🗺️ | [[url]](https://www.lcp.com/en/energy-transition/technology/enact/storetrack) |
| `Sweden Open Data Portal (Energy)` | Sweden's national open data portal aggregating energy datasets from the Swedish Energy Agency and Statistics Sweden, covering energy balances, supply and consumption by sector and commodity, renewable and fossil fuel shares, electricity production, district heating and cooling, building energy use, transport energy, grid-connected batteries, and energy indicators from 1970 onward. | 📊 📈 | 🏠 🔌 🏭 ⚡ 💦 ☢️ ☀️ 🚗 🌬️ | 🔗 📋 | 🏳️ | [[url]](https://www.dataportal.se/en/datasets?q=energy), [[api]](https://pxexternal.energimyndigheten.se/pxweb/en/Energimyndighetens_statistikdatabas/) |
| `UKPVGeo` | Crowdsourced geographic dataset of over 260,000 solar PV installations across the UK, covering approximately 86% of installed capacity (10.66 GW mapped, 13.93 GW inferred), with location coordinates and capacity metadata for both domestic rooftop and utility-scale solar farms. | 🗺️ 🏷️ | ☀️ | 📄 📋 | 🏳️ | [[url]](https://zenodo.org/records/4059881), [[code]](https://github.com/openclimatefix/solar-power-mapping-data), [[paper]](https://doi.org/10.1038/s41597-020-00739-0) |
| `WattApp` | Interactive map of available transformer capacity across Norway's electricity grid, developed by Elbits++ in collaboration with multiple Norwegian grid companies, showing over 680 locations where new consumption or production facilities can connect to the network. | 🗺️ 🏷️ | ⚡ | 🔗 | 🏳️ | [[url]](https://www.wattapp.no/) |

## Contributing

To add a new dataset, add an entry to `data.json` and run `python main.py` to regenerate the README.
