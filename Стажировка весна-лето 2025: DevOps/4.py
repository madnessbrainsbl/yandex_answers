#!/usr/bin/env python3
#решение на 3 из 6 балов
import os, glob, re

def get_last_numa_memory():
    nodes = glob.glob('/sys/devices/system/node/node[0-9]*')
    if nodes:
        max_node = max(int(re.search(r'node(\d+)$', n).group(1)) for n in nodes)
        meminfo_path = f'/sys/devices/system/node/node{max_node}/meminfo'
        if os.path.exists(meminfo_path):
            with open(meminfo_path) as f:
                for line in f:
                    if 'MemTotal:' in line:
                        return int(line.split()[1])
    
    with open('/proc/meminfo') as f:
        for line in f:
            if 'MemTotal:' in line:
                return int(line.split()[1])
    return 0

def get_ht_sibling(cpu_id):
    siblings_path = f'/sys/devices/system/cpu/cpu{cpu_id}/topology/thread_siblings_list'
    if os.path.exists(siblings_path):
        with open(siblings_path) as f:
            siblings_str = f.read().strip()
            siblings = []
            for part in siblings_str.split(','):
                if '-' in part:
                    start, end = map(int, part.split('-'))
                    siblings.extend(range(start, end + 1))
                else:
                    siblings.append(int(part))
            
            siblings = [s for s in siblings if s != cpu_id]
            if siblings:
                return min(siblings)  
    
    return cpu_id  

def main():

    memory_kb = get_last_numa_memory()
    
    cpu_dirs = glob.glob('/sys/devices/system/cpu/cpu[0-9]*')
    if cpu_dirs:
        cpu_ids = [int(re.search(r'cpu(\d+)$', d).group(1)) for d in cpu_dirs]
        last_cpu = max(cpu_ids)
    else:

        last_cpu = 0
        with open('/proc/cpuinfo') as f:
            for line in f:
                if line.startswith('processor'):
                    cpu_num = int(line.split(':')[1])
                    last_cpu = max(last_cpu, cpu_num)
    

    sibling = get_ht_sibling(last_cpu)
    
    print(memory_kb)
    print(sibling)

if __name__ == '__main__':
    main()
