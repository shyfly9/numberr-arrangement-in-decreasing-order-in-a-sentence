def roman(num):
    number=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
    rom=["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
    i=12
    while num:
        divisor = num//number[i]
        num=num%number[i]
        while divisor:
            print(rom[i],end="")
            divisor-=1 
        i-=1    



num=int(input())
roman(num)