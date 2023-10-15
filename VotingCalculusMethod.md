# A Dynamic Weight Allocation Model for Decentralized Voting Platforms

## Abstract
This research presents a mathematical model designed to address the issue of weight distribution in a decentralized voting platform with three community grades: starters, intermediates, and masters. The model ensures that each community grade has a non-negligible impact on the voting outcome, even when the number of users in these grades varies. The paper outlines a dynamic approach to allocate weights based on the changing composition of these user groups while adhering to the constraint that the total weight sums to 60%. The research focuses on maintaining a non-negligible influence for each grade by adjusting the weights of community members. The model presented in this paper is versatile and can adapt to different scenarios, making it a valuable tool for decentralized decision-making processes.

## 1. Introduction
Decentralized voting platforms have gained significant prominence in recent years for their ability to ensure transparent and community-driven decision-making. In these platforms, community members with different levels of experience and expertise may cast votes. The challenge is to allocate weights to these users in a way that ensures the influence of each community grade remains non-negligible. This paper addresses the need for a dynamic model that can accommodate varying levels of community participation while adhering to the prescribed weight distribution.
In fact, on the context of the HEC Paris x Tezos #2 edition (2023), our GoodGuy team tried to develop the Decentralized Voting Platforms (cf.main README)

## 2. Mathematical Model
The proposed mathematical model is designed to distribute weights (w1, w2, w3) to three community grades: starters, intermediates, and masters, based on the number of users in each grade. The model guarantees the following:
In this allocation model we will consider that all the users are going to vote. 

Total Weight Constraint: The sum of the weights (w1, w2, w3) equals 60% of the total decision-making power.
The 40% remainding vote will be dicided by the company. We are going to supose in this project, they are only going to vote just for one project.

Ascending Order: The weights are distributed in ascending order, ensuring that w1 < w2 < w3.

Non-negligible Contributions: Each community grade must have a significant impact on the final decision, regardless of the number of users in each grade.

The following grades can be defined as:
Starter = Nu * Token * weigh1
Intermediate = Nu * Token * weigh2
Master = Nu * Token * weigh3

Meaning that:
Starter = β1 * α1 * x1
Intermediate = β2 * α2 * x3
Master = β1 * α1 * x1

The contrains thus beeing:
β1, α1, x1 < β2, α2, x2
β2, α2, x2 < β3, α3, x3
x1 + X2 + x3 = 0.6

## 3.1 First simple limited solution

This first solution provide a very limited solution, not responding to the condition of Non-negligible Contributions, however it is the easier and faster implemenation solution.

We will have the following parameters:

W_total: Total weight available for the community grades (60%).
w_i: Weight assigned to community grade i.
n_i: Number of users in community grade i.

p_i: Proportion of the total number of users represented by community grade i.
W_company: Company's weight (40%).
α, β, and γ: Parameters defining the proportions of weights allocated to each community grade.
2.1 Proportion Definitions
To achieve these goals, we define the proportions of weights allocated to each community grade as follows:

Proportion for w1: α
Proportion for w2: α + β
Proportion for w3: α + β + γ
2.2 Weight Calculations
The weights for each community grade are calculated using the proportions and total weight as follows:

w_i = p_i * W_total
The company's weight (W_company) is calculated as:

W_company = 1 - ∑(w_i)

### Dynamic Function
The proposed mathematical model is implemented as a dynamic Python function to adapt to various scenarios. This function takes into account the presence of different community grades: starters, intermediates, and masters, and adjusts weights accordingly. The Python code is as follows:

```ruby
def calculate_weights(starters, intermediates, masters, alpha, beta, gamma):
    # Ensure there are no negative numbers
    starters = max(0, starters)
    intermediates = max(0, intermediates)
    masters = max(0, masters)

    # Total weight available (60%)
    W_total = 0.60

    # Calculate the proportions based on the provided alpha, beta, and gamma
    proportion_w1 = alpha
    proportion_w2 = alpha + beta
    proportion_w3 = alpha + beta + gamma

    # Calculate weights based on proportions
    w1 = proportion_w1 * W_total
    w2 = (proportion_w2 - proportion_w1) * W_total
    w3 = (proportion_w3 - proportion_w2) * W_total

    # Calculate the company's weight (40%)
    W_company = 1 - (w1 + w2 + w3)

    return w1, w2, w3, W_company

# Example usage:
starters = 1  # Replace with the number of starters
intermediates = 0  # Replace with the number of intermediates
masters = 0  # Replace with the number of masters
alpha = 0.2  # Adjust alpha as needed
beta = 0.3  # Adjust beta as needed
gamma = 0.1  # Adjust gamma as needed

w1, w2, w3, W_company = calculate_weights(starters, intermediates, masters, alpha, beta, gamma)
print(f"w1: {w1}, w2: {w2}, w3: {w3}, W_company: {W_company}")
```

The code enables dynamic weight allocation based on the evolving composition of the community grades, ensuring that the non-negligible contribution condition is met. The function provides flexibility for defining the proportions (α, β, γ) and allows for the allocation of weights in ascending order.
However it is limited on space as it will allocate some weigh to the inexisting grades.

## 3.2  Theoric semi-solution

Responding to the exact constarins:

β1, α1, x1 < β2, α2, x2
β2, α2, x2 < β3, α3, x3
x1 + X2 + x3 = 0.6

Would mean work in a three dimension space x1, x2, and x3, where we would find infinite solutions due to our limited computational power ressources.

To arrive to a soltion we will consider a two dimension space by constraining the equiation space.
We will then assume :
0 < x1 = 0.6 - x2 - x3 < 0.6

x1 α1 (0.6-x2-x3) < β2 α2 x2
β2 α2 x2 < β3 α3 x3

x2 + x3 > 0
x2 + x3 < 0.6
(β2 α2 + β1 α2) x2 + β1 α1 x3 > 0.6 β1 α1
β2 α2 x2 - β3 α3 x3 < 0

![image](https://github.com/MarcBTHT/HackathonHEC/assets/114303420/5eb1e25b-b1ca-46a5-b308-8b6ebc485886)

The solution exist on the area.


### Scenarios
The paper considers three distinct scenarios to demonstrate the adaptability of the model:

All starters: In this scenario, all users are beginners, and all weight is allocated to starters (w1) due to the absence of intermediates and masters.

Starters and intermediates: When both starters and intermediates are present, weights are allocated to w1 and w2. Masters are not considered.

Starters, intermediates, and masters: In this scenario, the weights are allocated to all community grades (w1, w2, w3), following the requirement w1 < w2 < w3.


## 5. Conclusion
The research presented offers a dynamic mathematical model for weight allocation in decentralized voting platforms. This model ensures that each community grade's contribution remains non-negligible, regardless of the composition of the community. It adapts to different scenarios and adheres to the constraints of total weight and ascending order of weights. This tool can significantly enhance the fairness and inclusivity of decentralized decision-making processes.

Carles Cerqueda
13th to 15th of October 2023 
In HEC Paris, on the HEC Paris x Tezos Hackathon

Acknowledgments
I would like to acknowledge the support development of this research, to Shuyi Zhang, and Dr. Gael Abongi Bokongo.
