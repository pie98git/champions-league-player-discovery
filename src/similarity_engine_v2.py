def find_similar_non_ucl_players_v3(
    player_name,
    df,
    model,
    scaler,
    feature_columns,
    ucl_teams,
    n_neighbors=30,
    age_range=3
):
    target_player = df[df["Player"] == player_name]

    if target_player.empty:
        raise ValueError(f"Player '{player_name}' not found.")

    target_index = target_player.index[0]
    target_age = target_player["Age"].iloc[0]

    player_features = df.loc[
        target_index,
        feature_columns
    ].values.reshape(1, -1)

    player_features_scaled = scaler.transform(player_features)

    distances, indices = model.kneighbors(
        player_features_scaled,
        n_neighbors=n_neighbors + 1
    )

    similar_players = df.iloc[indices[0][1:]].copy()
    similar_players["distance"] = distances[0][1:]
    similar_players["similarity_score"] = 100 / (1 + similar_players["distance"])

    similar_players["is_ucl_team"] = similar_players["Squad"].isin(ucl_teams)

    similar_players = similar_players[
        similar_players["is_ucl_team"] == False
    ].copy()

    similar_players = similar_players[
        similar_players["Age"].between(
            target_age - age_range,
            target_age + age_range
        )
    ].copy()

    return similar_players.sort_values("similarity_score", ascending=False)