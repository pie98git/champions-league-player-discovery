import sys
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
import streamlit as st
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

from src.similarity_engine_v2 import find_similar_non_ucl_players_v3


st.set_page_config(
    page_title="Football Scouting Engine",
    layout="wide"
)

st.title("⚽ Football Scouting Engine")

st.write(
    "Discover statistically similar players across Europe's Top 5 Leagues."
)

df = pd.read_csv(
    ROOT / "data" / "processed" / "enhanced_player_dataset_v2.csv"
)

ucl_teams = [
    "Arsenal", "Atlético Madrid", "Barcelona", "Bayern Munich",
    "Borussia Dortmund", "Inter", "Juventus", "Leverkusen",
    "Liverpool", "Manchester City", "Milan", "Monaco", "Napoli",
    "Newcastle Utd", "Paris S-G", "Real Madrid", "Tottenham"
]

advanced_features = [
    "Gls_per90",
    "Ast_per90",
    "Sh_per90",
    "SoT_per90",
    "G/Sh",
    "xG_per90",
    "xA_per90"
]

df["Gls_per90"] = df["Gls"] / df["90s"]
df["Ast_per90"] = df["Ast"] / df["90s"]
df["Sh_per90"] = df["Sh"] / df["90s"]
df["SoT_per90"] = df["SoT"] / df["90s"]

df["xG_per90"] = df["expected_goals"] / df["90s"]
df["xA_per90"] = df["expected_assists"] / df["90s"]

df = df.replace([float("inf"), -float("inf")], pd.NA)

df = df.dropna(subset=advanced_features).copy()

X = df[advanced_features]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = NearestNeighbors(
    n_neighbors=30,
    metric="euclidean"
)

model.fit(X_scaled)

st.subheader("Player Selection")

player = st.selectbox(
    "Choose a player",
    sorted(df["Player"].dropna().unique())
)

age_range = st.slider(
    "Age range",
    min_value=1,
    max_value=8,
    value=3
)

def create_radar_chart(target_player, comparison_player, df, features):
    target = df[df["Player"] == target_player].iloc[0]
    comparison = df[df["Player"] == comparison_player].iloc[0]

    target_values = target[features].values.astype(float).tolist()
    comparison_values = comparison[features].values.astype(float).tolist()

    target_values += target_values[:1]
    comparison_values += comparison_values[:1]

    angles = np.linspace(
        0,
        2 * np.pi,
        len(features),
        endpoint=False
    ).tolist()

    angles += angles[:1]

    fig, ax = plt.subplots(
        figsize=(6, 6),
        subplot_kw=dict(polar=True)
    )

    ax.plot(angles, target_values, linewidth=2, label=target_player)
    ax.fill(angles, target_values, alpha=0.25)

    ax.plot(angles, comparison_values, linewidth=2, label=comparison_player)
    ax.fill(angles, comparison_values, alpha=0.25)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(features)

    ax.set_title(f"{target_player} vs {comparison_player}")
    ax.legend(loc="upper right")

    return fig

if st.button("Find Similar Non-UCL Players"):
    results = find_similar_non_ucl_players_v3(
        player,
        df,
        model,
        scaler,
        advanced_features,
        ucl_teams,
        n_neighbors=30,
        age_range=age_range
    )

    results = results.head(5).copy()

    results["Similarity %"] = (
        results["similarity_score"]
        .round(1)
    )

    st.subheader(f"Recommended replacements for {player}")

    display_columns = [
        "Player",
        "Squad",
        "Age",
        "Similarity %",
        "Gls_per90",
        "Ast_per90",
        "xG_per90",
        "xA_per90"
    ]

    st.dataframe(
        results[display_columns],
        hide_index=True
    )
    st.subheader("Radar Comparison")

    comparison_player = st.selectbox(
        "Choose a recommended player for radar comparison",
        results["Player"].tolist()
    )

    radar_fig = create_radar_chart(
        player,
        comparison_player,
        df,
        advanced_features
    )

    st.pyplot(radar_fig)
