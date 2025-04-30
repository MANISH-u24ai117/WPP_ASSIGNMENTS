import pandas as pd

# Sample schedule (you can change this as needed)
data = {
    'John': [True, False, True, False, True, True, False, False, True, False],
    'Judy': [True, False, True, True, False, True, False, True, False, False]
}

df = pd.DataFrame(data)

# Step 1: Party happens when both John and Judy are present
df['party'] = df['John'] & df['Judy']

# Step 2: Calculate days until next party
days_til_party = [None] * len(df)
next_party_day = None

for i in reversed(range(len(df))):
    if df.loc[i, 'party']:
        days_til_party[i] = 0
        next_party_day = i
    elif next_party_day is not None:
        days_til_party[i] = next_party_day - i
    else:
        days_til_party[i] = None  # No future party found yet

df['days_til_party'] = days_til_party

# Drop the intermediate 'party' column (optional)
df.drop(columns='party', inplace=True)

print(df)
