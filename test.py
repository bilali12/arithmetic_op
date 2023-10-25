def arithmetic_arranger(problems, display_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = []

    for problem in problems:
        parts = problem.split()

        if parts[1] not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not parts[0].isdigit() or not parts[2].isdigit():
            return "Error: Numbers must only contain digits."
        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        num1 = int(parts[0])
        num2 = int(parts[2])
        operator = parts[1]

        max_width = max(len(parts[0]), len(parts[2]) + 2)  # Add 2 for the operator and space
        arranged_problems.append(f"{num1:>{max_width}}")
        arranged_problems.append(f"{operator} {num2:>{max_width-2}}")
        arranged_problems.append("-" * max_width)

    if display_answers:
        answers = []
        for problem in problems:
            num1, operator, num2 = problem.split()
            num1, num2 = int(num1), int(num2)
            if operator == '+':
                result = num1 + num2
            else:
                result = num1 - num2
            max_width = max(len(str(num1)), len(str(num2)) + 2)
            answers.append(f"{result:>{max_width}}")

        arranged_problems.append("    ".join(answers))

    return "    ".join(arranged_problems)

# Example usage:
problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
print(arithmetic_arranger(problems))
print(arithmetic_arranger(problems, True))
