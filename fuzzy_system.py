import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Input variables
rating = ctrl.Antecedent(np.arange(0, 10, 1), 'rating')
popularity = ctrl.Antecedent(np.arange(0, 101, 1), 'popularity')

# Output variable
recommendation = ctrl.Consequent(np.arange(0, 101, 1), 'recommendation')

# Membership functions for Rating
rating['low'] = fuzz.trimf(rating.universe, [0, 0, 5])
rating['medium'] = fuzz.trimf(rating.universe, [3, 5, 7])
rating['high'] = fuzz.trimf(rating.universe, [6, 9, 9])

# Membership functions for Popularity
popularity['low'] = fuzz.trimf(popularity.universe, [0, 0, 40])
popularity['medium'] = fuzz.trimf(popularity.universe, [20, 50, 80])
popularity['high'] = fuzz.trimf(popularity.universe, [60, 100, 100])

# Membership functions for Recommendation output
recommendation['weak'] = fuzz.trimf(recommendation.universe, [0, 0, 50])
recommendation['average'] = fuzz.trimf(recommendation.universe, [20, 50, 80])
recommendation['strong'] = fuzz.trimf(recommendation.universe, [60, 100, 100])

# Fuzzy rules
rule1 = ctrl.Rule(rating['high'] & popularity['high'], recommendation['strong'])
rule2 = ctrl.Rule(rating['medium'] & popularity['medium'], recommendation['average'])
rule3 = ctrl.Rule(rating['low'] | popularity['low'], recommendation['weak'])
rule4 = ctrl.Rule(rating['high'] & popularity['medium'], recommendation['strong'])
rule5 = ctrl.Rule(rating['medium'] & popularity['high'], recommendation['strong'])

# Create control system
recommendation_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
recommendation_system = ctrl.ControlSystemSimulation(recommendation_ctrl)

def compute_recommendation(r, p):
    recommendation_system.input['rating'] = r
    recommendation_system.input['popularity'] = p
    recommendation_system.compute()
    return recommendation_system.output['recommendation']
