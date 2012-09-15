import unittest

import numpy as np
from bits import timeseries

v = np.array([
    [ 0.4639,0.7878,0.4580,0.3559, ],
    [ 0.3154,0.9871,0.0924,0.7414,  ],
    [ 0.1466, 0.3632, 0.2711, 0.0494, ],
    [ 0.9527, 0.3546, 0.5507, 0.0325, ],
    [ 0.4159, 0.5354, 0.4563, 0.9488, ],
    [ 0.3341, 0.0674, 0.8936, 0.9819, ],
    [ 0.4350, 0.2618, 0.8961, 0.6589, ],
    [ 0.4250, 0.7027, 0.4737, 0.9558, ],
    [ 0.8357, 0.1027, 0.7569, 0.9778, ],
    [ 0.0845, 0.6533, 0.7428, 0.2288, ],
    [ 0.2687, 0.6348, 0.3721, 0.5872, ],
    [ 0.3120, 0.6766, 0.1626, 0.1015 ]])



class TestTimeseries(unittest.TestCase):

    def test_init_err_freq(self):
        pass

    def test_init_err_period(self):
        # negative
        # greater than freq
        pass

    def test_init_err_data(self):
        pass
    
    def test_init_base_366(self):
        ts = timeseries(2000,1,366,np.random.randn(733))

    def test_init_base_53(self):
        ts = timeseries(2000,1,366,np.random.randn(733))
        
    def test_init_copy_1(self):
        pass

    def test_init_dict_1(self):
        pass

    def test_init_name_1(self):
        pass

    def test_init_releases_1(self):
        pass

    def test_extend_0(self):
        ts1 = timeseries(1980,1,12,v[:,0:1])
        ts2 = timeseries(1981,4,12,v[:,0:1])
        ts31 = pd.merge(ts1,ts2)
        ts32 = tsmerge(ts1,ts2)
        ts33 = ts1.join(ts2)
        ts34 = ts2.join(ts2)
