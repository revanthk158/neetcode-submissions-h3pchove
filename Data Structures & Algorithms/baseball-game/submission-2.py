class Solution:
    def calPoints(self, operations: List[str]) -> int:
        mystack = []

        for op in operations:
            if op.lstrip('-').isdigit():          # integer score
                mystack.append(int(op))

            elif op == "+":
                mystack.append(mystack[-1] + mystack[-2])

            elif op == "D":
                mystack.append(mystack[-1] * 2)

            elif op == "C":
                mystack.pop()

        return sum(mystack)


        