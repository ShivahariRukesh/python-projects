import subprocess
import time
import os

def get_processes():
    if os.name == 'nt': 
        command = 'tasklist'
        start_line = 3 
    else: 
        command = ['ps', '-eo', 'pid,comm,%mem,%cpu']
        start_line = 1

    result = subprocess.run(command, capture_output=True, text=True, shell=(os.name=='nt'))
    
    lines = result.stdout.strip().split('\n')
    processes = []
    
    for line in lines[start_line:]:

        parts = line.split()
        if len(parts) > 1:
            processes.append(parts)
            
    return processes

def display_dashboard():
    while True:
        procs = get_processes()
        
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(f"{'PID':<10} {'NAME':<25} {'MEM USAGE'}")
        print("-" * 50)
        
        for p in procs[:10]: 
            print(f"{p[1]:<10} {p[0]:<25} {' '.join(p[2:])}")
            
        print("\nPress Ctrl+C to stop")
        time.sleep(1)

if __name__ == "__main__":
    display_dashboard()