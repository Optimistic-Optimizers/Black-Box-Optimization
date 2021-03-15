def test_ensemble_methods():
	'''Runs several tests on the function'''
	from black_box_optimization.ensemble_methods import decision_tree_classifier
	from black_box_optimization.ensemble_methods import random_forest_classifier
	import numpy as np    
    
	for i in range(2):
		a = np.random.rand(1)
		b = np.random.rand(1)
		c = np.random.rand(1)
		d = np.random.rand(1)
		predict = decision_tree_classifier(a,b,c,d)
		assert type(predict) == str, 'Output is not a string'
		if predict == 'TPE':
			error = 0
		elif predict == 'CmaEs':
			error = 0
		elif predict == 'Random':
			error = 0
		elif predict == 'Bayes':
			error = 0
		assert error == 0, 'Output optimizer is not defined' 

	for i in range(2):
		a = np.random.rand(1)
		b = np.random.rand(1)
		c = np.random.rand(1)
		d = np.random.rand(1)
		predict = random_forest_classifier(a,b,c,d)
		assert type(predict) == str, 'Output is not a string'
		if predict == 'TPE':
			error = 0
		elif predict == 'CmaEs':
			error = 0
		elif predict == 'Random':
			error = 0
		elif predict == 'Bayes':
			error = 0
		assert error == 0, 'Output optimizer is not defined' 
