import sys
def load_agents(filename: str) -> set:
    agents = set()
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                s = line.strip()
                if s:
                    agents.add(s)
    except FileNotFoundError:
        pass
    return agents
def extract_user_agent(line: str) -> str:
    end = line.rfind('"')
    if end == -1:
        return ''
    start = line.rfind('"', 0, end)
    if start == -1:
        return ''
    return line[start+1:end].strip()
def main():
    desktop_agents = load_agents('d.txt')
    mobile_agents = load_agents('m.txt')
    out_lines = []
    write = sys.stdout.write

    for raw_line in sys.stdin:
        line = raw_line.rstrip('\n')
        if not line:
            continue
        ua = extract_user_agent(line)
        if ua in desktop_agents:
            label = 'desktop'
        elif ua in mobile_agents:
            label = 'mobile'
        else:
            label = 'unknown'
        write(f"{label} {line}\n")
if __name__ == '__main__':
    main()
