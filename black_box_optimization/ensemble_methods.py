def decision_tree_classifier(a,b,c,d):
    '''This function runs the decision_tree_classifier on the data'''
    import numpy as np
    import os 
    import pandas as pd
    from bayes_opt import BayesianOptimization
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.preprocessing import MinMaxScaler
    from sklearn.ensemble import BaggingClassifier
    from sklearn.metrics import accuracy_score
    from sklearn.tree import DecisionTreeClassifier
    if os.path.exists('data/All Data combined.xlsx'):
        df = pd.read_excel('data/All Data combined.xlsx')
    else:
        df = pd.read_excel('../data/All Data combined.xlsx')
    df = df.drop(['Unnamed: 0'], axis=1)
    df = df.drop(['Unnamed: 8'], axis=1)
    df = df.drop(['type_of_opt'], axis=1)
    df.dropna()
    df = df[df['accuracy [calc. max/ actual max]'] < 1.05]
    x = df[['number of trials','number of parameters','accuracy [calc. max/ actual max]', 'time per trial [s]']].values
    y = df['assigned_class']
    x_train, x_test, y_train, y_test = train_test_split(x, y,test_size=0.30)
    x_train = StandardScaler().fit(x_train).transform(x_train)
    x_test = StandardScaler().fit(x_test).transform(x_test)
    x_train = MinMaxScaler().fit(x_train).transform(x_train)
    x_test = MinMaxScaler().fit(x_test).transform(x_test)
    y_train = np.asarray(y_train)
    def func(x,y):
        estimator = DecisionTreeClassifier(max_depth= int(np.round(x)))
        clf = BaggingClassifier(base_estimator=estimator, n_estimators= int(np.round(y)))
        clf = clf.fit(x_train, y_train)
        yhat = clf.predict(x_test)
        acc = accuracy_score(y_test, yhat)
        return  acc
    xmin = 1
    xmax = 50
    ymin = 1
    ymax = 50
    pbounds = {'x': (xmin, xmax), 'y': (ymin, ymax)}
    optimizer = BayesianOptimization(f=func, pbounds=pbounds, verbose=3)
    optimizer.maximize(init_points = 20, n_iter = 30)
    best_params = optimizer.max["params"]
    found_x = best_params['x']
    found_y = best_params['y']
    max_value = func(found_x, found_y)
    print("Found x: {}, f: {}".format(found_x, (func(found_x, found_y))))
    print("Found y: {}, f: {}".format(found_y, (func(found_x, found_y))))
    print("Max value found is: {}".format(max_value))
    estimator = DecisionTreeClassifier(max_depth=int(np.round(found_x)))
    clf = BaggingClassifier(base_estimator=estimator, n_estimators= int(np.round(found_y)))
    clf = clf.fit(x_train, y_train)
    yhat = clf.predict(x_test)
    acc = accuracy_score(y_test, yhat)
    x = np.array([a,b,c,d]).reshape(1,-1)
    predicted_category_num = int(clf.predict(x)[0])
    if predicted_category_num == 0:
        predicted_category = 'CmaEs'
    elif predicted_category_num == 1:
        predicted_category = 'Random'
    elif predicted_category_num == 2:
        predicted_category = 'TPE'
    elif predicted_category_num == 3:
        predicted_category = 'Bayes'
    elif predicted_category_num == 4:
        predicted_category = 'PULP_CBC_CMD'
    return predicted_category

def random_forest_classifier(a,b,c,d):
    '''This function runs the random_forest_classifier on the data'''
    import numpy as np
    import pandas as pd
    import os 
    from bayes_opt import BayesianOptimization
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.preprocessing import MinMaxScaler
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import accuracy_score
    if os.path.exists('data/All Data combined.xlsx'):
        df = pd.read_excel('data/All Data combined.xlsx')
    else:
        df = pd.read_excel('../data/All Data combined.xlsx')
    df = df.drop(['Unnamed: 0'], axis=1)
    df = df.drop(['Unnamed: 8'], axis=1)
    df = df.drop(['type_of_opt'], axis=1)
    df.dropna()
    df = df[df['accuracy [calc. max/ actual max]'] < 1.05]
    x = df[['number of trials','number of parameters','accuracy [calc. max/ actual max]', 'time per trial [s]']].values
    y = df['assigned_class']
    x_train, x_test, y_train, y_test = train_test_split(x, y,test_size=0.30)
    x_train = StandardScaler().fit(x_train).transform(x_train)
    x_test = StandardScaler().fit(x_test).transform(x_test)
    x_train = MinMaxScaler().fit(x_train).transform(x_train)
    x_test = MinMaxScaler().fit(x_test).transform(x_test)
    y_train = np.asarray(y_train)
    
    def func(x,y):
        rfr = RandomForestClassifier(max_depth = int(np.round(x)), n_estimators = int(np.round(y)), max_features = 4)
        rfr = rfr.fit(x_train, y_train.flatten())
        yhat = rfr.predict(x_test)
        acc = accuracy_score(y_test, yhat)
        return acc
    
    xmin = 1
    xmax = 50
    ymin = 1
    ymax = 50
    pbounds = {'x': (xmin, xmax), 'y': (ymin, ymax)}
    optimizer = BayesianOptimization(f=func, pbounds=pbounds, verbose=3)
    optimizer.maximize(init_points = 20, n_iter = 30)
    best_params = optimizer.max["params"]
    found_x = best_params['x']
    found_y = best_params['y']
    max_value = func(found_x, found_y)
    print("Found x: {}, f: {}".format(found_x, (func(found_x, found_y))))
    print("Found y: {}, f: {}".format(found_y, (func(found_x, found_y))))
    print("Max value found is: {}".format(max_value))
    
    rfr = RandomForestClassifier(max_depth = int(np.round(found_x)), n_estimators = int(np.round(found_y)), max_features = 4)
    rfr = rfr.fit(x_train, y_train.flatten())
    yhat = rfr.predict(x_test)
    acc = accuracy_score(y_test, yhat)
    x = np.array([a,b,c,d]).reshape(1,-1)
    predicted_category_num = int(rfr.predict(x)[0])
    if predicted_category_num == 0:
        predicted_category = 'CmaEs'
    elif predicted_category_num == 1:
        predicted_category = 'Random'
    elif predicted_category_num == 2:
        predicted_category = 'TPE'
    elif predicted_category_num == 3:
        predicted_category = 'Bayes'
    elif predicted_category_num == 4:
        predicted_category = 'PULP_CBC_CMD'
    return predicted_category

