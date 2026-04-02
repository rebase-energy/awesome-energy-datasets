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
| `Demand.ninja` | Daily temperature, heating degree days, and cooling degree days data spanning 1980-2022 for modelling heating and cooling energy demand in buildings at global scale. | 📈 | 🏠 🔌 | 📄 | 🌍 | [[url]](https://www.demand.ninja), [[code]](https://github.com/renewables-ninja/demand-ninja) |
| `MV-LV Networks` | Medium-voltage and low-voltage network models for distribution system studies. | 🗺️ 🏷️ | ⚡ | 📄 | 📍 | [[code]](https://github.com/Team-Nando/MV-LV-Networks) |
| `NVE Wind Power Generation Data` | Hourly power generation time series and metadata for 72 Norwegian wind parks (425 turbines), covering 1991-2023. | 🏷️ 📈 | 🌬️ | 📄 🗂️ | 🏳️ | [[url]](https://huggingface.co/datasets/rebase-energy/nve-windpower-data) |

## Contributing

To add a new dataset, add an entry to `data.json` and run `python main.py` to regenerate the README.
