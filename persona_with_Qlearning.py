import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from collections import defaultdict


API_URL = "https://api.jsonserve.com/XgAgFJ"
response = requests.get(API_URL)
data = response.json()
df = pd.DataFrame(data)


df.dropna(subset=['score', 'quiz'], inplace=True)
df['score'] = df['score'].astype(int)
df['user_id'] = df['user_id'].astype(str)
df['quiz'] = df['quiz'].apply(lambda x: x.get('id', 'Unknown') if isinstance(x, dict) else x)

class QLearningAgent:
    def __init__(self, actions, learning_rate=0.1, discount_factor=0.9, exploration_rate=0.2):
        self.q_table = defaultdict(lambda: np.zeros(len(actions)))
        self.actions = actions
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate

    def choose_action(self, state):
        if np.random.rand() < self.exploration_rate:
            return np.random.choice(self.actions)  
        return self.actions[np.argmax(self.q_table[state])]  

    def update_q_value(self, state, action, reward, next_state):
        action_index = self.actions.index(action)
        best_next_action = np.max(self.q_table[next_state])
        self.q_table[state][action_index] += self.learning_rate * (
            reward + self.discount_factor * best_next_action - self.q_table[state][action_index]
        )

actions = df['quiz'].unique().tolist()
agent = QLearningAgent(actions)

for _, row in df.iterrows():
    state = row['user_id']
    action = row['quiz']
    reward = row['score'] 
    next_state = state 
    agent.update_q_value(state, action, reward, next_state)

quiz_recommendations = {user: agent.choose_action(user) for user in df['user_id'].unique()}

for user, quiz in quiz_recommendations.items():
    print(f"Recommended quiz for Student {user}: {quiz}")

score_dict = defaultdict(lambda: {'sum': 0, 'count': 0})
for _, row in df.iterrows():
    quiz = row['quiz']
    score = row['score']
    score_dict[quiz]['sum'] += score
    score_dict[quiz]['count'] += 1

topic_performance = {quiz: score_dict[quiz]['sum'] / score_dict[quiz]['count'] for quiz in score_dict}
topic_performance = pd.Series(topic_performance)

plt.figure(figsize=(12, 6))
sns.barplot(x=topic_performance.index, y=topic_performance.values, palette="coolwarm")
plt.xlabel("Quiz/Topic")
plt.ylabel("Average Score")
plt.title("Performance by Topic")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
