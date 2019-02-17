#!/usr/bin/python
import argparse
import psutil
import subprocess

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
    p1 = subprocess.Popen(['lsof', '-p', str(pid), '-w'], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(['grep', '\.so'], stdin=p1.stdout)
    p1.stdout.close()
    p2.communicate()

def ExecutablePagesInProcess(pid):
    p1 = subprocess.Popen(['pmap', str(pid)], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(['grep', '\-x\-'], stdin=p1.stdout)
    p1.stdout.close()
    p2.communicate()

def MemoryInfo(pid):
    #undefined

def main():
    parser = argparse.ArgumentParser(description="Defense Against the Dark Arts!")
    parser.add_argument("-p", "--enum_proc", help="enumerate all the running processes", action="store_true")
    parser.add_argument("-t", "--threads", type=int, metavar="pid", help="list all running threads within process boundry")
    parser.add_argument("-l", "--loaded_modules", type=int, metavar="pid", help="View loaded modules inside a process")
    parser.add_argument("-e", "--executable_pages", type=int, metavar="pid", help="Pages of memory with executable bit set")
    parser.add_argument("-m", "--mem_info", type=int, metavar="pid", help="Read actual bits in memory of a process")

    args = parser.parse_args()
    if args.enum_proc:
        EnumRunningProcesses()
    elif args.threads:
        RunningThreadsInProcess(args.threads)
    elif args.loaded_modules:
        LoadedModulesInProcess(args.loaded_modules)
    elif args.executable_pages:
        ExecutablePagesInProcess(args.executable_pages)
    elif args.mem_info:
        MemoryInfo(args.mem_info)

    
if __name__ == "__main__":
    main()
