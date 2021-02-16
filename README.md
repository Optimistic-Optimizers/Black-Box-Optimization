# Black-Box-Optimization


## Use Cases

<strong> 1. Sampling </strong>
* User: Provide a function to be optimized
* Function: Samples the function to obtain a few data points  
* Results:  Stores these samples to create a model 
 
<strong> 2. Surrogate </strong> 
* User: Provides samples from the objective function 
* Function: Uses ML techniques to create a surrogate that can predict values for other data points  
* Results:  Create a surrogate model 

<strong> 3. Optimization </strong>
* User: Provides the surrogate model 
* Function: Determines which points are the most likely to contain an optimum based on the surrogate 
* Results: New points to sample from the objective function

<strong> 4. Update Model </strong>
* User: Provides data points to sample objective function  
* Function: Updates the surrogate  
* Results:  Surrogate becomes more accurate  
yesss
