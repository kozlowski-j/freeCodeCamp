def arithmetic_arranger(problems, par=False):
    """ docstring """

    # Validate input
    n_problems = len(problems)
    if n_problems > 5:
        return 'Error: Too many problems.'

    problems_str = ' '.join(problems)
    if problems_str.find('*') > 0 or problems_str.find('/') > 0:
        return "Error: Operator must be '+' or '-'."

    operands = problems_str.replace('+', '').replace('-', '').split()
    if len(operands) != len([o for o in operands if o.isnumeric()]):
        return 'Error: Numbers must only contain digits.'

    if len([o for o in operands if len(o) > 4]):
        return 'Error: Numbers cannot be more than four digits.'

    # Prepare formatted problems
    problems_to_print = []
    for p in problems:
        words = p.split()
        operator = [c for c in words if not c.isalnum()][0]
        op1 = words[0]
        op2 = words[2]
        line_length = len(max(words, key=len)) + 2
        line1_spaces = line_length - len(op2) - 1
        line0 = op1.rjust(line_length)
        line1 = operator + ' ' * line1_spaces + op2
        dashed_line = '-' * line_length
        if par:
            result = str(eval(p)).rjust(line_length)
            formatted_problem = '\n'.join([line0, line1, dashed_line, result])
        else:
            formatted_problem = '\n'.join([line0, line1, dashed_line])
        problems_to_print.append(formatted_problem)

    # Horizontal join
    if n_problems == 2:
        splt_lines = zip(
            problems_to_print[0].split('\n'),
            problems_to_print[1].split('\n')
        )
        res = '\n'.join(['    '.join([x, y]) for x, y in splt_lines])
    elif n_problems == 3:
        splt_lines = zip(
            problems_to_print[0].split('\n'),
            problems_to_print[1].split('\n'),
            problems_to_print[2].split('\n')
        )
        res = '\n'.join(['    '.join([x, y, z]) for x, y, z in splt_lines])
    elif n_problems == 4:
        splt_lines = zip(
            problems_to_print[0].split('\n'),
            problems_to_print[1].split('\n'),
            problems_to_print[2].split('\n'),
            problems_to_print[3].split('\n')
        )
        res = '\n'.join(['    '.join([x, y, z, v]) for x, y, z, v in splt_lines])
    elif n_problems == 5:
        splt_lines = zip(
            problems_to_print[0].split('\n'),
            problems_to_print[1].split('\n'),
            problems_to_print[2].split('\n'),
            problems_to_print[3].split('\n'),
            problems_to_print[4].split('\n')
        )
        res = '\n'.join(['    '.join([x, y, z, v, w]) for x, y, z, v, w in splt_lines])
    else:
        res = 'dd'

    return res


arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], 1)
