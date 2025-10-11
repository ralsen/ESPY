import sys
import time
import gc

class Logger:
    LOG_LEVELS = {"DEBUG": 10, "INFO": 20, "WARN": 30, "ERROR": 40}
    _instances = {}  # interne Sammlung der Logger pro Modul

    def __init__(self, name, level="INFO", logfile=None):
        self.name = name
        self.current_level = self.LOG_LEVELS.get(level.upper(), 20)
        self.logfile = logfile

    @classmethod
    def getLogger(cls, name, level="INFO", logfile=None):
        """Liefert pro Modul einen eigenen Logger (Singleton-artig)"""
        if name not in cls._instances:
            cls._instances[name] = cls(name, level, logfile)
        return cls._instances[name]

    def set_level(self, level):
        self.current_level = self.LOG_LEVELS.get(level.upper(), 20)

    def set_logfile(self, path):
        self.logfile = path

    def _now(self):
        try:
            t = time.localtime()
            return f"{t[3]:02d}:{t[4]:02d}:{t[5]:02d}"
        except:
            return "00:00:00"

    def _caller(self):
        try:
            frame = sys._getframe(3)  # 3 Ebenen hoch: log() -> info() -> Aufrufer
            filename = frame.f_code.co_filename.split("/")[-1]
            lineno = frame.f_lineno
            return filename, lineno
        except Exception as e:
            #print (f"Fehler in _caller(): {e}")
            return "-", 0

    def _write(self, line):
        print(line)  # immer Konsole
        if self.logfile:
            try:
                with open(self.logfile, "a") as f:
                    f.write(line + "\n")
            except Exception as e:
                print("Fehler beim Schreiben in Logdatei:", e)

    def log(self, level, msg):
        if self.LOG_LEVELS[level] >= self.current_level:
            #filename, lineno = self._caller()
            line = f"{self._now()} :: {level:5s} :: [{self.name:10s}] :: {msg}"
            self._write(line)
            gc.collect()

    # Komfort-Methoden:
    def debug(self, msg): self.log("DEBUG", msg)
    def info(self, msg):  self.log("INFO", msg)
    def warn(self, msg):  self.log("WARN", msg)
    def error(self, msg): self.log("ERROR", msg)
