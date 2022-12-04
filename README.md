# spotify_tracks

## Setup

```bash

# Set up a python virtual enivronment:
python3.10 -m venv venv

# Activate virtual environment.
. venv/bin/activate

# Update pip
pip install --upgrade pip

# Install necessary dependencies
pip install -r requirements.txt
```

This project has two objectives: 
1. Analyse the Spotify dataset and see what factors contribute towards the popularity of a track.
2. Build a prediction model which predicts whether or not a track will hit a high threshold of popularity. This threshold we speak of is a popularity of 64 or more, the 90th percentile of popularity in tracks released in and after 2012. 

Please look at EDA.ipynb for exploratory data analysis. 