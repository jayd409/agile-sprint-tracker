import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from utils import make_html

def build_dashboard(df):
    charts = []

    # 1. Story points per sprint
    fig, ax = plt.subplots(figsize=(9, 4))
    sprint_pts = df[df['sprint'] != 'Future Backlog'].groupby('sprint')['points'].sum().sort_index()
    ax.bar(range(len(sprint_pts)), sprint_pts.values, color='#3b82f6', alpha=0.7)
    ax.set_xticks(range(len(sprint_pts)))
    ax.set_xticklabels(sprint_pts.index, rotation=45)
    ax.set_ylabel('Story Points')
    ax.set_title('Story Points per Sprint')
    ax.axhline(30, color='red', linestyle='--', alpha=0.5, label='Capacity')
    ax.legend()
    charts.append(('Points per Sprint', fig))

    # 2. MoSCoW distribution (pie)
    fig, ax = plt.subplots(figsize=(7, 7))
    moscow_counts = df['moscow'].value_counts()
    colors_moscow = {'Must Have': '#ef4444', 'Should': '#f59e0b', 'Could': '#3b82f6', 'Won\'t': '#9ca3af'}
    ax.pie(moscow_counts.values, labels=moscow_counts.index, autopct='%1.0f%%',
           colors=[colors_moscow.get(label, '#ccc') for label in moscow_counts.index])
    ax.set_title('MoSCoW Distribution')
    charts.append(('MoSCoW Distribution', fig))

    # 3. Top 15 stories by WSJF
    fig, ax = plt.subplots(figsize=(9, 6))
    top15 = df.nlargest(15, 'wsjf')
    colors_moscow = {'Must Have': '#ef4444', 'Should': '#f59e0b', 'Could': '#3b82f6', 'Won\'t': '#9ca3af'}
    bar_colors = [colors_moscow.get(m, '#ccc') for m in top15['moscow']]
    ax.barh(range(len(top15)), top15['wsjf'].values, color=bar_colors)
    ax.set_yticks(range(len(top15)))
    ax.set_yticklabels(top15['story_id'].values)
    ax.set_xlabel('WSJF Score')
    ax.set_title('Top 15 Stories by WSJF Priority')
    charts.append(('Top Stories by WSJF', fig))

    # 4. Burndown chart Sprint 1
    fig, ax = plt.subplots(figsize=(9, 4))
    sprint1 = df[df['sprint'] == 'Sprint 1']
    total_pts = sprint1['points'].sum()
    days = np.arange(0, 15)
    ideal = np.linspace(total_pts, 0, len(days))
    rng = np.random.default_rng(42)
    noise = rng.normal(0, total_pts * 0.05, len(days))
    actual = np.maximum(0, ideal + noise)
    ax.plot(days, ideal, 'r--', label='Ideal', linewidth=2)
    ax.plot(days, actual, 'b-o', label='Actual', linewidth=2)
    ax.fill_between(days, actual, alpha=0.2)
    ax.set_xlabel('Days')
    ax.set_ylabel('Story Points Remaining')
    ax.set_title('Sprint 1 Burndown Chart')
    ax.legend()
    charts.append(('Sprint 1 Burndown', fig))

    # 5. Stories by epic
    fig, ax = plt.subplots(figsize=(9, 5))
    epic_counts = df['epic'].value_counts().sort_values(ascending=True)
    ax.barh(epic_counts.index, epic_counts.values, color='#8b5cf6')
    ax.set_xlabel('Number of Stories')
    ax.set_title('Stories by Epic')
    charts.append(('Stories by Epic', fig))

    # 6. Points distribution by moscow per sprint
    fig, ax = plt.subplots(figsize=(10, 5))
    sprints_active = df[df['sprint'] != 'Future Backlog']['sprint'].unique()
    moscow_order = ['Must Have', 'Should', 'Could']
    x = np.arange(len(sprints_active))
    width = 0.25
    for i, moscow in enumerate(moscow_order):
        pts = [df[(df['sprint'] == s) & (df['moscow'] == moscow)]['points'].sum() for s in sprints_active]
        ax.bar(x + i * width, pts, width, label=moscow)
    ax.set_xlabel('Sprint')
    ax.set_ylabel('Story Points')
    ax.set_title('Points Distribution by Priority per Sprint')
    ax.set_xticks(x + width)
    ax.set_xticklabels(sprints_active)
    ax.legend()
    charts.append(('Points by Moscow', fig))

    kpis = [
        ('Total Stories', f"{len(df)}"),
        ('Sprints', f"{df[df['sprint'] != 'Future Backlog']['sprint'].nunique()}"),
        ('Must-Haves', f"{(df['moscow'] == 'Must Have').sum()}"),
        ('Total Points', f"{df['points'].sum()}")
    ]

    html = make_html(charts, 'Agile Sprint Planner', kpis)
    with open('outputs/sprint_dashboard.html', 'w') as f:
        f.write(html)
