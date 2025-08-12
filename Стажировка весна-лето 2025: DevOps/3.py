import sys
import math
from collections import defaultdict

def parse_log_line(line):
    """Парсит строку лога и извлекает код ответа и время ответа только для запросов к /pet"""
    parts = line.strip().split()
    if len(parts) < 10:
        return None, None
    

    is_pet_request = False
    for part in parts:
        if part == '/pet':
            is_pet_request = True
            break
    
    if not is_pet_request:
        return None, None
    

    http_code = None
    response_time = None
    
    for i, part in enumerate(parts):
        if part.startswith('HTTP/'):
            if i + 1 < len(parts) and parts[i + 1].isdigit():
                http_code = int(parts[i + 1])
                break
    
  
    for part in reversed(parts):
        if part.endswith('ms'):
            try:
                response_time = int(part[:-2]) 
            except ValueError:
                continue
    
    return http_code, response_time

def calculate_percentile(values, percentile):
    """Вычисляет перцентиль для списка значений"""
    if not values:
        return 0
    
    sorted_values = sorted(values)
    n = len(sorted_values)
    index = (percentile / 100) * (n - 1)
    
    if index == int(index):
        return sorted_values[int(index)]
    else:
        lower = sorted_values[int(index)]
        upper = sorted_values[int(index) + 1]
        return lower + (upper - lower) * (index - int(index))

def main():

    lines = []
    try:

        with open('input.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:

        lines = sys.stdin.readlines()
    

    response_data = defaultdict(list)
    total_requests = 0
    error_requests = 0
    
    for line in lines:
        if line.strip():  
            http_code, response_time = parse_log_line(line)
            
            if http_code is not None and response_time is not None:
                response_data[http_code].append(response_time)
                total_requests += 1
                

                if 500 <= http_code < 600:
                    error_requests += 1
    

    sorted_codes = sorted(response_data.keys())
    

    for code in sorted_codes:
        times = response_data[code]
        count = len(times)
        min_time = min(times)
        max_time = max(times)
        percentile_75 = calculate_percentile(times, 75)
        
        # Округляем в меньшую сторону
        min_time = math.floor(min_time)
        max_time = math.floor(max_time)
        percentile_75 = math.floor(percentile_75)
        
        print(f"{code} {count} {min_time} {max_time} {percentile_75}")
    

    error_percentage = 0
    if total_requests > 0:
        error_percentage = (error_requests / total_requests) * 100
    
    error_percentage = math.floor(error_percentage)
    print(error_percentage)

if __name__ == "__main__":
    main()
