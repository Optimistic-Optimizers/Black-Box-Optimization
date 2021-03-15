# Black-Box-Optimization

Black-Box-Optimization is a Data Science Project that was developed as part of the DIRECT Program by a group of graduate students from the University of Washington in Seattle.

The goal of Black-Box-Optimization is to explore and test a variety of optimizing tools with many different objective functions to provide a guide for users to identify the best optimizing tool for their specific optimization needs. Optimization is an important tool in making decisions and in analyzing physical systems. In mathematical terms, an optimization problem is the problem of finding the best solution (i.e., maxima or minima) from among the set of all feasible solutions. 

We chose to do this project because we appreciate the essentiality of the application and the importance of making it a less expensive and timely process. 




## Description of Optimizers used:

**From the Optuna package, the following optimizers were tested:**

1. **Random Optimizer**: 
    This optimizer randomly selects parameter values to sample from the objective function, and returns the values that
    have the highest output of the function. 
    
    *Advantages:*
	- Good for functions with few parameters
	- Good when sampling is cheap 
	- Fast   
    
    *Disadvantages:*
	- Inefficient when the function has many parameters
	- Inefficient when sampling is expensive
	- Inefficent on multi-modal or noisy functions 

2. **Tree of Parzen Estimator (TPE):**
    This optimizer finds the probability that a sample is higher than a certain threshold, g(x) and another probability that a
    sample is less than this same threshold, l(x). Both of these probabilities are expressed as a distribution. l(x)/g(x) gives
    the expected improvement. The optimizer samples from l(x), evaluates the expected improvement l(x)/g(x) and then tests this
    sample in the objective function. It is expected that the sample would improve after every iteration and eventually reach
    the optimum value of the function. 

    *Advantages:*
	- Accurate
	- Fast 
    
    *Disadvantages:*
	- Does not model the interactions between parameters   
    

3. **Covariance Matrix Adaptation Evolution Strategy (CmaEs):**
    The basis of this optimization method is sampling from a multivariate gaussian distribution. This distribution 
    shows the correlation between the parameters of the objective function and is defined by a vector 
    of means and a covariance matrix. CmaEs employs an evolution strategy where candidates are sampled from the
    objective function and ranked according to their value. The best candidates undergo recombination which changes
    the covariance matrix of the multivariate gaussian distribution. As more iterations are calculated, the covariance matrix
    becomes more accurate and the optimum of the function is eventually found. 

    Advantages:
	- Works well on functions with large dimensions  
	- Works well on multi-modal or noisy functions
    
    Disadvantages:
	- Inefficient on functions with low dimensions 
	- Needs to sample the function many times     


**Additional optimizers tested:**

4. **Bayes_Opt:**
   Bayesian optimization works by constructing a posterior distribution of functions (Gaussian process) that best describes the 
   function to be optimized. When the number of observations increases, the posterior distribution improves, and the algorithm 
   becomes more confident of which regions in parameter space to explore and which regions to ignore.
   
   The algorithm balances its needs of exploration and exploitation taking into account what it 
   knows about the target function as the number of iterations increases. At each step a Gaussian Process is fitted to the 
   previously explored points, and the posterior distribution, combined with a exploration strategy (such Upper Confidence Bound 
   or Expected Improvement), are used to determine the next point that should be explored.
   
    *Advantages:*
	- Very accurate and fast 
	- Works well on expensive functions
    
    *Disadvantages:*
	- Results are sensitive to parameters of the surrogate model
	- Needs to sample the function many times

**From the Pulp package, the following optimizer is tested:**

