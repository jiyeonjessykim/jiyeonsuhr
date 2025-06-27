import pandas as pd

file_name = 'Problems we tackle, Shift Offers v3 .csv'
pd.set_option('display.max_columns', None)


# Read the CSV file into a pandas DataFrame

try:
    df = pd.read_csv(file_name)
    print("Data loaded successfully!")
    print("Total Number of records:", len(df))
    print("\n----- Data Preview (First 5 Rows) -----")
    print(df.head())

except FileNotFoundError:
    print(f"Error: '{file_name}' not found.")


# Check basic information about the data

print("\n----- Basic Data Information -----")
df.info()


# Convert date/time columns

date_columns = ['SHIFT_START_AT', 'SHIFT_CREATED_AT', 'OFFER_VIEWED_AT', 'CLAIMED_AT', 'DELETED_AT', 'CANCELED_AT']

for col in date_columns:
    df[col] = pd.to_datetime(df[col], errors='coerce')


# Convert boolean-like columns
df['IS_NCNS'] = df['IS_NCNS'].astype(bool)


# Create new columns for analysis
df['IS_BOOKED'] = df['CLAIMED_AT'].notna()

# Calculate Lead Time: the time between when a shift is booked and when it starts
df['LEAD_TIME_HOURS'] = (df['SHIFT_START_AT'] - df['CLAIMED_AT']).dt.total_seconds() / 3600                         


# Get the weekday of the shift start (Monday=0, Sunday=6)
df['SHIFT_WEEKDAY'] = df['SHIFT_START_AT'].dt.weekday


print("\n----- Data Cleaning and Feature Engineering Complete! -----")
print("New columns like 'IS_BOOKED' and 'LEAD_TIME_HOURS' have been added.")
print(df[['SHIFT_ID', 'CLAIMED_AT', 'IS_BOOKED', 'LEAD_TIME_HOURS']].head())



# --- Analysis 1: NCNS (No-Call No-Show) Rate by Workplace ---
print("\n\n===== Analysis 1: NCNS Rate by Workplace =====")


# 1. Filter for booked shifts only
booked_shifts = df[df['IS_BOOKED'] == True].copy()


# 2. Group by workplace and calculate total bookings and NCNS counts
workplace_analysis = booked_shifts.groupby('WORKPLACE_ID').agg(
    total_bookings=('IS_BOOKED', 'count'),
    ncns_count=('IS_NCNS', 'sum')
).reset_index()


# 3. Calculate the NCNS rate in percent
workplace_analysis['NCNS_RATE'] = (workplace_analysis['ncns_count'] / workplace_analysis['total_bookings']) * 100


# 4. Filter for workplaces with a meaningful number of bookings (e.g., >= 20) for statistical significance
reliable_analysis = workplace_analysis[workplace_analysis['total_bookings'] >= 20]


# 5. Sort by NCNS_RATE in descending order to find the top 10
top_10_ncns_workplaces = reliable_analysis.sort_values(by='NCNS_RATE', ascending=False).head(10)


print("Top 10 Workplaces with Highest NCNS Rate (min. 20 bookings):")
print(top_10_ncns_workplaces)



# --- Analysis 2: Relationship between Pay Rate and Booking Lead Time ---
print("\n\n===== Analysis 2: Pay Rate vs. Lead Time =====")


# Use only data with a non-negative lead time (booked before the shift started)
valid_lead_time_df = df[df['LEAD_TIME_HOURS'] >= 0].copy()


# 1. Bin the pay rates into $5 intervals (e.g., $20-$25, $25-$30)
valid_lead_time_df['PAY_RATE_BIN'] = pd.cut(valid_lead_time_df['PAY_RATE'], bins=range(15, 50, 5), right=False)


# 2. Calculate the average lead time for each pay rate bin
rate_vs_lead_time = valid_lead_time_df.groupby('PAY_RATE_BIN')['LEAD_TIME_HOURS'].mean().reset_index()


print("Average Booking Lead Time (in hours) by Pay Rate Bin:")
print(rate_vs_lead_time)



