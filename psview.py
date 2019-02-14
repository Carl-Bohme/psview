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

def RunningThreadsInProcess(pid):
    proc = psutil.Process(pid)
    threads = proc.threads()
    numThreads = proc.num_threads()
    for thread in threads:
        print(thread)
    print('Number of threads: {}'.format(numThreads))

def LoadedModulesInProcess(proc):
    return

def ExecutablePagesInProcess(proc):
    return

def MemoryInfo(pid):
    proc = psutil.Process(pid)
    print(proc.memory_info())

def main():
    parser = argparse.ArgumentParser(description="Defense Against the Dark Arts!")
    parser.add_argument("-p", "--enum_proc", help="enumerate all the running processes", action="store_true")
    parser.add_argument("-t", "--threads", type=int, metavar="pid", help="list all running threads within process boundry")
    parser.add_argument("-m", "--mem_info", type=int, metavar="pid", help="Read the memory")

    args = parser.parse_args()
    if args.enum_proc:
        EnumRunningProcesses()
    elif args.threads:
        RunningThreadsInProcess(args.threads)
    elif args.mem_info:
        MemoryInfo(args.mem_info)

    
if __name__ == "__main__":
    main()
