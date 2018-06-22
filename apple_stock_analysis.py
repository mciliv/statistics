'''
    Morgan Ciliv
    Statistics
    
    Stock assignment - Using Apple, Inc.
    - Uses 30 data points with delta t = 1/252 days
    - Calculates mu and sigma for the Cox-Ross-Rubenstein Model
    - Create a 3-period model for the future stock prices
    - Calculate interesting probability related to future stock prices
    
    Yahoo stock code given and inspired by "Mr_Spock" on...
    http://stackoverflow.com/questions/34124992/how-can-i-store-the-historical
    -stock-prices-using-an-array
'''

from yahoo_finance import Share
import math

# Variables given
T = 252
delta_t = 1.0 / 252.0
n = 30 - 1 # 30 is the total number of prices

# Define which stock to use and the time interval
stock = Share('AAPL')
start_date = '2017-03-13'
end_date = '2017-04-24'

# Obtain the prices array
closes = [c['Close'] for c in stock.get_historical(start_date, end_date)]
i = n
prices = [0.0] * 30
for c in closes:
    prices[i] = float(c)
    i -= 1

# Create the vector y
y = [0.0] * 29
for i in range(n):
    y[i] = math.log(prices[i + 1] / prices[i]) # i starts at 0, so i + 1, i

# Calculate mu
mu = (1.0 / delta_t) * (1.0 / n) * math.log(prices[n] / prices[0]) # All floats
print "Mu:", mu

# Calculate sigma
sum = 0
for i in range(n):
    sum += (y[i] - mu * delta_t) ** 2.0 # ** = ^
sigma = math.sqrt((1.0 / delta_t) * (1.0 / (n - 1)) * sum) # All floats
print "Sigma:", sigma, "\n"

# Calculate up and down values
u = math.exp( sigma * math.sqrt(delta_t) + mu * delta_t)
d = math.exp(-sigma * math.sqrt(delta_t) + mu * delta_t)
print "u:", u
print "d:", d, "\n"

# Calculate future stock prices s1 - s10
# s1 is the last value in our data set
s1 = prices[n]
print "s1:", s1,"\n"

# 2nd layer
s3 = u * s1
s2 = d * s1
print "s3:", s3
print "s2:", s2, "\n"

# 3rd layer
s6 = (u ** 2) * s1
s5 = (u * d) * s1
s4 = (d ** 2) * s1
print "s6:", s6
print "s5:", s5
print "s4:", s4, "\n"

# 4th layer
s10 = (u ** 3) * s1
s9 = (u ** 2) * d * s1
s8 = u * (d ** 2) * s1
s7 = (d ** 3) * s1
print "s10:", s10
print "s9:", s9
print "s8:", s8
print "s7:", s7, "\n"

# Calculation used for calculating an interesting probability
x_num = math.log(146.0 / s1) - 3.0 * (mu * delta_t - sigma * math.sqrt(delta_t))
x_den = 2 * sigma * math.sqrt(delta_t)
x = x_num / x_den
print "x: ", x, "\n"
