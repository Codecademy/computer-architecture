MEMORY_BUS_SIZE = 128


# This class implements the 'memory bus' as defined in the portfolio project outline document
class Memory:
    def __init__(self):
        # The actual memory bus is implemented as a python dictionary; Key = Address, Value = Value
        self.memory_bus = {}
        self.init_memory_bus()

    # Method used to initialize memory bus, loops from 0 to Size of bus and converts iterator to binary string
    def init_memory_bus(self):
        for i in range(MEMORY_BUS_SIZE):
            self.memory_bus['{0:08b}'.format(i)] = 0

    def search_memory_bus(self, address):
        if self.memory_bus.get(address) is not None:
            return self.memory_bus.get(address)
        return None

    def write_memory_bus(self, address, value):
        if self.memory_bus.get(address) is not None:
            self.memory_bus[address] = value
