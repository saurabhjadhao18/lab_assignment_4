class Process:
    def __init__(self, p_id, process, start_time, priority):
        self.p_id = p_id
        self.process = process
        self.start_time = start_time
        self.priority = priority

class ProcessTable:
    def __init__(self):
        self.processes = []

    def add_process(self, process):
        self.processes.append(process)

    def merge(self, left, right, key):
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if key(left[i]) < key(right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def merge_sort(self, arr, key):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        left_sorted = self.merge_sort(left_half, key)
        right_sorted = self.merge_sort(right_half, key)

        return self.merge(left_sorted, right_sorted, key)

    def sort_by_p_id(self):
        self.processes = self.merge_sort(self.processes, key=lambda x: x.p_id)

    def sort_by_start_time(self):
        self.processes = self.merge_sort(self.processes, key=lambda x: x.start_time)

    def sort_by_priority(self):
        priority_order = {'Low': 1, 'MID': 2, 'High': 3}
        self.processes = self.merge_sort(self.processes, key=lambda x: priority_order[x.priority])

    def display_table(self):
        print("P_ID\tProcess\tStart Time (ms)\tPriority")
        for process in self.processes:
            print(f"{process.p_id}\t{process.process}\t{process.start_time}\t\t{process.priority}")

if __name__ == "__main__":
    process_table = ProcessTable()

    process_table.add_process(Process("P1", "VSCode", 100, "MID"))
    process_table.add_process(Process("P23", "Eclipse", 234, "MID"))
    process_table.add_process(Process("P93", "Chrome", 189, "High"))
    process_table.add_process(Process("P42", "JDK", 9, "High"))
    process_table.add_process(Process("P9", "CMD", 7, "High"))
    process_table.add_process(Process("P87", "NotePad", 23, "Low"))

    print("Select sorting parameter:")
    print("1. Sort by P_ID")
    print("2. Sort by Start Time")
    print("3. Sort by Priority")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        process_table.sort_by_p_id()
    elif choice == 2:
        process_table.sort_by_start_time()
    elif choice == 3:
        process_table.sort_by_priority()
    else:
        print("Invalid choice.")

    process_table.display_table()
