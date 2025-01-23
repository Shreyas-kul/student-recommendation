import pandas as pd

def analyze_performance(df):
    # Calculate accuracy per topic
    topic_performance = df.groupby("topic")["correct"].mean()
    return topic_performance

def generate_recommendations(df):
    performance = analyze_performance(df)
    
    recommendations = {}
    for topic, accuracy in performance.items():
        if accuracy < 0.5:
            recommendations[topic] = "Needs Improvement – Practice more!"
        elif accuracy < 0.8:
            recommendations[topic] = "Doing well – Keep practicing!"
        else:
            recommendations[topic] = "Excellent – Try advanced questions!"

    return recommendations
