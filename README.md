Champions League-Level Player Discovery ⚽📊

A football scouting analytics project designed to identify non-Champions League players with statistical profiles similar to Champions League-level players across Europe’s top 5 leagues.

The goal is to simulate a modern data-driven recruitment engine used by football clubs to discover undervalued or overlooked talent outside elite European competitions.

⸻

Project Objective

Football clubs competing at the highest level often search for players capable of performing at Champions League intensity.

This project aims to answer the following question:

Which non-UCL players show statistical profiles similar to established Champions League players?

Using player statistics from Europe’s top 5 leagues, the project builds a similarity-based scouting engine capable of identifying realistic recruitment targets based on role-specific performance metrics.

⸻

Dataset

Primary Dataset

Source: FBref (Top 5 European Leagues)

Season:

* 2025/2026

Competitions:

* Premier League
* La Liga
* Serie A
* Bundesliga
* Ligue 1

Included statistics:

* Goals
* Assists
* Shots
* Shots on Target
* Goal Efficiency
* Playing Time
* Appearances
* Defensive Metrics
* Goalkeeping Metrics

⸻

Dataset Enrichment

A secondary football dataset was integrated to enrich the FBref data with advanced attacking metrics.

The enrichment process included:

* Player name normalization
* Cross-dataset entity matching
* Dataset merging
* Missing value handling

Additional metrics added:

* Expected Goals (xG)
* Expected Assists (xA)

Coverage after matching:

* xG available for ~73% of players
* xA available for ~84% of players

⸻

Methodology

1. Data Filtering

To improve statistical reliability, players with insufficient playing time are excluded.

Current thresholds:

* Minimum appearances: 15
* Minimum minutes played: 900

⸻

2. Role-Based Segmentation

Players are grouped by tactical role.

Current implementation:

* Strikers (FW)

Future extensions:

* Wingers
* Midfielders
* Defensive Midfielders
* Fullbacks
* Centre-backs
* Goalkeepers

⸻

3. Feature Engineering

The project uses per90 metrics to compare player profiles independently from total minutes played.

Current striker features:

* Goals per90
* Assists per90
* Shots per90
* Shots on Target per90
* Goal Conversion Efficiency (G/Sh)
* Expected Goals per90 (xG/90)
* Expected Assists per90 (xA/90)

⸻

4. Feature Scaling

All numerical features are standardized using StandardScaler from scikit-learn.

This prevents high-volume statistics from dominating the similarity calculation.

⸻

5. Similarity Engine

The project uses:

* NearestNeighbors
* Euclidean Distance
* Similarity Scoring

to identify statistically similar players.

⸻

6. Recruitment Constraints

To make recommendations more realistic, the engine applies additional recruitment filters:

* Champions League club exclusion
* Age-based filtering
* Minimum playing time requirements

This transforms the engine from a pure similarity model into a recruitment-oriented scouting tool.

⸻

Similarity Engine Evolution

Version 1

Features:

* Goals per90
* Assists per90
* Shots per90
* Shots on Target per90
* Goal Efficiency

Objective:

* Find statistically similar players using basic attacking output.

⸻

Version 2

Additional Features:

* xG per90
* xA per90

Objective:

* Capture underlying attacking performance rather than only final output.

⸻

Version 3

Additional Constraints:

* Age filtering
* Non-UCL filtering

Objective:

* Identify realistic transfer targets rather than purely similar players.

⸻

Example Use Case

Benchmark Player

Julián Álvarez (Atlético Madrid)

Objective

Find statistically similar strikers who are NOT currently playing for Champions League clubs.

Example Outputs

* Rômulo (RB Leipzig)
* Ragnar Ache (Köln)
* Akor Adams (Sevilla)
* Nico Williams (Athletic Club)
* Florian Thauvin (Lens)

Each recommendation includes:

* Playing time
* Goal production
* Chance creation
* xG / xA profile
* Similarity score

⸻

Example Radar Comparison

Julián Álvarez vs Ragnar Ache

⸻

Hidden Gems Discovery

The project includes a hidden gems discovery engine designed to identify young, non-Champions League players with strong attacking production and sufficient playing time.

Selection criteria:

* Not playing for a Champions League club
* Age ≤ 24
* Minimum playing time threshold
* Ranked using a custom scouting score

Example hidden gems:

Player	Club	League
Rômulo	RB Leipzig	Bundesliga
Karl Etta Eyong	Levante	La Liga
Emersonn	Toulouse	Ligue 1

⸻

Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Jupyter Notebook
* Git
* GitHub

⸻

Repository Structure

champions-league-player-discovery/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_collection.ipynb
│   ├── 02_similarity_engine.ipynb
│   ├── 03_visualizations.ipynb
│   └── 04_dataset_enrichment.ipynb
│
├── src/
│   ├── __init__.py
│   ├── data_utils.py
│   ├── scouting_score.py
│   ├── similarity_engine.py
│   └── similarity_engine_v2.py
│
├── images/
│
├── README.md
│
└── requirements.txt

⸻

Project Roadmap

Version 1.0

* Data collection
* Similarity engine
* Scouting score
* Hidden gems discovery
* Radar chart visualizations

Version 2.0

* Dataset enrichment
* xG integration
* xA integration
* Similarity Engine V2

Version 3.0

* Age-adjusted scouting
* Non-UCL filtering
* Recruitment-oriented recommendations

Future Improvements

* Midfielder scouting engine
* Defender scouting engine
* Progressive carries and progressive passes
* Similarity explainability
* Streamlit dashboard
* Automated weekly updates

⸻

Long-Term Vision

The long-term objective is to evolve this project into a complete football recruitment analytics platform capable of supporting:

* Scouting Departments
* Recruitment Analysts
* Performance Analysts
* Football Data Enthusiasts

⸻

Author

Pietro Miragoli

MSc in Data Science & Management — LUISS Guido Carli

Interested in:

* Sports Analytics
* Machine Learning
* Football Scouting
* Recommendation Systems
* AI Applications in Sports