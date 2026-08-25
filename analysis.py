import pandas as pd

data = pd.read_csv("dataset/robotics_maintenance_data.csv")

print("Robotics Operations & Maintenance Analytics")
print("--------------------------------------------")

print("\nDataset Overview:")
print(data.info())

print("\nAverage Performance Score:")
print(data["Performance_Score"].mean())

print("\nTotal Downtime Hours:")
print(data["Downtime_Hours"].sum())

print("\nTotal Maintenance Cost:")
print(data["Maintenance_Cost_USD"].sum())

print("\nTotal Failures:")
print(data["Failure_Count"].sum())

print("\nAverage Energy Consumption:")
print(data["Energy_Consumption_kWh"].mean())
