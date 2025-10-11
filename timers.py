import machine
import time

from logger import Logger
#log = Logger.getLogger(__name__, level="INFO", logfile="/log.txt")
log = Logger.getLogger(__name__)
class Timers():
    timers = {}
    id = 0
    is_running = False
    def __init__(self):
        self.is_running = False
        log.info("Timers class initialized")        
    def append(self, name, period, callback=None):
        while self.is_running:
            log.info("waiting in append()")

        self.is_running = True
        log.info(f"Timer <{name}> (ID = {self.id}) initialized with period {period}.")
        self.timers[name] = {
            'id': self.id,
            'instance': machine.Timer(-1),
            #'instance': machine.Timer(self.id),
            'name': name
        }
        if callback is None:
            log.info ('downcounter: ')
            self.timers[name]['callback'] = lambda x: self.downCnt(name)
            self.timers[name]['downCnt'] = period
            period = 10
        else:
            self.timers[name]['callback'] = callback
            self.timers[name]['period'] = period
            self.timers[name]['start'] = time.ticks_ms() + period
            
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
            log.info("waiting in stop()")
        self.is_running = True
        log.info(f"stopping timer <{timer['name']}>")
        timer['instance'].deinit()
        ret = self.timers.pop(timer['name'], None)
        self.is_running = False
        return ret
    def stopall(self):
        while self.is_running:
            log.info("waiting in stopall()")
        self.is_running = True
        log.info("stopping all timers")
        for name, timer in list(self.timers.items()):
            log.info(f"stopping timer <{name}>")
            timer['instance'].deinit()
            self.timers.pop(name, None)
        self.is_running = False
        
    def downCnt(self, name):
        while self.is_running:
            log.info(f"waiting in downCnt() for timer: <{name}")
        self.is_running = True
        try:
            if self.timers.get(name) and self.timers[name].get('downCnt'):
                self.timers[name]['downCnt'] -= 1
        except Exception as e:
            log.info(f"Error in downCnt: {e}")
        finally:
            self.is_running = False      
            
    def remain(self, timer):
        return int((timer['start'] - time.ticks_ms()) / 1000)  