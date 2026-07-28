
def FilterX(Task,Elements):
    Result=[]
    for no in Elements:
        Ret=Task(no)  #checkEven (no) call

        if Ret==True:
            Result.append(no)

    return Result     



def mapx(Task ,Elements):
    Result=[]

    for no in Elements:
        Ret=Task(no)    #increment (no)
        Result.append(Ret)

    return Result


def reducex(task,Elements):
    Sum=0
    for no in Elements:
        Sum=task(Sum,no)
    return Sum   