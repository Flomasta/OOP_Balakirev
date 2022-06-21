class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu, mem_slots, total_mem_slots=4):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = total_mem_slots
        self.mem_slots = [mem_slots[i] for i in range(total_mem_slots)]

    def get_config(self):
        return [f'Материнская плата: {self.name}',
                f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
                f'Слотов памяти: {self.total_mem_slots}',
                'Память: ' + f'{";".join([i.name + "-" + i.volume for i in self.mem_slots])}']


cpu = CPU('intel', '133')
mem = [Memory('kingston', '16'), Memory('scandisk', '8')]

mb = MotherBoard('intel motherboard', cpu, mem, total_mem_slots=2)
print(mb.get_config(), sep='\n')
