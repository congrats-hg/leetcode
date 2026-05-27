class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for op in operations:
            if op == "+":
                record.append(int(record[-2]) + int(record[-1]))
            elif op == "D":
                record.append(int(record[-1]) * 2)
            elif op == "C":
                record.pop(-1)
            else:
                record.append(int(op))

        return sum(record)