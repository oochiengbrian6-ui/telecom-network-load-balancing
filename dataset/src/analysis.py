import pandas as pd

# Load dataset
df = pd.read_csv("../dataset/telecom_nodes.csv")

# Identify the node causing maximum latency
max_latency_node = df.loc[df["Latency_ms"].idxmax()]

print("Node causing maximum latency:")
print(max_latency_node)
