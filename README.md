# Champions League-Level Player Discovery ⚽📊

A football scouting analytics project designed to identify non-Champions League players with statistical profiles similar to Champions League-level players across Europe's top 5 leagues.

The goal is to simulate a modern data-driven recruitment engine used by football clubs to discover undervalued or overlooked talent outside elite European competitions.

---

# Project Objective

Football clubs competing at the highest level often search for players capable of performing at Champions League intensity.

This project aims to answer the following question:

> Which non-UCL players show statistical profiles similar to established Champions League players?

Using player statistics from Europe's top 5 leagues, the project builds a similarity-based scouting engine capable of identifying hidden recruitment targets based on role-specific performance metrics.

---

# Dataset

Source: FBref (Top 5 European Leagues)

Season:
- 2025/2026

Dataset includes:
- Premier League
- La Liga
- Serie A
- Bundesliga
- Ligue 1

Player statistics:
- Goals
- Assists
- Shots
- Shots on Target
- Goal efficiency
- Playing time
- Appearances
- Goalkeeping and defensive metrics (future extensions)

The dataset is updated weekly.

---

# Methodology

## 1. Data Filtering

To improve statistical reliability, players with insufficient playing time are excluded.

Current thresholds:
- Minimum appearances: 15
- Minimum minutes played: 900

---

## 2. Role-Based Segmentation

Players are grouped by tactical role.

Current implementation:
- Strikers (FW)

Future extensions:
- Wingers
- Midfielders
- Defensive midfielders
- Fullbacks
- Centre-backs
- Goalkeepers

---

## 3. Feature Engineering

The project uses per90 metrics to compare player profiles independently from total minutes played.

Current striker features:
- Goals per90
- Assists per90
- Shots per90
- Shots on target per90
- Goal conversion efficiency (G/Sh)

---

## 4. Feature Scaling

All numerical features are standardized using `StandardScaler` from scikit-learn.

This prevents high-volume statistics from dominating the similarity calculation.

---

## 5. Similarity Engine

The project uses:
- `NearestNeighbors`
- Euclidean distance
- Similarity scoring

to identify statistically similar players.

---

# Example Use Case

## Benchmark Player
Julián Álvarez (Atlético Madrid)

## Objective
Find statistically similar strikers who are NOT currently playing for Champions League clubs.

## Example Outputs
- Ragnar Ache (Köln)
- Akor Adams (Sevilla)
- Rafael Leão (Milan)
- Andrea Pinamonti (Sassuolo)
- Emersonn (Toulouse)

Each recommendation includes:
- appearances
- minutes played
- attacking production
- similarity score

---

# Technologies Used

- Python
- Pandas
- NumPy
- scikit-learn
- Jupyter Notebook
- Git
- GitHub

---

# Repository Structure

```bash
champions-league-player-discovery/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│
├── src/
│
├── images/
│
├── README.md
│
└── requirements.txt
```

---

# Future Improvements

Planned future developments include:

- Advanced FBref metrics (xG, xA, progressive carries, progressive passes)
- Market value integration
- Age-adjusted scouting
- Position-specific archetypes
- Automated weekly data updates
- Streamlit interactive scouting dashboard
- Radar charts and visual player comparisons
- Similarity explanations and feature importance

---

# Long-Term Vision

The long-term objective is to evolve this project into a complete football recruitment analytics platform capable of supporting:
- scouting departments
- recruitment analysts
- performance analysts
- football data enthusiasts

---

# Author

Pietro Miragoli

MSc in Data Science & Management — LUISS Guido Carli

Interested in:
- Sports Analytics
- Machine Learning
- Football Scouting
- Recommendation Systems
- AI Applications in Sports