# --- Analysis 3: The Shift Failure Profile Analysis ---
print("\n\n===== Analysis 3: The Shift Failure Profile Analysis =====")

# --- Step 1: Advanced Feature Engineering ---

# 1. Explicitly define all "Failure Types"
df['IS_FACILITY_CANCELED'] = df['DELETED_AT'].notna() & df['IS_BOOKED']
df['IS_WORKER_CANCELED'] = df['CANCELED_AT'].notna()


# 2. 'Posting Lead Time': How urgently did the facility post the shift?
df['POSTING_LEAD_TIME_HOURS'] = (df['SHIFT_START_AT'] - df['SHIFT_CREATED_AT']).dt.total_seconds() / 3600


# 3. 'Booking Lead Time': How close to the start time did the worker book?
df['BOOKING_LEAD_TIME_HOURS'] = (df['SHIFT_START_AT'] - df['CLAIMED_AT']).dt.total_seconds() / 3600


# 4. 'Is Late Worker Cancellation?': A critical metric. Did they cancel within 24h of the shift start?
df['IS_LATE_WORKER_CANCELLATION'] = ((df['SHIFT_START_AT'] - df['CANCELED_AT']).dt.total_seconds() / 3600) < 24


# 5. Bin continuous variables to make grouping easier
# Duration Bins
df['DURATION_BIN'] = pd.cut(df['DURATION'], bins=[0, 6, 10, 24], labels=['Short (<=6h)', 'Medium (6-10h)', 'Long (>10h)'])


# Booking Lead Time Bins
df['BOOKING_LEAD_TIME_BIN'] = pd.cut(df['BOOKING_LEAD_TIME_HOURS'], bins=[-1, 8, 24, 168, df['BOOKING_LEAD_TIME_HOURS'].max()], labels=['Last-Minute (<8h)', 'Same-Day (8-24h)', 'Week (1-7d)', 'Advance (>7d)'])

# Posting Lead Time Bins
df['POSTING_LEAD_TIME_BIN'] = pd.cut(df['POSTING_LEAD_TIME_HOURS'], bins=[-1, 24, 168, df['POSTING_LEAD_TIME_HOURS'].max()], labels=['Urgent (<1d)', 'Week (1-7d)', 'Planned (>7d)'])


print("/n Advanced features created successfully!")
          

# Analysis is only meaningful for shifts that were actually booked.
booked_df = df[df['IS_BOOKED'] == True].copy()


# --- Step 2: Hypothesis Testing Deep Dive ---
# --- When and Why Do No-Shows (NCNS) Happen? ---
print("\n===== Deep Dive: Analyzing No-Call No-Shows (NCNS) =====")


# Hypothesis 1: Does the shift slot affect the NCNS rate?
print("\n--- NCNS Rate by Shift Slot ---")
print(booked_df.groupby('SLOT')['IS_NCNS'].mean().sort_values(ascending=False))


# Hypothesis 2: Is duration a factor? (e.g., workers give up on longer shifts)
print("\n--- NCNS Rate by Shift Duration ---")
print(booked_df.groupby('DURATION_BIN')['IS_NCNS'].mean().sort_values(ascending=False))


# Hypothesis 3: Do lower pay rates lead to more no-shows?
print("\n--- NCNS Rate by Pay Rate ---")
booked_df['PAY_RATE_BIN'] = pd.cut(booked_df['PAY_RATE'], bins=range(10, 51, 10))
print(booked_df.groupby('PAY_RATE_BIN', observed=True)['IS_NCNS'].mean().sort_values(ascending=False))


# Hypothesis 4: Are 'last-minute' bookings more likely to be no-shows?
print("\n--- NCNS Rate by Booking Lead Time ---")
print(booked_df.groupby('BOOKING_LEAD_TIME_BIN')['IS_NCNS'].mean().sort_values(ascending=False))


# Hypothesis 5: Are shifts posted 'urgently' by facilities more prone to no-shows?
print("\n--- NCNS Rate by Posting Lead Time ---")
print(booked_df.groupby('POSTING_LEAD_TIME_BIN')['IS_NCNS'].mean().sort_values(ascending=False))


