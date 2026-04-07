def score_wsjf(df):
    """Calculate WSJF (Weighted Shortest Job First) score"""
    df = df.copy()
    df['cost_of_delay'] = df['business_value'] + df['time_criticality'] + df['risk_reduction']
    df['wsjf'] = (df['cost_of_delay'] / df['points']).round(2)
    df['priority_rank'] = df['wsjf'].rank(ascending=False, method='dense').astype(int)
    return df.sort_values('priority_rank')
