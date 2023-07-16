import pandas as pd


def calculate_average():
    url = "https://drive.google.com/uc?export=download&id=13nk_FYpcayUck2Ctrela5Tjt9JQbjznt"

    data = pd.read_csv(url)

    average_height_inches = data['Height(Inches)'].mean()
    average_weight_pounds = data['Weight(Pounds)'].mean()

    average_height_cm = average_height_inches * 2.54
    average_weight_kg = average_weight_pounds * 0.45359237

    return average_height_cm, average_weight_kg


def print_average(height, weight):
    print(f"Average height: {height} cm")
    print(f"Average weight: {weight} kg")

