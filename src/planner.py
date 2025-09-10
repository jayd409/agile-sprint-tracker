import numpy as np
import pandas as pd

def assign_sprints(df, capacity=30):
    """Assign stories to sprints based on WSJF priority"""
    df = df.copy()
    df = df[df['moscow'] != 'Won\'t'].reset_index(drop=True)
    df = df.sort_values('priority_rank').reset_index(drop=True)

    sprints = []
    current_sprint = 1
    current_capacity = 0

    for idx, row in df.iterrows():
        if current_capacity + row['points'] > capacity and current_sprint < 6:
            current_sprint += 1
            current_capacity = 0
        elif current_sprint >= 6:
            current_sprint = 7  # Future backlog

        sprints.append(f'Sprint {current_sprint}' if current_sprint < 7 else 'Future Backlog')
        current_capacity += row['points']

    df['sprint'] = sprints

    # Add burndown simulation for Sprint 1
    sprint1_df = df[df['sprint'] == 'Sprint 1'].copy()
    total_pts = sprint1_df['points'].sum()
    days = np.arange(0, 15)
    ideal_line = np.linspace(total_pts, 0, len(days))
    rng = np.random.default_rng(42)
    noise = rng.normal(0, total_pts * 0.05, len(days))
    actual_line = np.maximum(0, ideal_line + noise)
    df['_ideal'] = None
    df['_actual'] = None
    df.loc[df['sprint'] == 'Sprint 1', '_ideal'] = 0
    df.loc[df['sprint'] == 'Sprint 1', '_actual'] = 0

    return df
