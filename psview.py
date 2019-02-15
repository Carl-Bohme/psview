import argparse
import psutil
import os

def EnumRunningProcesses():
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'status', 'username'])
        except psutil.NoSuchProcess:
            pass
        else:
            if pinfo['status'] == psutil.STATUS_RUNNING:
                print(pinfo)

def RunningThreadsInProcess(pid):
    proc = psutil.Process(pid)
    threads = proc.threads()
    numThreads = proc.num_threads()
    for thread in threads:
        print(thread)
    print('Number of threads: {}'.format(numThreads))

def LoadedModulesInProcess(pid):
    proc = psutil.Process(pid)
    mem_map = proc.memory_maps()
    for map in mem_map:
        print(map)

def ExecutablePagesInProcess(proc):
    return

def MemoryInfo(pid):
    proc = psutil.Process(pid)
    print(proc.memory_info())

def main():
    parser = argparse.ArgumentParser(description="Defense Against the Dark Arts!")
    parser.add_argument("-p", "--enum_proc", help="enumerate all the running processes", action="store_true")
    parser.add_argument("-t", "--threads", type=int, metavar="pid", help="list all running threads within process boundry")
    parser.add_argument("-l", "--loaded_modules", type=int, metavar="pid", help="View loaded modules inside a process")
    parser.add_argument("-m", "--mem_info", type=int, metavar="pid", help="Read the memory")

    args = parser.parse_args()
    if args.enum_proc:
        EnumRunningProcesses()
    elif args.threads:
        RunningThreadsInProcess(args.threads)
    elif args.loaded_modules:
        LoadedModulesInProcess(args.loaded_modules)
    elif args.mem_info:
        MemoryInfo(args.mem_info)

    
if __name__ == "__main__":
    main()
