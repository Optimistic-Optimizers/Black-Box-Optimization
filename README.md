# Black-Box-Optimization

From the Optuna package, the following optimizers were tested:

1. Random Optimizer 
    This optimizer randomly selects parameter values to sample from the objective function, and returns the values that
    have the highest output of the function. 
    
    Advantages:
	- Good for functions with few parameters
	- Good when sampling is cheap 
	- Fast   
    
    Disadvantages:
	- Inefficient when the function has many parameters
	- Inefficient when sampling is expensive
	- Inefficent on multi-modal or noisy functions 

2. Tree of Parzen Estimator (TPE)
    This optimizer finds the probability that a sample is higher than a certain threshold, g(x) and another probability that a
    sample is less than this same threshold, l(x). Both of these probabilities are expressed as a distribution. l(x)/g(x) gives
    the expected improvement. The optimizer samples from l(x), evaluates the expected improvement l(x)/g(x) and then tests this
    sample in the objective function. It is expected that the sample would improve after every iteration and eventually reach
    the optimum value of the function. 

    Advantages:
	- Accurate
	- Fast 
    
    Disadvantages:
	- Does not model the interactions between parameters   
    

3. Covariance Matrix Adaptation Evolution Strategy (CmaEs) 
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
