#Libraries
from math import sqrt
from random import seed
from random import randrange
from csv import reader
from math import sqrt
import matplotlib.pyplot as plt



class ML():
    def __init__(self):
        #Operations will be counted in this variable
        self.op = 0

    def addOp(self,val):
        self.op += val

    # Calculate the mean value of a list of numbers
    def mean(self,values):
        self.addOp(len(values) + 1)
        return sum(values) / float(len(values))

    # Calculate the variance of a list of numbers
    def variance(self,values, mean):
        self.op += len(values) + 1 # each value subs the mean
        return sum([(x-mean)**2 for x in values])

        
    # Calculate covariance between x and y
    def covariance(self,x, mean_x, y, mean_y):
        covar = 0.0
        for i in range(len(x)):
            self.addOp(3) # 2xsubs 1xMult
            covar += (x[i] - mean_x) * (y[i] - mean_y)
        return covar


    # Calculate coefficients
    def coefficients(self,dataset):
        x = [row[0] for row in dataset]
        y = [row[1] for row in dataset]
        x_mean, y_mean = self.mean(x), self.mean(y)
        b1 = self.covariance(x, x_mean, y, y_mean) / self.variance(x, x_mean)
        b0 = y_mean - b1 * x_mean
        self.addOp(2) #b0 subs mult
        return [b0, b1]

    def yPredict(self, x):
        return self.b0 + self.b1 * x # y=mx+b

    def simple_linear_regression(self, train, test):
        predictions = list()
        #get coefficients
        self.b0, self.b1 = self.coefficients(train)
        for row in test:
            yhat = self.yPredict(row[0])
            self.addOp(2)# add mult
            predictions.append(yhat)
        return predictions




    # Evaluate regression algorithm on training dataset
    def evaluate_algorithm(self, dataset, algorithm, split, *args):
        train, test = self.train_test_split(dataset, split)
        test_set = list()
        for row in test:
            row_copy = list(row)
            row_copy[-1] = None
            test_set.append(row_copy)
        predicted = algorithm(train, test_set, *args)
        actual = [row[-1] for row in test]
        rmse = self.rmse_metric(actual, predicted)
        self.plotData(dataset,[row[0] for row in test],predicted)
        return rmse

    # Split a dataset into a train and test set
    def train_test_split(self,dataset, split):
        train = list()
        train_size = split * len(dataset)
        dataset_copy = list(dataset)
        while len(train) < train_size:
            index = randrange(len(dataset_copy))
            train.append(dataset_copy.pop(index))
        return train, dataset_copy

    # Calculate root mean squared error
    def rmse_metric(self,actual, predicted):
        sum_error = 0.0
        for i in range(len(actual)):
            prediction_error = predicted[i] - actual[i]
            sum_error += (prediction_error ** 2)
        mean_error = sum_error / float(len(actual))
        return sqrt(mean_error)
    
    def plotData(self,dataset,inputs,predicted):
        # Data points
        x =[]
        y =[]
        bY = 0 # highest Y value
        bX = 0 # highest Y value
        for i in dataset:
            bX = i[0] if i[0] > bX else bX
            bY = i[1] if i[1] > bY else bY
            x.append(i[0])
            y.append(i[1])
        plt.scatter(x,y)
        print(bY)
        # Predition points
        plt.scatter(inputs,predicted, linestyle='dashed', color='orange')
        # Best fit oline
        plt.plot([bX,bY], [self.yPredict(bX),self.yPredict(bY)], linestyle='dashed', color='red')
        plt.show()


# Load a CSV file
def load_csv(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	return dataset
    
# Convert string column to float
def str_column_to_float(dataset, column):
	for row in dataset:
		row[column] = float(row[column].strip())






# Test simple linear regression
ml = ML()
ml.op = 0
# Simple linear regression on insurance dataset
# seed(1)
filename = 'data.csv'
dataset = load_csv(filename)
for i in range(len(dataset[0])):
	str_column_to_float(dataset, i)
split = 0.8
rmse = ml.evaluate_algorithm(dataset, ml.simple_linear_regression, split)
print('\nOperations: ' + str(ml.op))
print('RMSE: %.3f' % (rmse))



