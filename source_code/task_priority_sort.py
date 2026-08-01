from datetime import datetime, timedelta

class Task:
    def __init__(self, title, priority, due_date, status, tags, updated_at):
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self.status = status
        self.tags = tags
        self.updated_at = updated_at

def calculate_task_score(task):
    # Base priority weights
    priority_weights = {
        "LOW": 1,
        "MEDIUM": 2,
        "HIGH": 4,
        "URGENT": 6
    }

    score = priority_weights.get(task.priority, 0) * 10

    # Due date score
    if task.due_date:
        days_until_due = (task.due_date - datetime.now()).days

        if days_until_due < 0:
            score += 35
        elif days_until_due == 0:
            score += 20
        elif days_until_due <= 2:
            score += 15
        elif days_until_due <= 7:
            score += 10

    # Status score
    if task.status == "DONE":
        score -= 50
    elif task.status == "REVIEW":
        score -= 15

    # Tag bonus
    if any(tag in ["blocker", "critical", "urgent"] for tag in task.tags):
        score += 8

    # Recently updated bonus
    days_since_update = (datetime.now() - task.updated_at).days

    if days_since_update < 1:
        score += 5

    return score

def sort_tasks_by_importance(tasks):
    task_scores = [(calculate_task_score(task), task) for task in tasks]
    sorted_tasks = [task for _, task in sorted(task_scores, reverse=True)]
    return sorted_tasks

def get_top_priority_tasks(tasks, limit=5):
    sorted_tasks = sort_tasks_by_importance(tasks)
    return sorted_tasks[:limit]

# Example
if __name__ == "__main__":
    tasks = [
        Task(
            "Finish Assignment",
            "HIGH",
            datetime.now() + timedelta(days=1),
            "TODO",
            ["school"],
            datetime.now()
        ),
        Task(
            "Pay Electricity Bill",
            "URGENT",
            datetime.now() - timedelta(days=1),
            "TODO",
            ["critical"],
            datetime.now()
        ),
        Task(
            "Wash Car",
            "LOW",
            datetime.now() + timedelta(days=10),
            "DONE",
            [],
            datetime.now()
        )
    ]

    sorted_tasks = sort_tasks_by_importance(tasks)

    print("Tasks sorted by importance:\n")

    for task in sorted_tasks:
        print(f"{task.title} - Score: {calculate_task_score(task)}")
