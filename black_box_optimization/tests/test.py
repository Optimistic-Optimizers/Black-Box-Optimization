#testing the test 
def test_ensemble_methods():
	'''Runs several tests on the function'''
	from ensemble_methods import decision_tree_classifier
	predict = decision_tree_classifier(1,1,1,1)
	assert type(predict) == str, 'Output is not a string'