# --- When and Why Do Worker Cancellations Happen? ---
print("\n\n===== Deep Dive: Analyzing Worker Cancellations =====")
# First, see how many cancellations are "late"
late_cancel_ratio = booked_df['IS_LATE_WORKER_CANCELLATION'].sum() / booked_df['IS_WORKER_CANCELED'].sum()
print(f"\nRatio of late cancellations among all worker cancellations: {late_cancel_ratio:.2%}")

# Hypothesis 6: Which shift slots have the most late cancellations?
print("\n--- Late Cancellation Rate by Shift Slot ---")
print(booked_df.groupby('SLOT')['IS_LATE_WORKER_CANCELLATION'].mean().sort_values(ascending=False))


# --- Step 3: The Final Analysis - Finding the Highest-Risk Profile ---
print("\n\n===== Final Analysis: The Highest-Risk Shift Profile =====")

# Define 'failure' as either a no-show OR a worker cancellation
booked_df['IS_FAILED'] = booked_df['IS_NCNS'] | booked_df['IS_WORKER_CANCELED']

# Group by multiple conditions at once to find the failure rate
failure_profile = booked_df.groupby(['SLOT', 'DURATION_BIN', 'BOOKING_LEAD_TIME_BIN']).agg(
    total_shifts=('IS_BOOKED', 'count'),
    failure_rate=('IS_FAILED', 'mean')
).reset_index()

# Filter for profiles with a statistically significant number of shifts (e.g., >= 30)
significant_profiles = failure_profile[failure_profile['total_shifts'] >= 50]

# Find the worst combinations with the highest failure rate
worst_profiles = significant_profiles.sort_values(by='failure_rate', ascending=False)

print("Top 5 Worst Shift Profiles (Highest Failure Rate):")
print(worst_profiles.head(10))





# --- Find the worst combinations with the highest filure rate (including the pay rate) ---
print("\n\n===== Deep Dive 2.0: Highest-Risk Profile Including Pay Rate =====")

failure_profile_with_pay = booked_df.groupby(['SLOT', 'PAY_RATE_BIN', 'DURATION_BIN', 'BOOKING_LEAD_TIME_BIN'], observed=True).agg(
    total_shifts=('IS_BOOKED', 'count'),
    failure_rate=('IS_FAILED', 'mean')
).reset_index()

significant_profiles_with_pay = failure_profile_with_pay[failure_profile_with_pay['total_shifts'] >= 50]

worst_profiles_with_pay = significant_profiles_with_pay.sort_values(by='failure_rate', ascending=False)

print("Top 10 Worst Shift Profiles (Including Pay Rate):")
print(worst_profiles_with_pay.head(10))


# --- Failure Rate Breakdown ---
print("\n\n=====Failure Rate Breakdown =====")

failure_breakdown = booked_df.groupby(['SLOT', 'PAY_RATE_BIN', 'DURATION_BIN', 'BOOKING_LEAD_TIME_BIN'], observed=True).agg(
    total_shifts=('IS_BOOKED', 'count'),
    total_failure_rate=('IS_FAILED', 'mean'),
    cancellation_rate=('IS_WORKER_CANCELED', 'mean'),
    ncns_rate=('IS_NCNS', 'mean')
).reset_index()


significant_breakdown = failure_breakdown[failure_breakdown['total_shifts'] >= 50]


top_5_breakdown = significant_breakdown.sort_values(by='total_failure_rate', ascending=False)


top_5_breakdown['total_failure_rate'] = top_5_breakdown['total_failure_rate'] * 100
top_5_breakdown['cancellation_rate'] = top_5_breakdown['cancellation_rate'] * 100
top_5_breakdown['ncns_rate'] = top_5_breakdown['ncns_rate'] * 100

print("Top 5 Worst Shift Profiles with Failure Rate Breakdown (min. 50 bookings):")
print(top_5_breakdown.head())


