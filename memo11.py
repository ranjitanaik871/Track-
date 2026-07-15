# List vs Tuple Decision Memo

# Task Queue uses List because tasks may be added, removed,
# or updated frequently.

task_queue = ["Task A", "Task B", "Task C"]

task_queue.append("Task D")
task_queue.remove("Task B")

print("Task Queue (List):")
print(task_queue)

# GPS Coordinates use Tuple because coordinates
# should remain fixed and not be modified.

gps_coordinate = (18.5204, 73.8567)

print("\nGPS Coordinate (Tuple):")
print(gps_coordinate)

# gps_coordinate[0] = 20.0000
# This would cause an error because tuples are immutable.