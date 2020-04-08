class Timer:
    def __init__(self, name):
        self.name = name
        self.timestamp = time.time()
        self.seconds_passed = 0
        self.is_timing = False
        #get from database if name exists in database
        #else add to database

    def start(self):
        #set current time as timestamp in database
        #set is_timing local and in database to True
        pass

    def stop(self):
        #Get timestamp from database
        #set seconds_passed to current_time - timestamp
        #set is_timing to False
        #update everything to database
        pass

    def reset(self):
        #Set self.seconds_passed to zero
        pass

    def read(self):
        #Get timestamp from database
        #if is_timing: subtract timestamp from current time
        #else print seconds_passed retrieved from database
        pass