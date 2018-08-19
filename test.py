
import pylab as pl
import numpy as np
import PortfolioMatrixAlgebra
import DataProcessing



BTC = np.loadtxt("BTC-USD.csv", delimiter = ",",skiprows = 1,usecols = (5))  
ETC = np.loadtxt("ETC-USD.csv", delimiter = ",",skiprows = 1,usecols = (5))  
LTC = np.loadtxt("LTC-USD.csv", delimiter = ",",skiprows = 1,usecols = (5))  
BTC2 = np.loadtxt("BTC-USD2.csv", delimiter = ",",skiprows = 1,usecols = (5))  

Ln_return_BTC = DataProcessing.compute_ln_return (BTC  )
Ln_return_ETC = DataProcessing.compute_ln_return (ETC )
Ln_return_LTC = DataProcessing.compute_ln_return (LTC )
Ln_return_BTC2 = DataProcessing.compute_ln_return (BTC2  )


inputData = [BTC,ETC,BTC2,LTC]
Ln_return_input = [Ln_return_BTC,Ln_return_ETC,Ln_return_LTC,Ln_return_BTC2  ]

    

port = PortfolioMatrixAlgebra.PortfolioMatrixAlgebra (Ln_return_input, 0.001) 

port.report()

x = port.tangency_portfolio()[2]
y = port.globalMin_portfolio() 

DataProcessing.investment_report (x ,inputData)   
DataProcessing.investment_report (y ,inputData)   
