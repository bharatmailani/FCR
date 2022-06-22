at=int(input("attened tickets:-"))
ata=int(input("total assigned ticket:-"))
opr=input("Enter the opr:- ")

if opr=="+":
     print(at+ata)
if opr=="-":
    print(at-ata)
if opr=="*":
    print(at*ata/100,"%")
if opr=="/":
    print(at/ata)
if opr!="+" and opr!="-" and opr!="*" and opr!="/":
    print("invalid operations.")




