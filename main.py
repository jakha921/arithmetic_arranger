numbers = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]


def arithmetic_arranger(numbers, answer=False):
    errors = 0
    first_digit = ''
    second_digit = ''
    operator = ''
    
    if errors > 5:
        return "Error: Too many problems."
    
    for i in numbers:
        short = i.split(" ")
        first_digit = short[0]
        operator = short[1]
        second_digit = short[2]
        
        if (not first_digit.isnumeric()) or (not second_digit.isnumeric()):
            errors += 1;
            return "Error: Numbers must only contain digits."
        
        if (len(first_digit) > 4 ) or (len(second_digit) > 4):
            errors += 1
            return "Error: Numbers cannot be more than four digits."
        
        if (operator == '+') or (operator == '-'):
            
            if operator == '+':
                ans = f'{int(first_digit) + int(second_digit)}'
            else:
                ans = f'{int(first_digit) - int(second_digit)}'  
    
            if (len(first_digit)>len(second_digit)):
                lines_length = len(first_digit) + 2
            else:
                lines_length = len(second_digit) + 2

            top_line = str(first_digit).rjust(lines_length)
            bottom_line = operator + str(second_digit).rjust(lines_length - 1)
            result = str(ans).rjust(lines_length)

            small_lines = ""

            for j in range(lines_length):
                small_lines += "-"


            fin_firsts = top_line + "    "
            fin_seconds = bottom_line + "    "
            fin_lines = small_lines + "    "
            fin_sums = result + "    "

        else:
            return "Error: Operator must be '+' or '-'."

        fin_firsts = fin_firsts.rstrip()
        fin_seconds = fin_seconds.rstrip()
        fin_lines = fin_lines.rstrip()
        fin_sums = fin_sums.rstrip()

        if answer:
            arranged_problems = fin_firsts + "\n" + fin_seconds + "\n" + fin_lines + "\n" + fin_sums
        else:
            arranged_problems = fin_firsts + "\n" + fin_seconds + "\n" + fin_lines

        return arranged_problems

if __name__ == "__main__":
    print(arithmetic_arranger(numbers, True))
