# OPTIMIZATION-MODEL

*COMPANY*: COTECH IT SOLUTIONS

*NAME*: R.S.PRIYADHARSHINI

*INTERN ID*: CTO4DR2648

*DOMAIN*: DATA SCIENCE

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

## DESCRIPTION - OPTIMIZATION MODEL

Optimization is a very important concept in computer science, data science, and business decision-making. Many real-world problems involve limited resources such as time, money, labor, or raw materials, and organizations aim to use these resources in the best possible way. The main goal of this task is to understand how optimization techniques can be applied to solve a business problem and maximize profit while satisfying given constraints.

In this task, an optimization model is developed to solve a profit maximization problem using Python. The problem is based on a simple business scenario where a company manufactures two products: Product A and Product B. Each product generates a certain amount of profit per unit, but the production of these products is limited by resource constraints. The objective is to determine how many units of each product should be produced in order to achieve the maximum total profit without violating any constraints.

The company earns a profit of ₹40 for every unit of Product A and ₹30 for every unit of Product B. However, the production process uses limited resources, which are represented using linear constraints. The first constraint states that producing two units of Product A and one unit of Product B should not exceed a total resource limit of 100 units. The second constraint states that producing one unit of Product A and two units of Product B should not exceed another resource limit of 80 units. Additionally, it is assumed that negative production is not possible, meaning the number of units produced for both products must be zero or greater.

The optimization problem is formulated with the objective of maximizing total profit, which is expressed as a linear objective function. The objective function combines the profits of both products and depends on the number of units produced for each product. This type of problem falls under the category of linear programming, where both the objective function and constraints are linear in nature.

Although specialized optimization libraries such as PuLP are commonly used to solve linear programming problems, this task demonstrates an alternative approach using a brute-force search method in Python. This approach involves checking all feasible combinations of Product A and Product B within a reasonable range and selecting the combination that yields the highest profit while satisfying all constraints. This method helps in clearly understanding the logic behind optimization without relying heavily on external libraries.

The Python program systematically iterates through possible values for Product A and Product B. For each combination, it checks whether the constraints are satisfied. If the constraints are met, the total profit is calculated. The program keeps track of the best solution found so far by comparing profits and updating the optimal values whenever a higher profit is achieved. At the end of the execution, the program outputs the optimal number of units for Product A and Product B along with the maximum achievable profit.

In addition to calculating the optimal solution, the task also includes visualizing the results. A bar chart is created using the Matplotlib library to display the optimal production quantities for both products. Visualization plays an important role in data analysis and decision-making, as it makes the results easier to understand and interpret. The generated graph serves as a clear visual representation of the optimal production plan and can be included as output evidence for the internship submission.

The final result of the optimization model shows that producing 40 units of Product A and 20 units of Product B yields the maximum profit of ₹2200 while satisfying all constraints. This result demonstrates how optimization techniques can help businesses make informed production decisions and efficiently utilize available resources.

In conclusion, this task successfully demonstrates the application of optimization concepts to a real-world business problem using Python. It provides a strong foundation for understanding linear programming, constraint handling, and result visualization. The task highlights the importance of optimization in improving efficiency and profitability, making it a valuable learning experience during the CODTECH internship program.
