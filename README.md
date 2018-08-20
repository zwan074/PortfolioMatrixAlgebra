# PortfolioMatrixAlgebra

This is a simple calculation of Markowitz Portfolio method to find efficient portfolios,global minimum portfolios, tangency portfolios.
A testing function has also being provided to report the proposed return with differenct portfolios.

# Start with:

import pylab as pl
import numpy as np
import PortfolioMatrixAlgebra
import DataProcessing

# using np.loadtxt to load data from CSV and create 1D array e.g. [1,2,3 ......] format

BTC = np.loadtxt("BTC-USD.csv", delimiter = ",",skiprows = 1,usecols = (5))  
ETC = np.loadtxt("ETC-USD.csv", delimiter = ",",skiprows = 1,usecols = (5))  
LTC = np.loadtxt("LTC-USD.csv", delimiter = ",",skiprows = 1,usecols = (5))  
BTC2 = np.loadtxt("BTC-USD2.csv", delimiter = ",",skiprows = 1,usecols = (5))  

# using compute_ln_return function from DataProcessing file to transfer data into ln return

Ln_return_BTC = DataProcessing.compute_ln_return (BTC  )
Ln_return_ETC = DataProcessing.compute_ln_return (ETC )
Ln_return_LTC = DataProcessing.compute_ln_return (LTC )
Ln_return_BTC2 = DataProcessing.compute_ln_return (BTC2  )

# Create an array with different risky asset, not able to copy two same asset since inverse of covariance matrix would return error.
Ln_return_input = [Ln_return_BTC,Ln_return_ETC,Ln_return_LTC,Ln_return_BTC2  ]

# Initialise  PortfolioMatrixAlgebra class, with input of Ln_return_input and value of risk free asset (0.001)
port = PortfolioMatrixAlgebra.PortfolioMatrixAlgebra (Ln_return_input, 0.001) 

# Pring report of efficient frontier graph, efficient portfolios,global minimum portfolios, tangency portfolios.
port.report()

# Print profit and loss graph with proposed asset portfolio

x = port.tangency_portfolio()[2]
y = port.globalMin_portfolio() 

DataProcessing.investment_report (x ,inputData)   
DataProcessing.investment_report (y ,inputData)  
