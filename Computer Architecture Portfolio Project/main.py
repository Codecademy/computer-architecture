from cpu import CPU

INSTRUCTION_INPUT_FILE = "instruction_input.txt"
DATA_INPUT_FILE = "data_input.txt"


# Generate list of instructions from input file, use lambda function to strip off '\n' character from each line
def fetch_instructions():
    instruction_file = open(INSTRUCTION_INPUT_FILE, 'r')
    instructions = instruction_file.readlines()
    instructions = list(map(lambda s: s.strip(), instructions))
    return instructions


# Generate list of data inputs to initialize the memory bus from.
# Use lambda function to strip off '\n' character from each line
def fetch_data():
    data_file = open(DATA_INPUT_FILE, 'r')
    data = data_file.readlines()
    data = list(map(lambda s: s.strip(), data))
    return data


# Method to write each value from data_input file to CPU's memory bus
def initialize_memory_bus(cpu):
    data_loaded = fetch_data()
    for data in data_loaded:
        data_parsed = data.split(",")
        cpu.write_memory_bus(data_parsed[0], data_parsed[1])


# Method to send instructions line-by-line to CPU object
def send_instructions_to_cpu(cpu):
    instructions_loaded = fetch_instructions()
    for instruction in instructions_loaded:
        cpu.parse_instruction(instruction)


# Start of Python script to run the CPU simulator
my_cpu = CPU()
print("---------------------------------------------------")
print("Welcome to the Python CPU Simulator!")
print("---------------------------------------------------")
print("Initializing Memory Bus from data input file...")
initialize_memory_bus(my_cpu)
print("Memory Bus successfully initialized")
print("---------------------------------------------------")
print("Sending instructions to CPU...")
send_instructions_to_cpu(my_cpu)
print("---------------------------------------------------")
print("Terminating CPU Processing...")
