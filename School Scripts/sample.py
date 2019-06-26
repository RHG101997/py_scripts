import math

class Sample:

    '''
    This class creates a sample out of
    an array on numbers
    contains:
        •Mean
        •SEM
        •Variance
        •percentile
        •Standard Diviation
    '''

    def __init__(self,sample):
        self.sample = sample
        self.sampleSize = len(sample)
        self.sampleSorted = sorted(self.sample)
  
    def getSum(self):
        sum = 0
        for n in self.sample:
            sum += n
        return sum
    # is the sum of the numbers in the sample, 
    # divided by how many there are
    def mean(self): 
        return self.getSum()/self.sampleSize

    # The deviation is the difference between given sample value 
    # and the sample mean
    def deviation(self, x):
        return x- self.mean()
    
    def sqDeviation(self, x):
        return (self.deviation(x)**2)


    
    def variance(self):
        '''
        A measure of spread of sample data is the sample 
        variance:
        '''
        sumDeviation = 0
        for n in self.sample:
            sumDeviation += self.sqDeviation(n)
        return sumDeviation / (self.sampleSize-1)

    # The standard deviation (often represented by letter σ) measures the amount
    # of variation or dispersion from the mean
    def standardDeviation(self, variance):
        '''
        A low standard deviation indicates that the data points tend to be very close
        to the mean (also called expected value); a high standard deviation indicates
        that the data points are spread out over a large range of values
        '''
        return math.sqrt(variance)

    def median(self):
        '''
        The sample median is the middle value in an ordered sequence of the sample
        values. 
        '''

        sampleSorted = self.sampleSorted

        if self.sampleSize%2 == 0:
            # if sample size is even use: average of -> (n/2) , (n+1)/2
            # [this are index so they need to be substracted by 1 cz arrays begin at 0]
            return self.getAverage([sampleSorted[int(self.sampleSize/2)-1],sampleSorted[int((self.sampleSize/2))]])
        else:
            # if sample size is odd use: (n+1)/2 -> to get meadian value
            return sampleSorted[int((self.sampleSize+1)/2)-1]


    def getAverage(self, num):
        '''
        Get the average of a list or array
        '''
        sum= 0
        for n in num:
            sum +=n
        return sum/len(num)


    def percentile(self, p):
        '''
        The p-th percentile of a sample, for a number p between
        0 and 100, divides the sample so that as nearly as possible
        p% of the sample values are less than the p-th percentile,
        and (100% – p%) are greater
        Formula  (p/100)(n + 1)
        '''
        percentile = (p/100)*(self.sampleSize+1)
        if isinstance(percentile, int):
            return percentile
        return self.getAverage([self.sampleSorted[math.floor(percentile-1)],self.sampleSorted[math.floor(percentile+1)-1]])

     
    def standardErrorMean(self):
        '''
        The standard error of the mean (SEM) is equal to the
        standard sample deviation s divided by the square root of
        the sample size (n)
        SEM = s/sqrt(n)
        '''
        return self.mean() / math.sqrt(self.sampleSize)

    


    def printInfo(self):
        print("--------------------------------------------------")
        print("Sample: " + str(self.sample))
        print("Sample Sorted: " + str(self.sampleSorted))
        print("--------------------------------------------------")
        print("Size(n): " + str(self.sampleSize))
        print("Mean: " +  str(round(self.mean(), 2)))
        print("Variance: " + str(round(self.variance(),2)))
        print("Standard Deviation: " + str(round(self.standardDeviation(self.variance()),2)))
        print("SEM(Standard Error Mean): " + str(round(self.standardErrorMean(),2)))
        print("--------------------------------------------------")
        print("1rs Quartile: " + str(self.percentile(25)))
        print("Median(2nd Quartile): " + str(self.median()))
        print("3rd Quartile: " + str(self.percentile(75)))
        print("--------------------------------------------------")
        

def test():
    # a = [ 72.30, 68.31, 67.05, 70.68]
    # a = [65.51, 72.30, 68.31, 67.05, 70.68]
    # a =[1,2,3,4,20]
    # a = [30, 75, 79, 80, 80, 105, 126, 138, 149, 179, 179, 191, 223, 232, 232,
    # 236, 240, 242, 245, 247, 254, 274, 384, 470]
    a = [2, 3, 5, 6, 7, 9, 9, 11, 12, 15]

    sample = Sample(a)
    sample.printInfo()

