firstLine = list(map(int, input().rstrip().split()))
costOfFood = list(map(int, input().rstrip().split()))
charged = int(input())

deal = 0

def JudgeOfCost(firstLine,costOfFood, charged):
    deal = ((sum(costOfFood) - costOfFood[firstLine[1]])/2)
    if (charged - deal == 0):
        print("Bon Appetit")
    else:
        print(int(charged - deal))

JudgeOfCost(firstLine, costOfFood, charged)