import pandas as pd

# Load dataset
df = pd.read_csv("../dataset/telecom_nodes.csv")

print("Before Load Balancing:")
print(df[["Node", "CPU_pct", "Memory_GB"]])

# Load balancing logic
for index, row in df.iterrows():
    if row["CPU_pct"] > 70:
        # Reduce load on overloaded node
        df.at[index, "CPU_pct"] -= 10
        df.at[index, "Memory_GB"] -= 2

        # Redistribute load to least loaded node
        target_index = df["CPU_pct"].idxmin()
        df.at[target_index, "CPU_pct"] += 10
        df.at[target_index, "Memory_GB"] += 2

print("\nAfter Load Balancing:")
print(df[["Node", "CPU_pct", "Memory_GB"]])

# Save results
df.to_csv("../results/after_balancing.txt", index=False)
