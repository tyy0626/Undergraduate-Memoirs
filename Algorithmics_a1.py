import sys


# Boost recursion limit to handle deep recursive calls.
# The default limit might be too low for some graph problems.
def boost_recursion(limit=10_000_000):
    sys.setrecursionlimit(limit)
boost_recursion()
def compute_max_snake(n, link):
    answer = 0
    def explore(last, visited, length):
        nonlocal answer  # Allow modification of the 'answer' variable in the outer scope.

        # Update the global maximum if the current snake is longer.
        if length > answer:
            answer = length

        remain = (~visited) & ((1 << n) - 1)  # Calculate unvisited nodes.
        if length + bin(remain).count('1') <= answer:
            return

        # Iterate through all possible next nodes.
        for nxt in range(n):
            # Check if 'nxt' is not visited AND 'nxt' is linked to 'last'.
            if (visited >> nxt) & 1 == 0 and (link[last] >> nxt) & 1:
                if link[nxt] & (visited ^ (1 << last)):
                    continue  # If connected to other visited nodes, skip this 'nxt'.

                # Recursively explore the path with 'nxt' added.
                explore(nxt, visited | (1 << nxt), length + 1)

    # Start exploring from each possible node as the first node of the snake.
    for start_node in range(n):
        # Initial call: start with 'start_node' as the first node,
        explore(start_node, 1 << start_node, 0)
    return answer  # Return the overall maximum snake length.


def main():
    # Read all lines from standard input.
    lines = sys.stdin.read().splitlines()
    ptr = 0  # Pointer to keep track of the current line being processed.
    total_lines = len(lines)

    # Process input line by line.
    while ptr < total_lines:
        line = lines[ptr].strip()  # Get the current line and remove leading/trailing whitespace.
        ptr += 1  # Move to the next line.

        if not line:  # Skip empty lines.
            continue
        try:
            size = int(line)  # Attempt to parse the line as an integer (graph size).
        except ValueError:
            break  # If not a valid integer, stop processing.
        if size == 0:
            break  # If size is 0, terminate.

        adj = [0] * size  # Initialize adjacency list (represented as bitmasks).
        # Read adjacency matrix for the current graph.
        for i in range(size):
            if ptr >= total_lines:  # Ensure we don't go out of bounds.
                break
            row = lines[ptr].strip()  # Get the row representing connections for node 'i'.
            ptr += 1
            if row:  # If the row is not empty.
                # Parse connected nodes and set bits in the adjacency mask.
                for num in map(int, row.split()):
                    adj[i] |= (1 << num)  # Set the bit for 'num' in 'adj[i]'.

        print(compute_max_snake(size, adj))


if __name__ == "__main__":
    main()
