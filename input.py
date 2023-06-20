with open('input.txt', 'r') as file:
    lines = file.readlines()

# Open the output file in write mode
with open('categorysubsub.txt', 'w') as file:
    for line in lines:
        if line.strip():
            file.write(line.lstrip())
            print(line.lstrip())
