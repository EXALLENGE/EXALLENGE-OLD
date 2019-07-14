import solution

input_data = ['1', '2']
output_data = []

solution.input = lambda : input_data.pop()
solution.print = lambda s: output_data.append(s)

solution.__main_process_in_solution_which_we_are_going_to_test()

print(output_data)