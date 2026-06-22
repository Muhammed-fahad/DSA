def processLogs(logs, threshold):
    store_out = {}
    n = len(logs)
    for i in range(n):
        store = logs[i].split()
        single_check = set()
        for j in store:
            s = int(j)
            if(s not in single_check and s < 100):
                store_out[s] = store_out.get(s,0)+1
                single_check.add(s)

    out = []
    for l,m in store_out.items():
        if(m >= threshold):
            out.append(l)
    return(out)


if __name__ == "__main__":
    logs_count = int(input("Enter number of logs: "))
    logs = []
    for i in range(logs_count):
        value = input("Enter the numbers with space ex:1 2 50: ")
        logs.append(value)
    threshold = int(input("Enter the threshold value: "))
    print(processLogs(logs,threshold))