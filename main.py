import sys, os
sys.path.insert(0, 'src')
os.makedirs('outputs', exist_ok=True)

from config import config
from backlog import make_backlog
from scorer import score_wsjf
from planner import assign_sprints
from charts import build_dashboard
from database import save_to_db, query

df = make_backlog(config['num_stories'])
df = score_wsjf(df)
df = assign_sprints(df, capacity=config['sprint_capacity'])

print("Agile Sprint Planner")
print(f"  Stories      : {len(df)}")
print(f"  Sprints      : {df[df['sprint'] != 'Future Backlog']['sprint'].nunique()}")

must = df[df['moscow'] == 'Must Have']
sprint1 = df[df['sprint'] == 'Sprint 1']
print(f"  Must-Haves   : {len(must)}")
print(f"  Sprint 1 pts : {sprint1['points'].sum()}")

save_to_db(df, 'sprint_backlog')

print("\n--- SQL Analytics (SQLite) ---")
# Stories by sprint
r1 = query("SELECT sprint, COUNT(*) as stories, SUM(points) as total_points FROM sprint_backlog GROUP BY sprint ORDER BY sprint")
print("Sprint Breakdown:")
print(r1.to_string(index=False))
# MoSCoW distribution
r2 = query("SELECT moscow, COUNT(*) as count, SUM(points) as total_points FROM sprint_backlog GROUP BY moscow ORDER BY count DESC")
print("\nMoSCoW Distribution:")
print(r2.to_string(index=False))
# Top scoring stories by WSJF
r3 = query("SELECT story_id, title, moscow, points, wsjf FROM sprint_backlog ORDER BY wsjf DESC LIMIT 5")
print("\nTop 5 Stories by WSJF:")
print(r3.to_string(index=False))

df.to_csv('outputs/sprint_plan.csv', index=False)
build_dashboard(df)
print("\nDone — open outputs/sprint_dashboard.html")
