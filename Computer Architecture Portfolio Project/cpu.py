from cache import Cache
from memory import Memory

CPU_COUNTER_INIT_VALUE = 0
NUMBER_OF_REGISTERS = 9

ADD_INSTRUCTION_OPERATOR = "ADD"
ADD_I_INSTRUCTION_OPERATOR = "ADDI"
JUMP_INSTRUCTION_OPERATOR = "J"
CACHE_INSTRUCTION_OPERATOR = "CACHE"

CACHE_OFF_VALUE = 0
CACHE_ON_VALUE = 1
CACHE_FLUSH_VALUE = 2


# Helper function to convert register string to index. I.e. register labelled 'R2' should correspond to int index 2
def convert_register_to_index(value):
    return int(value[1:])


# CPU class to implement the bulk of CPU Simulator requirements. Member properties include:
# CPU Counter - Int representing the number of the instruction being parsed
# Registers - List used to represent internal registers used by the CPU
# Cache Flag - boolean representing whether or not the cache is to be used
# Cache - instance of Cache object instantiated for CPU
# Memory Bus - instance of Memory Bus object instantiated for CPU
class CPU:

    def __init__(self):
        self.cpu_counter = CPU_COUNTER_INIT_VALUE
        self.registers = [0] * NUMBER_OF_REGISTERS
        self.cache_flag = False
        self.cache = Cache()
        self.memory_bus = Memory()

    def increment_cpu_counter(self):
        self.cpu_counter += 1

    def reset_cpu_counter(self):
        self.cpu_counter = CPU_COUNTER_INIT_VALUE

    def set_cpu_counter(self, value):
        self.cpu_counter = value

    def get_cpu_counter(self):
        return self.cpu_counter

    def reset_registers(self):
        for i in range(len(self.registers)):
            self.registers[i] = 0

    def set_cache_flag(self, value):
        self.cache_flag = value

    def flush_cache(self):
        self.cache.flush_cache()

    def search_cache(self, address):
        return self.cache.search_cache(address)

    def write_cache(self, address, value):
        self.cache.write_cache(address, value)

    def search_memory_bus(self, address):
        return self.memory_bus.search_memory_bus(address)

    def write_memory_bus(self, address, value):
        self.memory_bus.write_memory_bus(address, value)

    # --- Sample implementations for ADD, ADDI, J, and Cache instructions ---

    def jump_instruction(self, target):
        self.cpu_counter = int(target)

    def add_instruction(self, destination, source, target):
        self.registers[convert_register_to_index(destination)] = self.registers[convert_register_to_index(source)] + \
                                                                 self.registers[convert_register_to_index(target)]

    def add_i_instruction(self, destination, source, immediate):
        self.registers[convert_register_to_index(destination)] = self.registers[convert_register_to_index(source)] + \
                                                                 int(immediate)

    # Method to implement cache instruction. 0 = OFF, 1 = ON, 2 = Flush Cache
    def cache_instruction(self, value):
        if value == CACHE_OFF_VALUE:
            self.set_cache_flag(False)
        if value == CACHE_ON_VALUE:
            self.set_cache_flag(True)
        if value == CACHE_FLUSH_VALUE:
            self.flush_cache()

    # --- Add implementations for further instructions below ---

    # --------------------------------------------------------- #

    # Main parser method used to interpret instructions from input file.
    # Check value of operator and call subsequent helper function
    def parse_instruction(self, instruction):
        instruction_parsed = instruction.split(",")
        print("Reading instruction: " + instruction)
        self.increment_cpu_counter()
        if instruction_parsed[0] == ADD_INSTRUCTION_OPERATOR:
            self.add_instruction(instruction_parsed[1], instruction_parsed[2], instruction_parsed[3])
        if instruction_parsed[0] == ADD_I_INSTRUCTION_OPERATOR:
            self.add_i_instruction(instruction_parsed[1], instruction_parsed[2], instruction_parsed[3])
        if instruction_parsed[0] == JUMP_INSTRUCTION_OPERATOR:
            self.jump_instruction(instruction_parsed[1])
        if instruction_parsed[0] == CACHE_INSTRUCTION_OPERATOR:
            self.cache_instruction(instruction_parsed[1])
