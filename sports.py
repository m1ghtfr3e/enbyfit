class Sport:
    '''
        Sport class

    Contains classes for several activities.
    '''
    class Running:
        '''
            Running class

        :param km_run: The distance which was run in km
        :type km_run: float
        :param time_sport: The duration of the activity in minutes
        :type time_sport: int
        '''
        def __init__(self, km_run=0.0, time_sport=0):
            self.km_run = km_run
            self.time_sport = time_sport

        def running(self, weight, ):
            return self.km_run * weight * 0.9

        def __str__(self):
            return ''' Kind of activity: Running '''

    class Walking:
        pass
