from sklearn import tree #importing decision tree 
features = [[140,1], [130,1], [150,0], [170,0]] #first the weight and 1 for smooth 0 for bumpy
labels = [0, 0, 1, 1] #0 for orange 1 for apple
clf = tree.DecisionTreeClassifier() #clf is an instance of decision tree classifier
clf = clf.fit(feautures, labels) #trains the decision tree using given features and labels
print clf.predict([[150, 0]]) #asks decision tree to predict label of new data point
