# Black-Box-Optimization


## Use Cases

1. Sampling 
* User: Provide a function to be optimized
* Function: Samples the function to obtain a few data points  
* Results:  Stores these samples to create a model 
 
2. Surrogate  
* User: Provides samples from the objective function 
* Function: Uses ML techniques to create a surrogate that can predict values for other data points  
* Results:  Create a surrogate model 

3. Optimization 
* User: Provides the surrogate model 
* Function: Determines which points are the most likely to contain an optimum based on the surrogate 
* Results: New points to sample from the objective function

4. Update Model 
* User: Provides data points to sample objective function  
* Function: Updates the surrogate  
* Results:  Surrogate becomes more accurate  