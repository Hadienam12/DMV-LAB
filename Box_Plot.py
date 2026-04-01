import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("network_security_metrics.csv")

# Style
sns.set(style="whitegrid")

plt.figure(figsize=(10,6))

# Box plot
sns.boxplot(
    data=df,
    x="attack_type",
    y="byte_volume_mb",
    palette="Set3"
)

plt.title("Box Plot: Byte Volume by Attack Type")
plt.xlabel("Attack Type")
plt.ylabel("Byte Volume (MB)")

plt.show()