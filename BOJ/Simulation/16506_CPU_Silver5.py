# 16506_CPU_Silver5
# https://www.acmicpc.net/problem/16506

N = int(input())
assembly_codes = [input().split() for _ in range(N)]


def solution0():
    def to_machine_lang(assembly_code):
        answer = ""

        # opcode = assembly_code[0]
        # if opcode.startswith("ADD"):  # 0~3 bit
        #     answer += '0000'
        # elif opcode.startswith("SUB"):
        #     answer += '0001'
        # elif opcode.startswith("MOV"):
        #     answer += '0010'
        # elif opcode.startswith("AND"):
        #     answer += '0011'
        # elif opcode.startswith("OR"):
        #     answer += '0100'
        # elif opcode.startswith("NOT"):
        #     answer += '0101'
        # elif opcode.startswith("MULT"):
        #     answer += '0110'
        # elif opcode.startswith("LSFTL"):
        #     answer += '0111'
        # elif opcode.startswith("LSFTR"):
        #     answer += '1000'
        # elif opcode.startswith("ASFTR"):
        #     answer += '1001'
        # elif opcode.startswith("RL"):
        #     answer += '1010'
        # else:  # RR
        #     answer += '1011'
        # if opcode.endswith('C'):  # 4 bit
        #     answer += '1'
        # else:
        #     answer += '0'

        opcode_dict = {"ADD": 0, "ADDC": 1, "SUB": 2, "SUBC": 3, "MOV": 4, "MOVC": 5,
                       "AND": 6, "ANDC": 7, "OR": 8, "ORC": 9, "NOT": 10, "MULT": 12,
                       "MULTC": 13, "LSFTL": 14, "LSFTLC": 15, "LSFTR": 16, "LSFTRC": 17,
                       "ASFTR": 18, "ASFTRC": 19, "RL": 20, "RLC": 21, "RR": 22, "RRC": 23}
        answer += bin(opcode_dict[assembly_code[0]])[2:].zfill(5)

        answer += '0'  # 5 bit
        answer += bin(int(assembly_code[1]))[2:].zfill(3)  # 6~8 bit
        answer += bin(int(assembly_code[2]))[2:].zfill(3)  # 9~11 bit

        if answer[4] == '0':  # 12~15 bit
            answer += bin(int(assembly_code[3]))[2:].zfill(3) + '0'
        else:
            answer += bin(int(assembly_code[3]))[2:].zfill(4)

        return answer

    for a in assembly_codes:
        print(to_machine_lang(a))


"""
문제가 긴 구현문제
opcode rD rA rB 또는 opcode rD rA #C
r 은 레지스터 #C 는 상수
rA 와 rB(#C) 를 opcode 로 연산 후 rD 에 저장

0~3 : opcode
4 : 0 이면 rB, 1 이면 #C
5 : 0
6~8 : rD (3자리)
9~11 : rA or 000 (3자리)
12~15 : 4 가 0이면 rB (3자리) + 0, 4가 1이면 #C (4자리)

opcode 쪽을 숫자의 dict 으로 처리하는 것도 가능
"""

solution0()
