import numpy as np
import matplotlib.pyplot as plt

myData = np.loadtxt("data.csv", delimiter=",", skiprows=1, usecols=(0), max_rows = 23, encoding="utf-8")    # Change max_rows according to length to ignore empty cells
generalData = np.loadtxt("data.csv", delimiter=",", skiprows=1, usecols=(1), encoding="utf-8")

rangeBins = np.array(range(0,401))/100
myDataAverage = np.average(myData)
myDataStdDev = np.std(myData)
generalDataAverage = np.average(generalData)
generalDataStdDev = np.std(generalData)

def gaussian(x, mu, sigma):
    return ((np.sqrt(2*np.pi)*sigma)*np.exp(-0.5 * ( (x-mu)/sigma )**2 ) )                                                           #1/(np.sqrt(2*np.pi)*sigma)* in front maybe?

plt.title("My K/D (μ={0:.2f}, σ={1:.2f}) vs. My Opponents' K/D (μ={2:.2f}, σ={3:.2f})".format(myDataAverage, myDataStdDev, generalDataAverage, generalDataStdDev))
plt.xlabel("K/D Ratio")
plt.ylabel("Count")
plt.hist(generalData, bins = rangeBins, label= "Opponents' K/D", color = "cyan")
plt.hist(myData, bins = rangeBins, label = "My K/D", color = "red")
plt.plot(generalData, gaussian(generalData, generalDataAverage, generalDataStdDev), color = "blue")
plt.plot(myData, gaussian(myData, myDataAverage, myDataStdDev), color = "orange")
plt.xlim(0,4)
plt.legend()
plt.show()

print(myData)
print(generalData)