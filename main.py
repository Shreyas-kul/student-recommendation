import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


API_URL = "https://api.jsonserve.com/XgAgFJ"
response = requests.get(API_URL)
data = response.json()

df = pd.DataFrame(data)
df.head()
# Check column names and data types
print(df.info())
print(df.describe())


performance = df.groupby('score')['score'].mean()
print("Performance by Topic:")
print(performance)

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 5))
sns.barplot(x=performance.index, y=performance.values, palette="coolwarm")
plt.xlabel("Topic")
plt.ylabel("Average Score")
plt.title("Student Performance by Topic")
plt.xticks(rotation=45)
plt.show()


recommendations = {}
for topic, score in performance.items():
    if score < 60:
        recommendations[topic] = "Review this topic"
    elif 60 <= score < 80:
        recommendations[topic] = "Good, but could improve"
    else:
        recommendations[topic] = "Excellent"

print("Personalized Recommendations:")
for topic, recommendation in recommendations.items():
    print(f"{topic}: {recommendation}")



with open("recommendations.txt", "w") as f:
    for topic, recommendation in recommendations.items():
        f.write(f"{topic}: {recommendation}\n")

print("Recommendations saved to recommendations.txt")

