def decision_tree_classifier(a,b,c,d):
    import numpy as np
    import pandas as pd
    from bayes_opt import BayesianOptimization
    import sklearn 
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.preprocessing import MinMaxScaler
    from sklearn.ensemble import BaggingClassifier, RandomForestClassifier, GradientBoostingClassifier
    from sklearn.metrics import r2_score, mean_squared_error, accuracy_score
    from sklearn import tree
    from sklearn.tree import DecisionTreeClassifier
    
    df = pd.read_excel('data/All Data combined.xlsx')
    df = df.drop(['Unnamed: 0'], axis=1)
    df = df.drop(['type_of_opt'], axis=1)
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
        MSE = mean_squared_error(y_test, yhat)
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

    estimator = DecisionTreeClassifier(max_depth=int(np.round(found_x)))
    clf = BaggingClassifier(base_estimator=estimator, n_estimators= int(np.round(found_y)))
    clf = clf.fit(x_train, y_train)
    yhat = clf.predict(x_test)
    acc = accuracy_score(y_test, yhat)
    x = np.array([a,b,c,d]).reshape(1,-1)
    predicted_class = clf.predict(x)
    
    return predicted_class
    