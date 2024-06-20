import json
from enum import Enum


class ALUOpcode(str, Enum):
    INC_A = "inc_a"
    INC_B = "inc_b"
    DEC_A = "dec_a"
    DEC_B = "dec_b"
    ADD = "add"
    SUB = "sub"
    MUL = "mul"
    DIV = "div"
    CMP = "cmp"
    TEST = "test"
    SKIP_A = "skip_a"
    SKIP_B = "skip_b"

    def __str__(self) -> str:
        return str(self.value)


class Opcode(str, Enum):
    NOP = "nop"

    INC = "inc"
    DEC = "dec"
    HALT = "halt"
    PUSH = "push"
    POP = "pop"

    LOAD = "load"
    STORE = "store"
    ADD = "add"
    SUB = "sub"
    MUL = "mul"
    DIV = "div"
    OUT = "out"
    IN = "in"
    CMP = "cmp"
    TEST = "test"

    JG = "jg"
    JZ = "jz"
    JNZ = "jnz"
    JMP = "jmp"

    def __str__(self) -> str:
        return str(self.value)


class Selectors(str, Enum):
    FROM_INPUT = "from_input"
    FROM_ALU = "from_alu"
    FROM_DR = "from_dr"
    FROM_PC = "from_pc"
    FROM_SP = "from_sp"
    FROM_AC = "from_ac"
    FROM_PS = "from_ps"

    def __str__(self) -> str:
        return str(self.value)


nullar_instructions = [Opcode.INC, Opcode.DEC, Opcode.HALT, Opcode.PUSH, Opcode.POP]

branch_instructions = [Opcode.JG, Opcode.JZ, Opcode.JNZ, Opcode.JMP]

onear_instructions = [Opcode.LOAD, Opcode.STORE, Opcode.ADD, Opcode.SUB, Opcode.MUL, Opcode.DIV, Opcode.OUT, Opcode.IN, Opcode.CMP, Opcode.TEST]


def write_code(filename, code):
    with open(filename, "w", encoding="utf-8") as file:
        buf = []
        for instr in code:
            buf.append(json.dumps(instr))
        file.write("[" + ",\n ".join(buf) + "]")


def read_code(filename):
    with open(filename, encoding="utf-8") as file:
        return json.loads(file.read())  #  code
