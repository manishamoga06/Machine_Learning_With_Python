
# Student Performance Prediction Project

# Importing libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# Step 1: Creating student data
hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
marks = [20, 25, 35, 40, 50, 55, 65, 75, 85, 95]


# Step 2: Creating a table
data = pd.DataFrame({
    "Study Hours": hours,
    "Marks": marks
})

print("\nStudent Data")
print(data)


# Step 3: Displaying the graph
plt.scatter(hours, marks)

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")

plt.show()


# Step 4: Preparing data for the model
X = data[["Study Hours"]]
y = data["Marks"]


# Step 5: Creating the model
model = LinearRegression()


# Step 6: Training the model
model.fit(X, y)

print("\nModel trained successfully!")


# Step 7: Taking input from the user
study_hours = float(input("\nEnter study hours (1 to 10): "))


# Step 8: Predicting marks
if 1 <= study_hours <= 10:

    new_student = pd.DataFrame({
        "Study Hours": [study_hours]
    })

    prediction = model.predict(new_student)

    print("Predicted Marks:", round(prediction[0], 2))

else:
    print("Please enter study hours between 1 and 10.")


# Step 9: Displaying the final graph
plt.scatter(hours, marks, label="Actual Marks")

plt.plot(
    hours,
    model.predict(X),
    color="red",
    label="Prediction Line"
)

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Student Performance Prediction")

plt.legend()
plt.show()

print("\nProject Completed!")
