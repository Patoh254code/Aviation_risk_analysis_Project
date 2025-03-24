# 1.0 **Project Title: Aircraft Risk Assessment for Business Expansion**
### **Author:** Patrice Okoiti

## 1.1 **Overview**
For this project, I will use data cleaning, imputation, analysis, and visualization to generate insights in the aviation industry for a business stakeholder looking to diversify operations.

## 1.2 **Data Understanding**
The selected Dataset https://www.kaggle.com/datasets/khsamaha/aviation-accident-database-synopses for our analysis is from the National Transportation Safety Board, available on Kaggle, detailing the civil aviation accidents and selected incidents in the United States and international waters between 1962 and 2023. It details aircraft accidents, including information on accident, aircraft specifications, weather conditions, and injury severity which are relevant to our analysis.

### 1.2.1 **column description**

| **Columns** | **Description** |
|-------------|-----------------|
| Event Id, Accident Number, Event Date, Location, Country, Latitude, Longitude, Airport Code, Airport Name | Unique identifiers for each accident and its location. |
| Make, Model, Aircraft Category, Amateur Built, Number of Engines, Engine Type | Details about the aircraft involved in the accident. |
| Injury Severity, Aircraft Damage, Weather Condition, Broad Phase of Flight | Risk factors contributing to the accident. |
| FAR Description, Schedule, Purpose of Flight, Air Carrier | Type of operations and flight purpose. |
| Total Fatal Injuries, Total Serious Injuries, Total Minor Injuries, Total Uninjured | Casualties per accident. |

*Features:* The most important features relevant to our analysis from our dataset include unique identifiers of aircraft, that is, Make, Model, Date and risk factors associated with aircraft accidents, that is, Weather Conditions, Broad phase of flight

*Target:* The target audience for this analysis is a business stakeholder looking to diversify operations into the aviation industry, particularly in private and commercial flights operations

## 1.3 **Business problem**
Our company is diversifying their portfolio by venturing into the aviation industry. The aim is to purchase and operate aircraft for commercial and private enterprises. However, aviation involves significant safety risks, including accidents and operational hazards. The goal of this project is to analyze historical aircraft accident data to identify low-risk aircraft models and key risk factors that could impact operations.

## 1.4 **Objectives**
1. Identify the aircract models with lowest accidents rate - This will involve analyzing the number of accidents based on aircraft 'Make' and 'Model' to determine the aircraft with the lowest risk of accidents.
2. Identify risk factors contributing to aircraft accidents - This will involve tracking accident trends over the last 23years and weather conditions, broad phase of the aircraft, for example landing or taking off, as risk factors contributing to accident.
3. Evaluate flight risks based on operations - Compare number of accidents between private commercial flight operations by analyzing Category of Purpose column to determine safer operational choices.

## 1.5 **Method of Analysis**
1. Descriptive Statistics: Summarizing the accident counts based on aircraft type and accident trend overtime.
2. Data visualisation: Use of bar charts and line charts to analyse accident rates per aircraft.
3. Risk Assessment: Analyze risk factors associated with number of accidents of the aircrafts.

## 1.6 **Key Findings**

1. The following chart shows the safest aircrafts based on lowest number of accidents for private and commercial flights to be prioritized:

![Safest Aircracts](Images/Safest-aircrafts.jpg)




2. The following chart shows that most accidents occurred under VMC(Visual Meteorological Conditions) to suggest that weather is not the primary risk factor associated with accidents but rather human error and possibly mechanical issues:

![Weather Conditions as a Risk Factor](Images/Weather-impact.jpg)




3. The following chart shows that venturing into private flight operations is riskier than commercial flights operations:

![Risks Based on Flight Operations](Images/Operations-risk.jpg)





## 1.7 **Conclusion**

From out analysis of the Aviation Data we can conclude the following:

1. The aircrafts with the high number of accidents may be due to high levels of usage
2. Adverse weather conditions is a significant risk factor in aircraft accidents but it has not been the primary risk factor in the  
21st Century. Additionally, Significant number of accidents often occur during landing, taking off and cruising
3. Private flights have encountered a significant high number of accidents as compared to commercial flights


