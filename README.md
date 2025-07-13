# NZ Electricity Time Series Analysis

## Project Overview
Interactive dashboard analyzing 50 years of electricity system data (1974-2024) including:
- Generation by source
- Transmission losses
- Consumption patterns

## Features
- **Interactive Visualizations**: Plotly-powered charts with dropdown filters
- **Time Series Analysis**: Explore trends across decades
- **Data Export**: Download cleaned datasets in CSV format
- **Reproducible Analysis**: Jupyter Notebook + Python

## Data Sources
| Data tables for electricity [XLSX, 313 KB] | https://www.mbie.govt.nz/building-and-energy/energy-and-natural-resources/energy-statistics-and-modelling/energy-statistics/electricity-statistics |

## Installation
```bash
git clone https://github.com/xzo-cs/nz-electricity-statistics.git
cd nz-electricity-statistics

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # If Linux or Mac
# .venv\Scripts\activate  # If Windows

# Install requirements
pip install -r requirements.txt
