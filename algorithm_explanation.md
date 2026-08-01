# Algorithm Explanation

## Selected Algorithm

Task Priority Sorting Algorithm

## Introduction

The Task Priority Sorting Algorithm helps organize tasks by calculating a score for each task. The score is based on several factors such as priority level, due date, completion status, tags, and recent updates. After calculating the score, the algorithm sorts the tasks so the most important tasks appear first.

## How the Algorithm Works

### 1. Base Priority

The algorithm first assigns a score based on the task's priority.

- Low Priority = 10 points
- Medium Priority = 20 points
- High Priority = 40 points
- Urgent Priority = 60 points

### 2. Due Date

Extra points are added depending on how close the due date is.

- Overdue tasks receive the highest bonus.
- Tasks due today receive a bonus.
- Tasks due within the next week also receive additional points.

### 3. Task Status

Completed tasks receive fewer points because they no longer need attention.

Tasks that are still under review also receive a small deduction.

### 4. Important Tags

Tasks marked with tags such as **blocker**, **critical**, or **urgent** receive bonus points.

### 5. Recent Updates

Recently updated tasks receive a small bonus because they are likely still active.

### 6. Final Score

All points are added together to create one final score.

### 7. Sorting

The algorithm sorts all tasks from the highest score to the lowest score.

The highest-scoring task becomes the highest priority.

## Example

Imagine three tasks:

- Task A: High priority, due tomorrow
- Task B: Low priority, due next month
- Task C: Urgent priority, overdue

After calculating the scores:

1. Task C
2. Task A
3. Task B

## Advantages

- Helps organize work efficiently.
- Prioritizes urgent tasks.
- Reduces missed deadlines.
- Improves productivity.
- Makes task management easier.

## Conclusion

The Task Priority Sorting Algorithm is useful because it combines several factors to determine which tasks should be completed first instead of relying on priority alone.
