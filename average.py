
from math import *


def average(spike_trains,tau):

    class Delta_error:
        def __init__(self,spike_trains,tau):
            self.n=len(spike_trains)
            self.big_train=[]
            for train in spike_trains:
                self.big_train=self.big_train+train
            self.centre_train=[]
            self.tau=tau
            self.min=min(self.big_train)
            self.max=max(self.big_train)

        def add_spike(self,time):
            self.centre_train.append(time)
            

        def minimize(self):
            value=1.0
            time=self.min

            for spike in self.big_train:
                new_value=self.__call__(spike)
                if new_value<value:
                    value=new_value
                    time=spike
            return time
            
        def sort(self):
            self.centre_train.sort()
            
        def __call__(self,time):

            cross1=0.0
            for centre_time in self.centre_train:
                cross1+=exp(-fabs(centre_time-time)/self.tau)
            cross2=0.0
            for big_time in self.big_train:
                cross2+=exp(-fabs(big_time-time)/self.tau)

            return 1.0+2.0*cross1-2.0/self.n*cross2

        
    delta_error=Delta_error(spike_trains,tau)
    train_length=len(delta_error.big_train)/len(spike_trains)

        
    for spike_c in range(0,train_length):
        new_spike = delta_error.minimize()
        delta_error.add_spike(new_spike)
        
    delta_error.sort()
    return delta_error.centre_train






    


