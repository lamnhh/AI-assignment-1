# HCMUS - Introduction to AI - Assignment 1

Remember to install required packages first

```
pip install -r requirements.txt
```

## Usage

```
python3 main.py --input INPUT_PATH --algorithm ALGORITHM --visualize VISUALIZE
```

Where:

- INPUT_PATH: path to input file.
- ALGORITHM: algorithm to use to find shortest path. There are 5 options: 
    - ucs: Uniform-Cost Search.
    - a_star: A* with Heuristic function being Euclidean distance.
    - greedy: Greedy search, choose vertex with smallest heuristic value to go next.
    - t3_dp: a dynamic programming approach for task 3.
    - t3_greedy: a greedy search approach for task 3 - choose the nearest waiting point to go next.
- VISUALIZE: 2d/3d - visualize result in 2D or 3D (for task 5).