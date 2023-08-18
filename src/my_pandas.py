import my_pandas as pd
import random
from faker import Faker

fake = Faker()

# Generate sample data for up to 200 records
num_records = 200
data = []
for _ in range(num_records):
    row = [
        random.randint(800, 999),    # OfficeNo
        random.randint(10000, 99999),# AccountNo
        random.randint(100, 999),    # FaNo
        fake.date_between(start_date='-2y', end_date='today').strftime('%d-%m-%Y'),   # Report Date
        fake.word(),                # ReportCode
        random.randint(1, 5),       # Version
        fake.word(),                # ISGAcct
        fake.date_between(start_date='-2y', end_date='today').strftime('%d-%m-%Y'),   # LoadDate
        random.choice(['Y', 'N']),  # Consolidation
        ', '.join([str(random.randint(800000000, 899999999)) for _ in range(random.randint(5, 10))]),  # ConsolidatedAccts1
        ', '.join([str(random.randint(800000000, 899999999)) for _ in range(random.randint(5, 10))])   # ConsolidatedAccts2
    ]
    data.append(row)

# Create a DataFrame from the generated data
columns = ['OfficeNo', 'AccountNo', 'FaNo', 'Report Date', 'ReportCode', 'Version:', 'ISGAcct',
           'LoadDate', 'Consolidation', 'ConsolidatedAccts1', 'ConsolidatedAccts2']
df = pd.DataFrame(data, columns=columns)

# Write the DataFrame to a CSV file
df.to_csv('generated_data.csv', index=False)
