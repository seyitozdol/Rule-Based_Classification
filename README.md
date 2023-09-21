# Potential Customer Return Calculation with Rule-Based Classification

![image](https://desktime.com/blog/wp-content/uploads/2021/08/meeting.png)


# Business Problem
A Game company aims to create new customer personas based on certain characteristics of our current customers, using a level-based approach.
After forming segments based on these new personas, we intend to predict how much a potential new customer in each segment might generate in terms of revenue for the company.
For instance, we want to determine the average revenue a 25-year-old male IOS user from Turkey might bring to the company.


## Dataset Story
The 'Persona.csv' dataset contains the prices of products sold by an international gaming company and certain demographic information about the customers who purchased these products.
The dataset is composed of records created with each sale transaction. Hence, the table is not deduplicated.
In other words, a user with specific demographic features might have made multiple purchases."

## Dataset

The dataset used in the project was taken from Kaggle named "Hotel Reservation Dataset". It has 36,275 observations and 18 features related to hotel reservations.
Attributes are a mix of categorical and numerical data. The target variable is "is_canceled", indicating whether the reservation has been cancelled.



| Variable Name                        | Description                                    |
| ------------------------------------ |------------------------------------------------|
| SOURCE                         | The type of device the customer connected from |
| SEX                       | The gender of the customer                     |
| COUNTRY                 | The country of the customer                    |
| AGE                    | The age of the customer                        |
| PRICE           | The amount the customer spent                  |

