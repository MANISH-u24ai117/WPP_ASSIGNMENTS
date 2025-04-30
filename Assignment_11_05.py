import pandas as pd

# STEP 1: Sample dataset (replace this with your actual CSV or Excel read)
data = {
    'artist': ['A', 'A', 'B', 'A', 'B', 'C'],
    'venue': ['X', 'Y', 'X', 'X', 'Y', 'Z'],
    'date': pd.to_datetime([
        '2023-01-05', '2023-01-15', '2023-01-20',
        '2023-02-10', '2023-02-15', '2023-02-18'
    ])
}
df = pd.DataFrame(data)

# STEP 2: Define artist and venue series (you can customize this)
artists = pd.Series(['A', 'B', 'C'])
venues = pd.Series(['X', 'Y', 'Z'])

# STEP 3: Extract year-month
df['year_month'] = df['date'].dt.to_period('M').astype(str)

# STEP 4: Count concerts per (artist, venue, year_month)
grouped = df.groupby(['year_month', 'artist', 'venue']).size().reset_index(name='count')

# STEP 5: Cross product of all year_month, artists, and venues
artist_venue_pairs = pd.MultiIndex.from_product(
    [artists, venues], names=['artist', 'venue']
).to_frame(index=False)

year_months = pd.Series(df['year_month'].unique(), name='year_month')

full_index = pd.merge(
    year_months.to_frame(),
    artist_venue_pairs,
    how='cross'
)

# STEP 6: Merge and fill missing with 0
merged = pd.merge(
    full_index,
    grouped,
    on=['year_month', 'artist', 'venue'],
    how='left'
).fillna(0)

# STEP 7: Pivot to wide format
wide_table = merged.pivot_table(
    index='year_month',
    columns=['artist', 'venue'],
    values='count',
    fill_value=0
)

# Optional: Flatten column names
wide_table.columns = [f'{a}_{v}' for a, v in wide_table.columns]
wide_table = wide_table.reset_index()

# STEP 8: Show the result
print(wide_table)
