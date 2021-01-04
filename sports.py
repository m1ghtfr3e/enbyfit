
class Sport:
    '''
        Sport class

    Contains classes for several activities.

    :class: Running
    :class: Walking
    '''

    class Running:
        '''
            Running class

        :param body: Instance of an object which has
                         needed parameters
        :type body: class
        :param km_run: The distance which was run in km
        :type km_run: float
        :param time_sport: The duration of the activity in minutes
        :type time_sport: int
        '''
        def __init__(self, body, km_run=0.0, time_sport=0):
            self.__body = body
            self.km_run = km_run
            self.time_sport = time_sport

        def calories_used(self):
            '''
            # Add Informations
            '''
            return self.km_run * self.__body._weight * 0.9

        def run_pace(self):
            '''
            # Add Informations
            '''
            tmp = self.time_sport / self.km_run
            t = tmp - int(tmp)
            t *= 60   # to get minutes
            pace = int(tmp) + (t - int(t))
            return float('%.2f' % pace)

        def __str__(self):
            return f'''
            Kind of activity: Running

            Duration: {self.time_sport} min
            Distance: {self.km_run} km
            Speed:  {self.run_pace()} min/km
            Calories used:  {self.calories_used()}
             '''

    class Walking:
        def __init__(self):
            pass

        @classmethod
        def show(cls):
            return Sport.myvar

        def __str__(self):
            pass
