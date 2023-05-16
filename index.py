import time
from common.script import script

# Timer Initiated
start_time = time.time()

print("Loading....")
script()

# Stop Timer
end_time = time.time()

# Verifying Process Time
duration = end_time - start_time
print(f"Process took {duration:.2f} seconds to complete.")
