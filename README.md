Student Performance Recommendation System
Project Overview
This project is designed to analyze student performance data, provide personalized recommendations, and visualize performance insights. The system processes quiz scores and uses KMeans clustering to categorize students into different personas. Each student is grouped based on their average score, and relevant recommendations are generated accordingly.

Features
Data Fetching: The system fetches student data from an external API.
Data Analysis: It computes the average score per student.
Clustering: Uses KMeans clustering to categorize students into personas based on their performance.
Persona Assignment: Each student is assigned a persona based on their average score.
Visualization: Visualizes the performance of students across different quiz topics using a bar chart.
Machine Learning: Implements KMeans clustering for persona creation based on student performance.
Setup Instructions
Prerequisites
Python 3.8 or higher
pip for installing dependencies
Steps to Set Up
Clone the repository:
git clone https://github.com/Shreyas-kul/student-recommendation.git

##steps 1.Navigate to the project directory: cd student-recommendation

2.Create a virtual environment (optional but recommended): python3 -m venv .venv

3.Activate the virtual environment: windows:.venv\Scripts\activate macOS:source .venv/bin/activate

4.Install dependencies: pip install -r requirements.txt

5.python main.py Persona Assignment The script assigns a persona to each student based on their average score:

The High Achiever: For students with scores >= 80. The Consistent Learner: For students with scores between 50 and 79. The Struggler: For students with scores below 50.

The following output will display the persona for each student: Student 1: The High Achiever Student 2: The Consistent Learner

Performance Visualization A bar chart will be generated to show the average score by quiz/topic, helping you understand how each topic was performed by students.

Technologies Used Python: Programming language Pandas: Data manipulation and analysis Matplotlib: Data visualization Seaborn: Advanced data visualization Scikit-learn: Machine learning (KMeans clustering)
