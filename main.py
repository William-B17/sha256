
import math

def toBinary(a):
    out = "0"+str(bin(ord(a)))[2:]
    if(len(out) == 8):
        return out
    else:
        return "00"+str(bin(ord(a)))[2:]

def main(maininput):
    def step9(input9a,input9b):
        input9a = []
        
    def step8(input8a,input8b):
        a_i = []
        for x in input8a:
            a_i += '' + x
        step9(a_i,input8b)

    def step7(input7):
        a_h = []
        for i in input7:
            if(i != "00000000"):
                a_h.append(i)
        a_h.pop(-1)
        step8(a_h,input7)

    def step6(input6a,input6b,input6c):
        a_f = input6c
        a_g = int(input6a/8)
        for i in range(0,a_g):
            a_f.append("00000000")
        step7(a_f)

    def step5(input5a,input5b):
        for i in range(1,512):
            if(i + input5a == 448):
                step6(i,input5a,input5b)

    def step4(input4a,input4b):
        a_d = 0
        for i in input4a:
            a_d = a_d + 1
        step5(a_d,input4b)

    def step3(input3a,input3b):
        a_c = []
        for i in input3a:
            for x in (str(i)):
                a_c.append(x)
        step4(a_c,input3b)
        
    def step2(input2):
        a_b = input2
        a_b.append("10000000")
        step3(a_b,a_b)        

    def step1(input1):
        a_a_out = []
        
        for i in [*input1]:
            a_a_out.append(toBinary(i))
        step2(a_a_out)
    step1(maininput)

main("hello world")
