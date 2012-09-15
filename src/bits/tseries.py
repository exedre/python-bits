

class tsidx(DatetimeIndex):
    pass
    

class timeseries(Series):
    def __init__(self,*args,**kwargs):
        """
%   A time series matrix (TSMAT) object is a MATLAB object that minimally
%   contains a data matrix, a frequency indicator and 
%   a start year and period  (henceforth called a tsidx).
%   The frequency and tsidx *must* be explicitly specified.  
%   In addition to these four items (start year and period, frequency, data) 
%   the time series can also contain a bunch of metadatas, which 
%   can be added separately with addmeta commands.
%
%   There is a single way to instantiate a TSMAT object
%   using the constructor.  It is:
%
%      TS = tsmat(YEAR,PERIOD,FREQ,DATAMATRIX);
%
%   TS = tsmat(YEAR,PERIOD,FREQ,DATAMATRIX) generates a time series object,TS.
%   The data in the input matrix needs to be of size 
%   T x N where T=number of periods, N=number of columns (individual time series).
%
%   For example:
%
%      t = tsmat(1980,1,12,rand([1 40])
%
%   You can specify the frequency indicator, FREQ, using these 
%    valid frequency indicators:
%
%      DAILY,      Daily,      daily,      D, d, 365
%      WEEKLY,     Weekly,     weekly,     W, w, 52
%      MONTHLY,    Monthly,    monthly,    M, m, 12
%      QUARTERLY,  Quarterly,  quarterly,  Q, q, 4
%      SEMIANNUAL, Semiannual, semiannual, S, s, 2
%      ANNUAL,     Annual,     annual,     A, a, 1
%   
%   You can even use some other frequencies as:
%       .5   One observation every two years
%       .25  One observation every four years
%       .125 One observation every eight years
%   or:
%        730  Twice a day
%       1460  Four times a day
%

        """

        # do kwargs treatment

        self.start_year = 0
        self.start_perios = 0
        self.freq = 0
        self.last_year = None
        self.last_period = None
        self.meta = {}
        self.data = []

        if isinstance(args[0],tseries):
            # copy constructor
            return tseries._copy_constructor(self,args[0])

        if isinstance(args[0],dict):
            return tseries._dict_constructor(self,args[0])
        
        if len(args)>3:
            # has data 
            self.data = args[3]
        
        if len(args)>2:
            # has freq else freq = 12
            self.freq = args[2]        

        if len(args)>1:
            # has min index else min index if fractional part of max index
            self.start_period = args[1]
            self.start_year = args[0]
        elif len(args)>0:        
            self.start_year,self.start_period = math.modf(args[0])

        self.start_index = "%s-%s" % (self.start_year,self.start_period)
        
        self.periods=len(self.data)
        
        date = period_index(self.start_index,periods=self.periods,freq=self.freq)
        
        # Name Management
        # a tseries has a name

        # Release Date Management
        # a tseries has a release date

        # Creation Date Management
        # a tseries has a creation date

        super(Series,self).__init__(self.data,index=date)

    def _copy_constructor(self,_ts,*args,**kwargs):
        pass

    def _dict_constructor(self,_dict,*args,**kwargs):
        pass

    
    def shift(self,periods=1,freq=None,copy=True,**kwds):
        """
        Shift the index of the Series by desired number of periods with an
        optional time offset
    
        Parameters
        ----------
        periods : int
           Number of periods to move, can be positive or negative
        freq : DateOffset, timedelta, or offset alias string, optional
           Increment to use from datetools module or time rule (e.g. 'EOM')
           if None use tseries freq
    
        Returns
        -------
        shifted : Series

        """
        if not freq:
            freq = self.freq
        return Super(Series,self).shift(periods,freq=freq,copy=copy,**kwds)

    
