# Black-Box-Optimization

Black-Box-Optimization is a Data Science Project that was developed as part of the DIRECT Program by a group of graduate students from the University of Washington in Seattle.

The goal of Black-Box-Optimization is to explore and test a variety of optimizing tools with many different objective functions to provide a guide for users to identify the best optimizing tool for their specific optimization needs. Optimization is an important tool in making decisions and in analyzing physical systems. In mathematical terms, an optimization problem is the problem of finding the best solution (i.e., maxima or minima) from among the set of all feasible solutions. 

We chose to do this project because we appreciate the essentiality of the application and the importance of making it a less expensive and timely process. 




## Description of Optimizers used:

From the Optuna package, the following optimizers were tested:

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