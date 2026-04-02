# TODO: Add datasets to `data.json`

## Instructions for AI agent

Each task below represents a potential dataset to add to this repository. For each task:

1. **Visit the URL(s)** listed and research the dataset to understand what it contains.
2. **Skip the task** (mark with `[SKIP]` and a reason) if:
   - The link is dead or paywalled with no public data access.
   - It's not actually a dataset (e.g. a blog post, news article, or tool with no downloadable/queryable data).
   - It duplicates a dataset already in `data.json`.
3. **Add an entry to `data.json`** with the following structure:
   ```json
   {
     "name": "Short Descriptive Name",
     "description": "One sentence describing what the dataset contains.",
     "data_type": [],
     "energy_sector": [],
     "format": [],
     "coverage": [],
     "links": {
       "url": "primary dataset URL",
       "code": "github repo if applicable",
       "docs": "documentation URL if applicable",
       "api": "API endpoint if applicable"
     }
   }
   ```
4. **Category values must come from `mapping.json`**:
   - `data_type`: timeseries, geospatial, metadata, tabular
   - `energy_sector`: solar, wind, hydro, demand, price, weather, grid, fossil, nuclear, building, battery, transport
   - `format`: csv, parquet, api, json, excel, netcdf
   - `coverage`: global, continental, country, region, city, site
   - If a needed category value doesn't exist in `mapping.json`, add it there too with an appropriate emoji.
5. **After adding all entries**, run `python main.py` to regenerate the README.
6. **Mark each task as done** (`[x]`) after completing it.

---

## Tasks

### Solar datasets

- [ ] **UK Solar PV Dataset (Subak)** — https://data.subak.org/dataset/uk-solar-pv-dataset

- [ ] **Solar Power Datasets and Resources** — https://github.com/Charlie5DH/Solar-Power-Datasets-and-Resources

- [ ] **Ausgrid Solar Data** — https://pierreh.eu/ausgrid-solar-data/ and https://www.ausgrid.com.au/Industry/Our-Research/Data-to-share

- [ ] **UNISOLAR** — https://zenodo.org/records/10594108 and https://github.com/CDAC-lab/UNISOLAR

- [ ] **UK PV (Open Climate Fix)** — https://huggingface.co/datasets/openclimatefix/uk_pv

- [ ] **Global Inventory of Solar PV** — LinkedIn reference: https://www.linkedin.com/posts/lucaskruitwagen_a-global-inventory-of-photovoltaic-solar-activity-6859522872486977536-5ymu (find the actual Nature paper/dataset)

- [ ] **London PV Solar Panel Generation Data** — https://data.london.gov.uk/dataset/photovoltaic--pv--solar-panel-energy-generation-data

- [ ] **Solar Irradiance Data (Adam R. Jensen)** — LinkedIn reference: https://www.linkedin.com/posts/adamrjensen_need-free-solar-irradiance-data-for-your-activity-7126244905957437440-S1YB (find the actual data source)

### Wind datasets

- [ ] **Hill of Towie Wind Farm Open Dataset** — LinkedIn reference: https://www.linkedin.com/posts/alex-clerc_hill-of-towie-wind-farm-open-dataset-activity-7316140008791244800-LN8A (find the actual dataset URL)

- [ ] **Wind Turbines in Europe (OpenStreetMap)** — https://landgeist.com/2022/02/25/wind-turbines-in-europe/ (source: OpenStreetMap)

- [ ] **WindEurope Interactive Maps & Data** — https://windeurope.org/intelligence-platform/interactive-data-and-maps/

- [ ] **UK Wind Curtailment Monitor** — https://wind-curtailment-app-ahq7fucdyq-lz.a.run.app/ and methodology: https://wooden-knee-d53.notion.site/UK-Wind-Curtailment-Monitor-Methodology-71475d0b7cfd4edb97d6397b358f4118

- [ ] **4C Offshore Wind Map** — https://map.4coffshore.com/offshorewind/

### Grid & electricity datasets

- [ ] **JAO Static Grid Model** — https://www.jao.eu/static-grid-model

- [ ] **Energy Charts (Fraunhofer ISE)** — https://energy-charts.info/index.html?l=en&c=DE and map: https://energy-charts.info/map/map.htm?l=en&c=DE

- [ ] **EIA US Grid Monitor** — https://www.eia.gov/electricity/gridmonitor/dashboard/electric_overview/US48/US48

- [ ] **Dutch High-Voltage Grid Map** — https://webkaart.hoogspanningsnet.com/index2.php

- [ ] **Copper Sushi European Power Flow** — https://121gigawatts.org/copper-sushi-power-flow-european-grid/

- [ ] **Irish Smart Grid Dashboard (Frequency data)** — https://www.smartgriddashboard.com/

- [ ] **Open Grid Emissions (Singularity Energy)** — https://singularity.energy/open-grid-emissions

- [ ] **Swedish Reserve Market Data (SVK)** — https://www.svk.se/aktorsportalen/bidra-med-reserver/behov-av-reserver-nu-och-i-framtiden/utbud-pa-marknaderna-for-reserver/

- [ ] **Portugal Daily Electricity Balance (REN)** — https://datahub.ren.pt/en/electricity/daily-balance/

- [ ] **UK Energy Dashboard** — https://www.energydashboard.co.uk/data

- [ ] **Power Station Dictionary (OSUKED)** — https://github.com/OSUKED/Power-Station-Dictionary and https://osuked.github.io/Power-Station-Dictionary/index.html

- [ ] **Global Energy Monitor** — https://globalenergymonitor.org/

### Building & demand datasets

- [ ] **Smart Meter Heatmap (WPD)** — https://github.com/wpd-data/smart-meters

- [ ] **Thermal Properties of Building Materials** — https://vbn.aau.dk/en/publications/thermal-properties-of-building-materials-review-and-database

- [ ] **Building Energy Models Directory** — https://xiaoyujin97-building-data-directory-meta-directory-e3n6bv.streamlit.app/Building_Energy_Models

- [ ] **Microsoft Global ML Building Footprints** — https://github.com/microsoft/GlobalMLBuildingFootprints

- [ ] **Bing Maps Global Building Footprints** — https://blogs.bing.com/maps/2023-06/Bing-Maps-Global-Building-Footprints-released (may overlap with Microsoft dataset above — check)

- [ ] **Ecobee Building Data (LBNL)** — https://bbd.labworks.org/ds/bbd/ecobee

- [ ] **Home Series HVAC & Hot Water (LBNL)** — https://bbd.labworks.org/ds/bbd/hshus

- [ ] **Low-Voltage Load Forecasting Dataset** — https://low-voltage-loadforecasting.github.io/ and paper: https://arxiv.org/abs/2106.00006

- [ ] **HEDGE — Home Electricity Data Generator** — LinkedIn reference: https://www.linkedin.com/posts/flora-charbonnier-bevan-phd-398874107_home-electricity-data-generator-hedge-activity-7183858670936457219--opY (find the actual dataset/code)

- [ ] **Greybrick Buildings** — https://github.com/JulienLeprince/greybrickbuildings

### Weather & climate datasets

- [ ] **BARRA2 (Australian Weather Reanalysis)** — https://near.csiro.au/assets/42966a8f-bc3c-4bde-91d6-91bc5826aa21 and https://github.com/akarich73/barra2-dl

- [ ] **SECURES-Met (European Meteorological Data)** — LinkedIn reference: https://www.linkedin.com/posts/franziska-schoeniger-aa99a9126_secures-met-a-european-meteorological-data-activity-7106993451006607360-LQfE (find the actual dataset)

- [ ] **ClimaPower** — https://github.com/eantonini/climapower

### Price & market datasets

- [ ] **Swiss Electricity Prices (ElCom)** — https://www.prix-electricite.elcom.admin.ch/

- [ ] **Battery Charts (Germany)** — https://www.battery-charts.de/

### Storage & hydrogen datasets

- [ ] **H2 Infrastructure Map Europe** — https://www.h2inframap.eu/

- [ ] **Storage Lab Data** — https://www.storage-lab.com/data

- [ ] **BESS Analytics** — https://www.bessanalytics.com/

### Energy data portals & platforms

- [ ] **GEE Community Datasets (Google Earth Engine)** — https://github.com/samapriya/awesome-gee-community-datasets and https://gee-community-catalog.org/

- [ ] **Open Energy Platform** — https://openenergy-platform.org/

- [ ] **Icebreaker One / Open Energy** — https://icebreakerone.org/ and https://data.openenergy.org.uk/dataset-list

- [ ] **Realto API Marketplace** — https://realto.io/api-marketplace/

- [ ] **Denmark Energy Data (EnergyData.dk)** — https://energydata.dk/en/

- [ ] **Sweden Open Data Portal (Energy)** — https://www.dataportal.se/en/datasets?q=energy

- [ ] **Helen Open Data (Finland)** — https://www.helen.fi/en/company/responsibility/current-topics/open-data

- [ ] **COPED (Coventry Open Platform for Energy Data)** — https://coped.coventry.ac.uk/ and https://github.com/cogent-computing/COPED

- [ ] **PG&E Distribution Resource Planning Data** — https://www.pge.com/en_US/for-our-business-partners/distribution-resource-planning/distribution-resource-planning-data-portal.page

- [ ] **CO2 Monitor Netherlands** — https://co2monitor.nl/energiebronnen

- [ ] **Openmod Initiative** — https://openmod-initiative.org/

- [ ] **WattApp (Norway)** — https://www.wattapp.no/

### Research datasets (from Zenodo / papers)

- [ ] **Zenodo 14870023** — https://zenodo.org/records/14870023 (investigate what this dataset contains)

- [ ] **Zenodo 5946808** — https://zenodo.org/record/5946808 (investigate what this dataset contains)

- [ ] **Zenodo 5841834** — https://zenodo.org/record/5841834 (investigate what this dataset contains)

- [ ] **Nature Scientific Data paper (s41597-020-00739-0)** — https://www.nature.com/articles/s41597-020-00739-0 (investigate the associated dataset)

- [ ] **JOSS paper 3313** — https://joss.theoj.org/papers/10.21105/joss.03313 (investigate the associated dataset)

### Other / uncategorised

- [ ] **PowerTAC** — LinkedIn reference: https://www.linkedin.com/posts/ketter_powertac-energy-sustainability-activity-7133110807868919808-Dqop (find the actual data/platform)

- [ ] **Ember Open Data** — LinkedIn reference: https://www.linkedin.com/posts/dave-jones-ember_opendata-activity-7062065738911473664-VIin (find the actual dataset at ember-climate.org)

- [ ] **Energy Data Spaces (EU initiative)** — LinkedIn reference: https://www.linkedin.com/posts/nunosouzasilva_energy-data-spaces-current-results-of-the-activity-7161723739112513538-agL1 (find the actual data source)

- [ ] **Energy Storage Markets Europe** — LinkedIn reference: https://www.linkedin.com/posts/phillippa-c-rose-79bb2b92_energystoragemarkets-europe-energystorage-activity-7002971364227731457-bFfe (find the actual dataset)

- [ ] **Staffell Energy Modelling Data** — LinkedIn reference: https://www.linkedin.com/posts/iainstaffell_energy-modeling-sustainability-activity-7108336797809528832-OHFa (find the actual dataset)

- [ ] **Building Thermal Data (Hussain Kazmi)** — LinkedIn reference: https://www.linkedin.com/posts/hussain-kazmi_interpretable-domain-informed-and-domain-agnostic-activity-7185741221321973760-kk6j (find the actual dataset)
