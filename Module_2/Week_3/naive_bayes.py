import numpy as np
import numpy as np
import numpy as np

def create_train_data():
    data = [
        ['Sunny', 'Hot', 'High', 'Weak', 'No'],
        ['Sunny', 'Hot', 'High', 'Strong', 'No'],
        ['Overcast', 'Hot', 'High', 'Weak', 'Yes'],
        ['Rain', 'Mild', 'High', 'Weak', 'Yes'],
        ['Rain', 'Cool', 'Normal', 'Weak', 'Yes'],
        ['Rain', 'Cool', 'Normal', 'Strong', 'No'],
        ['Overcast', 'Cool', 'Normal', 'Strong', 'Yes'],
        ['Overcast', 'Mild', 'High', 'Weak', 'No'],
        ['Sunny', 'Cool', 'Normal', 'Weak', 'Yes'],
        ['Rain', 'Mild', 'Normal', 'Weak', 'Yes']
    ]
    return np.array(data)

train_data = create_train_data()

def compute_prior_probability(train_data):
    y_unique = ['No', 'Yes']
    prior_probability = np.zeros(len(y_unique))
    labels = train_data[:, -1]
    total_instances = len(labels)
    for i, label in enumerate(y_unique):
        count = np.sum(labels == label)
        prior_probability[i] = count / total_instances
    return prior_probability

train_data = create_train_data()
prior_probability = compute_prior_probability(train_data)

print("P(Play Tennis = No):", prior_probability[0])
print("P(Play Tennis = Yes):", prior_probability[1])


def compute_conditional_probability(train_data):
    feature_names = ['Outlook', 'Temperature', 'Humidity', 'Wind']
    y_unique = ['No', 'Yes']
    conditional_probabilities = {}
    features = train_data[:, :-1]
    labels = train_data[:, -1]
    num_features = features.shape[1]
    for label in y_unique:
        class_data = features[labels == label]
        feature_probabilities = {}
        for i in range(num_features):
            feature_column = class_data[:, i]
            unique_values = np.unique(feature_column)
            feature_probabilities[i] = {val: np.sum(feature_column == val) / len(feature_column)
                                        for val in unique_values}
        conditional_probabilities[label] = feature_probabilities
    return conditional_probabilities, feature_names

def train_naive_bayes(train_data):
    prior_probability = compute_prior_probability(train_data)
    conditional_probability, list_x_name = compute_conditional_probability(train_data)
    return prior_probability, conditional_probability, list_x_name

train_data = create_train_data()
prior_probability, conditional_probability, list_x_name = train_naive_bayes(train_data)

print("Prior Probabilities:", prior_probability)
print("Conditional Probabilities:", conditional_probability)
print("Feature Names:", list_x_name)
