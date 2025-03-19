# GeoRisk

Flood Risk assessment based on The Meteorological Service of Canada (MSC) data center


## Structure:

- `core/`: Core functionality for the flood risk assessment
- `docs/`: test notebooks with workable examples
- `README.md`: This file

## Installation:

```bash
pip install -r requirements.txt
```

## Thinking out loud:

- What I want to try and do is build out a cell grid where each cell is the location on a map. Each cell then contains the following data:
    - Elevation
    - Date
    - Current water accumulation (based on previous 5 days of precipitation)
- Then I want to use regression to predict the water accumulation for the next day based on the data above.
- I want to do this for each cell in the grid.
    - In this way the direction of flow is already built into the model. and physics modeling isn't really needed.