5.	**Coin-or branch and cut (CBC)**:
    Given a MIP model to minimize where some variables must take on integer values (e.g., 0, 1, or 2), relax the integrality requirements
	(e.g., consider each "integer" variable to be continuous with a lower bound of 0.0 and an upper bound of 2.0). Then Solves the resulting 
	linear model with an LP solver to obtain a lower bound on the MIP's objective function value. If the optimal LP solution has integer values 
	for the MIP's integer variables, we are finished. Any MIP-feasible solution provides an upper bound on the objective value. 
	The upper bound equals the lower bound; the solution is optimal. Otherwise, there exists an "integer" variable with a non-integral value. 
	Choose one non-integral variable (e.g., with value 1.3) and branch. Creates two nodes, one with the branching variable having an upper bound of 1.0, 
	and the other with the branching variable having a lower bound of 2.0. Add the two nodes to the search tree. Picks a node off the tree. 
	Creates an LP relaxation and solve. Interrogate the optimal LP solution and if unable to prune the node, then branch.

    *Advantages:*
	- On easier instances it is fast
 	- On easier instances it performs well
    
    *Disadvantages:*
	- On harder instances it works very slow
    - On harder instances it's not accurate 

**From the Hyperopt package, the following optimizers were tested:**

6. **Random Search**: 
    This method works where random combinations of the values of the hyperparameters are used to find the best solution for the built model. 
	Random search samples random parameters combinations from a statistical distribution provided by the user.
	This approach is based on the assumption that in most cases, hyperparameters are not uniformly important. 
	The search strategy starts evaluating all the candidates with a small amount of resources and iteratively selects the best candidates, using more and more resources. 
    
    *Advantages:*
	- Random Search is Fast
	- Adding parameters that do not influence the performance does not decrease efficiency.
    
    *Disadvantages:*
	- Random Search sometimes could miss important points(values) in the search space.

7. **Tree of Parzen Estimators (TPE):**
    This optimizer finds the probability that a sample is higher than a certain threshold, g(x) and another probability that a
    sample is less than this same threshold, l(x). Both of these probabilities are expressed as a distribution. l(x)/g(x) gives
    the expected improvement. The optimizer samples from l(x), evaluates the expected improvement l(x)/g(x) and then tests this
    sample in the objective function. It is expected that the sample would improve after every iteration and eventually reach
    the optimum value of the function. 

    *Advantages:*
    - Executes in consistent, predictable amount of time that will never change
 	- Fast to execute
	- Better normalized between different hyper-parameter spaces
    
    *Disadvantages:*
	- Not focused on the globally optimal result - forces the algorithm to take the shortest path into a local minima
    - In Mean loss after K-trials, if you set K too high, algorithm may find near optimal values regardless of what changes you make to it  

**From the Skopt package, the following optimizer was tested:**

8. **Bayesian Optimization:**
   Bayesian optimization works by constructing a posterior distribution of functions (Gaussian process) that best describes the 
   function to be optimized. When the number of observations increases, the posterior distribution improves, and the algorithm 
   becomes more confident of which regions in parameter space to explore and which regions to ignore.
   
   The algorithm balances its needs of exploration and exploitation taking into account what it 
   knows about the target function as the number of iterations increases. At each step a Gaussian Process is fitted to the 
   previously explored points, and the posterior distribution, combined with a exploration strategy (such Upper Confidence Bound 
   or Expected Improvement), are used to determine the next point that should be explored.
   
    *Advantages:*
    - Very accurate and fast 
    - Works well on expensive functions
    - Works well on noisy functions
    
    *Disadvantages:*
    - Results are sensitive to parameters of the surrogate model
    - Needs to sample the function many times
    - Scale poorly with number of hyperparameters

## Results:
![alt text](https://github.com/Optimistic-Optimizers/Black-Box-Optimization/blob/main/optimization_results.jpg?raw=true)    
*Figure 1.* The figure shows how the machine learning model categorized each optimizer based on the three parameters:
Number of trials, Accuracy, Time of Iteration. The figure shows the results for a 2 dimensional objective function.

![alt text](https://github.com/Optimistic-Optimizers/Black-Box-Optimization/blob/main/optimization_results_4.jpg?raw=true)
*Figure 2* The figure shows how the machine learning model categorized each optimizer based on the three parameters.
The figure shows the results for a 4 dimentional objective function.  
## Software Dependencies:

The following software dependencies are associated with this package:
	- Python 3.7
	- Please see the file environmental.yml for the needed packages **(Note to group: Need to create the environmental.yml??)**


## How to Install:


## Organization of the Project:


## Running Tests:
