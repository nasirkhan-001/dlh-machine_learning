#!/usr/bin/env python3
"""This module creates a class exponential"""


class Exponential:
    """This class represents an exponential distribution"""
    # if data is given, the lambtha is calculated from data,
    # else it will be provided by the user, by default lambdha is 1.0
    # lambtha is the rate of events occure for given time
    # while λ is rate paraemter and is λ = 1/mean for exponential. DF
    # time matter in this distribution, its a continous random variable
    # e.g. waiting time for call, bus, failure, accident
    # focus is to find probabiltiy of waiting time untill next event
    # that why decay used (-lambdha in exponent) in Exp.Dist.Func.
    # becuase possibility of still wating will get decrease over time
    # not time itself
    # whats the probability that next emails will arive within 10mins
    # probability that next emails will arive in 10mins = not possible
    # becuase time is continous random variable and probability of
    # time itself at specific point in time in future is not possible
    # core concept difference is waiting time vs time
    # finance. e.g. prob of time btw no of trades, of time btw credit default
    # how long it will take that next trade/default will occure
    # find probability of waiting time for given interval of time
    def __init__(self, data=None, lambtha=1.):
        """constructor method."""
        # attaching data to object "self or P1, P2 per checker file"
        self.data = data
        self.lambtha = float(lambtha)
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
        if data is not None:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                Sum = 0
                for i in range(len(data)):
                    Sum += data[i]
            # lambdha = 1/mean for exponential DF
            self.lambtha = 1 / (Sum / len(data))

    def pdf(self, x):
        """find PDF where dansity=likelihood for give time period."""
        if x < 0:
            return 0
        else:
            # calculate PDF using the formula: (lambdha * e^-lambtha.Time)
            e = 2.7182818285
            pdf = ((self.lambtha) * e ** ((-self.lambtha) * x))
            return pdf
