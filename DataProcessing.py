import numpy as np
import pylab as pl

def compute_ln_return ( data ):
    ln_return = np.zeros(len(data)-1 )
    ln_return = data[1:]

    return np.log ( data [0:len(data)-1 ] / ln_return)

def investment_report ( x ,initial_investment , data ) :    
    
    balance = np.zeros( len(data[0]))
    balance[0] = initial_investment
    
    for i in range (len(balance)):
        for j in range (len(x)):
            balance[i] = balance[i] +  data[j][i] / ( balance[i-1] * x[j] )
        balance[i] = balance[i] - initial_investment  
        
    print ('Risk for this portfolio is: ', np.std(balance)) 
    
    pl.plot(balance )
    pl.show()
