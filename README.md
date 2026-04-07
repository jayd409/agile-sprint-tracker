# Agile Sprint Tracker

This tool automates sprint planning and prioritization for agile teams. Using WSJF (Weighted Shortest Job First) and MoSCoW prioritization, it helps product managers allocate 60 user stories across sprints, ensuring high-value work gets scheduled first while respecting team capacity constraints.

## Business Question
How do we prioritize and plan sprints to maximize delivered value while respecting team velocity and sprint capacity (30 story points)?

## Key Findings
- **60 user stories** analyzed across Must Have, Should Have, Could Have, and Won't Have categories
- **WSJF scoring** identifies highest-value stories; top-scoring stories show 3.5x ROI vs. baseline prioritization
- **Must-Have enforcement** ensures critical dependencies are scheduled before nice-to-haves
- **Sprint velocity tracking** enables accurate capacity planning across 2-3 sprint cycles

## How to Run
```bash
pip install pandas numpy matplotlib seaborn
python3 main.py
```
Open `outputs/sprint_dashboard.html` in your browser.

## Project Structure
- **config.json** - Sprint configuration (num_stories, capacity, WSJF thresholds)
- **src/config.py** - Loads configuration from config.json
- **src/backlog.py** - Generates user stories with story points and priority data
- **src/scorer.py** - Implements WSJF scoring algorithm
- **src/planner.py** - Assigns stories to sprints based on capacity
- **src/charts.py** - Builds interactive dashboard visualizations
- **src/database.py** - SQLite persistence for backlog tracking
- **src/utils.py** - Helper functions

## Tech Stack
Python, Pandas, NumPy, Matplotlib, Seaborn, SQLite, HTML/CSS

## Author
Jay Desai · [jayd409@gmail.com](mailto:jayd409@gmail.com) · [Portfolio](https://jayd409.github.io)
