# Task: Use while, for, range(), break, continue, and the loop-else clause.

"""
TODO:
[ ] - use range() to create a loop that iterates a specific number of times
[ ] - use break to exit a loop early based on a condition
[ ] - use continue to skip an iteration of a loop based on a condition
[ ] - use a loop-else clause to execute code after a loop completes without a break
"""

import random
import time
import sys
def main():
    # Set a random target progress (e.g., between 20 and 100)
    target = random.randint(20, 100)
    progress = 0
    bar_width = 30  
    while progress < target:
        # Increment progress by a random small step (0.5 to 2)
        step = random.uniform(0.5, 2.0)
        progress += step
        if progress > target:
            progress = target
        # Calculate percentage
        percent = (progress / target) * 100
        # Calculate filled length of the bar
        filled_len = int(round(bar_width * progress / target))
        bar = '=' * filled_len + '-' * (bar_width - filled_len)
        # Print the progress bar on the same line
        sys.stdout.write(f'\rProgress: [{bar}] {percent:5.1f}%')
        sys.stdout.flush()
        # Sleep a bit to simulate work
        time.sleep(0.1)
    # After loop, ensure 100%
    sys.stdout.write(f'\rProgress: [{"=" * bar_width}] 100.0%\n')
    sys.stdout.flush()
if __name__ == '__main__':
    main()