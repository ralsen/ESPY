import machine

class Timers():
    timers = {}
    id = 0
    is_running = False
    def __init__(self):
        print(f"Timer class initialized.")
        timers = {}   
        self.is_running = False
        
    def append(self, name, period, callback=None):
        while self.is_running:
            print("waiting in append()")
            pass
        self.is_running = True
        print(f"Timer <{name}> initialized with ID = {self.id} ...")
        self.timers[name] = {
            'id': self.id,
            'instance': machine.Timer(self.id),
            'name': name
        }
        if callback == None:
            print ('downcounter: ')
            self.timers[name]['callback'] = lambda x: self.downCnt(name)
            self.timers[name]['downCnt'] = period
            period = 10
        else:
            self.timers[name]['callback'] = callback
            self.timers[name]['period'] = period
            self.timers[name]['downCnt'] = -1
        self.timers[name]['instance'].init(
            period=period, 
            mode=machine.Timer.PERIODIC, 
            callback= self.timers[name]['callback']
            )
        self.id += 1
        self.is_running = False
        return self.timers[name]
       
    def stop(self, timer):  
        while self.is_running:
            print("waiting in stop()")
            pass
        self.is_running = True
        print(f"stopping timer <{timer['name']}>")
        timer['instance'].deinit()
        ret = self.timers.pop(timer['name'], None)
        self.is_running = False
        return ret
    
    def downCnt(self, name):
        while self.is_running:
            print("waiting in downCnt()")
            pass
        self.is_running = True
        try:
            if self.timers.get(name) and self.timers[name].get('downCnt'):
                self.timers[name]['downCnt'] -= 1
        except Exception as e:
            print(f"Error in downCnt: {e}")
        finally:
            self.is_running = False        