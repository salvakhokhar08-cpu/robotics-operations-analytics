# Robotics Operations & Maintenance Analytics

## Project Overview

This project analyzes robotics operations and maintenance data to identify patterns in robot performance, downtime, failures, maintenance costs, and energy consumption.

The goal is to demonstrate how data analytics can support maintenance planning, operational efficiency, and data-driven decision-making in technology and robotics environments.

## Business Questions

- Which maintenance type has the highest downtime?
- Which maintenance type has the highest maintenance cost?
- How does maintenance type affect robot performance?
- Which location has the highest and lowest robot performance?
- What operational improvements can be identified from the data?

## Key Findings

- Average robot performance score: **87.1**
- Total downtime: **156.2 hours**
- Total maintenance cost: **$9,830**
- Total failures: **26**
- Average energy consumption: **4.39 kWh**

### Maintenance Type Analysis

| Maintenance Type | Avg. Downtime (Hours) | Avg. Maintenance Cost (USD) | Avg. Performance |
|---|---:|---:|---:|
| Corrective | 24.425 | $1,545.00 | 79.50 |
| Preventive | 11.925 | $712.50 | 90.75 |
| Routine | 5.400 | $400.00 | 95.00 |

### Location Analysis

| Location | Avg. Performance |
|---|---:|
| Data Center A | 88.0 |
| Data Center B | 84.5 |
| Data Center C | 92.0 |
| Data Center D | 81.0 |

## Business Insight

The analysis indicates that corrective maintenance is associated with the highest average downtime and maintenance cost, while routine and preventive maintenance show higher average performance scores.

Data Center D has the lowest average performance score and may require further investigation to identify operational or maintenance issues.

These findings demonstrate how data analytics can help organizations identify maintenance priorities and opportunities for operational improvement.

## Visualizations

The project includes Python visualizations comparing:

- Robot performance by location
- Average downtime by maintenance type
- Average maintenance cost by maintenance type
- Average performance by maintenance type

## Tools & Technologies

- Python
- Pandas
- Matplotlib
- Google Colab
- GitHub

## Dataset

The dataset contains information about robot operating hours, downtime, failures, maintenance costs, energy consumption, maintenance type, location, and performance scores.

Dataset file:

`dataset/robotics_maintenance_data.csv`

## Project Structure

```text
robotics-operations-analytics/
│
├── dataset/
│   └── robotics_maintenance_data.csv
│
├── analysis.py
│
└── README.md
```
## Project Purpose
This project was created as a portfolio project to demonstrate Business Analytics skills, including data cleaning, exploratory analysis, data visualization, business insights, and analytical problem-solving.
It also reflects my interest in applying analytics to technology, robotics, and operational efficiency.
