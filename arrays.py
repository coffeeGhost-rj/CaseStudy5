import numpy as np

dataArr = [1,2,3],[4,5,6],[7,8,9]

arrObj = np.array(dataArr)
# print(arrObj)

ranObj = np.random.rand(3,3)*10

roundrandObj = np.round(ranObj)
score = 0
print("\n")
print("Number guess Krega???")
print("\n")

notFinished = True
while notFinished:
    # comment: 
    if (input("HAAaaa ya NAAA: ") == "HAAaaa"):
        notFinished = False
    # end if
# end while
# input("HAA ya NAAA ")


for i in roundrandObj:
    # print(i)
    for j in i:
        # print(f"money is {int(j)}")
        # comment: game mode
        print("\n")
        # print(j)
        j+=5
        # print(j)
        guess = input("Chal ab number Daal: ")
        # print(guess)

        if len(guess) == 0:
            print("\n")
            print("counting nahi aati kya? ")
        elif len(guess)>=2:
            print("\n")
            print("1 se 9 ke beech m daal")
        elif int(guess) == int(j):
            print("\n")
            print("Arrey bc sahi Pakkda")
            score +=1
            # break
        else:
            print("\n")
            print("GALAT h tu!!! Kisi kaam ka nahi h.")   
            print("\n")
            print(int(j), "ye tha number, tu bhi kya yaad rkhega!!")
        if len(str(int(j)))>1:
            print("ohh!! 10 se upr bhi number jata h sorry!! our Bad!!\n")
            print(f"ye tha number -> {int(j)} \n Jaa tu bhi kya yaad rkhega!!")
                     
        # end try
print("\n")
print(f"Delulu h tu!!!!\n Arrey waah bohot jyada hi hoshiyaar ho aap \n tera score hua {score} \n ye lo apka NObel PRize!!!")