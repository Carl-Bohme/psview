import argparse
import psutil

def EnumRunningProcesses():
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
        except psutil.NoSuchProcess:
            pass
        else:
            print(pinfo)

def RunningThreadsInProcess(proc):
    return

def LoadedModulesInProcess(proc):
    return

def ExecutablePagesInProcess(proc):
    return

def MemoryInfo():
    return

def main():
    parser = argparse.ArgumentParser(description="Defense Against the Dark Arts!")
    parser.add_argument("-p", "--enum_proc", help="Enumerate all the running processes", action="store_true")

    args = parser.parse_args()
    if args.enum_proc:
        EnumRunningProcesses()
    
if __name__ == "__main__":
    main()
