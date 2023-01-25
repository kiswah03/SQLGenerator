from textblob.classifiers import NaiveBayesClassifier
train_data_query = [
    ('which department does smith manage', 'employee'),
    ('what is the name of manager of finance department', 'employee'),
    ('which department does smith work in', 'employee'),
    ('how many hours has smith worked in project p2', 'project'),
    ('Which all projects does smith works in', 'project'),
    ('where is fridge project located', 'project'),
] 
test_data = [
    ('Its a fantastic series', 'pos'),
    ('Never watched such a brillent movie', 'pos'),
    ("horrible acting", 'neg'),
    ("It is a Wonderful movie", 'pos'),
    ('waste of money', 'neg'),
    ("Send me ", 'select'),
    ("Get the last name, job title, city and phone number of all employees who live in either Seattle or Kirkland,"
     "and have a phone number that starts with (206) and works as Sales Representatives","select")
]
classifier = NaiveBayesClassifier(train_data_query)
print(classifier.classify("how many employees work in sales department"))

classifier.show_informative_features(3)