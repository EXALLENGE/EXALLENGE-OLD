import hello_world

output = []

hello_world.print = lambda s: output.append(s)

hello_world.main()

print(output)
