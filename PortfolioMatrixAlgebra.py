import pylab as pl
import numpy as np
from operator import inv



class PortfolioMatrixAlgebra:
        
    def __init__ (self, data,risk_free ):
        self.input_data = data
        self.sigma = np.cov(self.input_data)
        
        mu1 = np.average (self.input_data,axis = 1 )
        mu2 = np.zeros  (( len (mu1),1 ))
        for i in range (len(mu1)) :
            mu2 [i] = mu1 [i]
        
        self.mu = mu2
        self.target_return = np.max (self.mu)
        self.risk_free = risk_free
        
    def globalMin_portfolio (self ):
        ones = np.ones (( len (self.input_data ) ,1 ) )
        sigmaInv = np.linalg.inv (self.sigma )  
        m = np.dot (sigmaInv , ones) / np.dot ( np.dot (ones.transpose(), sigmaInv ), ones ) 
        
        return m
                
        

    def tangency_portfolio(self):
        ones = np.ones (( len (self.input_data ) ,1 ) )
        sigmaInv = np.linalg.inv (self.sigma )
        t = sigmaInv .dot ( self.mu - self.risk_free * ones) / ones.transpose() .dot (sigmaInv .dot ( self.mu - self.risk_free * ones))
        t_mu = t.transpose() .dot (self.mu)
        t_mu_rf = t_mu - self.risk_free
        t_sig = t.transpose() .dot (self.sigma) .dot(t)
        t_sd = t_sig ** 0.5
        t_slope = t_mu_rf / t_sd
        tan_rf_mu = np.zeros ((20,1))
        tan_rf_sd = np.zeros ((20,1))
        
  
        for i in range ( 20) :
            tan_rf_mu[i] = self.risk_free + i * t_mu_rf * 0.1
            tan_rf_sd[i] = i * t_sd * 0.1
        
        return tan_rf_sd,tan_rf_mu,t,t_slope

    def efficient_portfolio(self    ):
        ones = np.ones ( (len (self.input_data ) ,1) )
        M = np.hstack ( (self.mu, ones))
        B = M.transpose() .dot (np.linalg.inv (self.sigma )).dot (M)
        mu_targeted = np.vstack ((self.target_return,1))
        x = np.linalg.inv (self.sigma ) .dot( M ) .dot (np.linalg.inv(B)) .dot (mu_targeted)
        
        return x


    def efficient_frontier(self , alpha_min = -2,alpha_max = 1.5):
        m = self.globalMin_portfolio()
        m_return = m.transpose () .dot (self.mu)
        m_sig = m.transpose() .dot ( self.sigma).dot ( m)
        
        n = self.efficient_portfolio()
        n_return = n.transpose () .dot (self.mu)
        n_sig = n.transpose() .dot (self.sigma) .dot (n)
        n_cov = m.transpose() .dot (self.sigma) .dot (n)
        
        a = np.arange (alpha_max,alpha_min - 0.1 , -0.1 )
        z = np.zeros ( ( int ( (alpha_max - alpha_min) * 10 +1  ) , len(m))  )
        mu_z = np.zeros ( (int ((alpha_max - alpha_min) * 10 +1 ),1) )
        sig_z = np.zeros ( (int ((alpha_max - alpha_min) * 10 +1 ),1) )
        sd_z = np.zeros  ( (int ((alpha_max - alpha_min) * 10 +1 ),1) )
       
        for i in range (len(a) ) :
            mu_z[i] = a[i] * m_return + (1-a[i]) * n_return
            sig_z[i] = a[i]**2 *  m_sig + (1-a[i]) **2 * n_sig + 2 * a[i] * (1-a[i]) * n_cov
            sd_z[i] = sig_z[i] ** 0.5
            z[i,] = (a[i] * m + (1-a[i]) * n).transpose()
        
        return sd_z,mu_z,z   
    
    def report (self):
        
        print ('Number of Risky Asset: ', len(self.input_data))
        print ('Risk free Asset value: ',self.risk_free )
        print ('Globale Minimum Portfolio: ', self.globalMin_portfolio().transpose()  )
        print ('Tangency Portfolio: ', self.tangency_portfolio()[2].transpose())
        print ('Tangency Portfolio Slope: ', self.tangency_portfolio()[3])
        
        pl.plot (self.efficient_frontier()[0],self.efficient_frontier()[1]) 
        pl.plot (self.tangency_portfolio()[0],self.tangency_portfolio()[1]) 
        pl.show()
        
    
                        