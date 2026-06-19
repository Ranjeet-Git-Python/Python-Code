import numpy as np

class McDonaldsNutritionAnalyzer:
    def __init__(self):
        self.food_items = np.array(['Big Mac', 'Fries', 'McChicken', 'Coke'])
        self.nutrition_data = np.array([
            [550, 25, 30],
            [320, 4, 15],
            [400, 14, 21],
            [150, 0, 0]
        ])

    def show_all_items(self):
        print("McDonald's Items and their Nutrition (Calories, Protein, Fat):")
        for i in range(len(self.food_items)):
            print(self.food_items[i], ":", self.nutrition_data[i])

    def get_total_nutrition(self):
        total = self.nutrition_data.sum(axis=0)
        print("\nTotal Nutrition for All Items:")
        print("Calories:", total[0])
        print("Protein:", total[1], "g")
        print("Fat:", total[2], "g")

    def reshape_nutrition(self):
        reshaped = self.nutrition_data.reshape(2, 6)
        print("\nReshaped Nutrition Data (2 rows, 6 columns):")
        print(reshaped)

    def add_new_food(self, name, calories, protein, fat):
        self.food_items = np.append(self.food_items, name)
        new_data = np.array([[calories, protein, fat]])
        self.nutrition_data = np.vstack((self.nutrition_data, new_data))
        print("\n", name, "added successfully!")

analyzer = McDonaldsNutritionAnalyzer()
analyzer.show_all_items()
analyzer.get_total_nutrition()
analyzer.reshape_nutrition()
analyzer.add_new_food('McFlurry', 510, 9, 16)
analyzer.show_all_items()
