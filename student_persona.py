import requests
import pandas as pd
import sklearn

API_URL = "https://api.jsonserve.com/XgAgFJ"
response = requests.get(API_URL)
data = response.json()
df = pd.DataFrame(data)
df.head()

print(df.info())
print(df.describe())

df['score'] = df['score'].astype(int)
average_score_per_student = df.groupby('user_id')['score'].mean()

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3, random_state=42)

df['score'] = df['score'].astype(int)

average_score_per_student = df.groupby('user_id')['score'].mean()

average_score_per_student = average_score_per_student.values.reshape(-1, 1)

personas = {
    0: "The High Achiever - Strong performance across the board.",
    1: "The Consistent Learner - Steady, consistent performance with room for improvement.",
    2: "The Struggler - Needs more support in several topics."
}

average_score_per_student = df.groupby('user_id')['score'].mean()

def assign_persona(score):
    if score >= 80:
        return "The High Achiever - Strong performance across the board."
    elif score >= 50:
        return "The Consistent Learner - Steady, consistent performance with room for improvement."
    else:
        return "The Struggler - Needs more support in several topics."

        personas = average_score_per_student.apply(assign_persona)


        df['persona'] = df['user_id'].map(personas)

        for user_id, persona in df[['user_id', 'persona']].drop_duplicates().values:
print(f"Student {user_id}: {persona}")

    import matplotlib.pyplot as plt


print(df.columns)

print(df.dtypes)

df = df.dropna(subset=['score', 'quiz'])  




score_dict = {}

df['score'] = pd.to_numeric(df['score'], errors='coerce')
for index, row in df.iterrows():
    quiz = row['quiz']

if isinstance(quiz, dict):
        quiz = quiz.get('id', 'Unknown')
    
    score = row['score']

    if quiz in score_dict:
        score_dict[quiz]['sum'] += score
        score_dict[quiz]['count'] += 1
    else:
        score_dict[quiz] = {'sum': score, 'count': 1}

        topic_performance = {quiz: score_dict[quiz]['sum'] / score_dict[quiz]['count'] for quiz in score_dict}

        topic_performance = pd.Series(topic_performance)

        print(topic_performance.head())
        plt.figure(figsize=(12, 6))  # Adjust the figure size if necessary
sns.barplot(x=topic_performance.index, y=topic_performance.values, palette="coolwarm")

# Add labels and title to the plot
plt.xlabel("Quiz/Topic")
plt.ylabel("Average Score")
plt.title("Performance by Topic")

# Rotate the x-axis labels if there are too many topics or they are too long
plt.xticks(rotation=45, ha="right")  # Rotate labels and align them for better readability

# Display the plot
plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()