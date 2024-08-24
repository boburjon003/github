
Menyu = {
    'Osh':"10000",
    'Qozonkabob':"50000",
    'Siltama':"25000",
    'Manti':"5000",
    
    'Mastava':"9000",
    'shashlik':"7000",
    'gril':"45000",
    'dimlama':"30000",
    'shorva':"15000",
    'Somsa':"6000"
     }
ovqat1=input("birinchi ovqatni kiriting :")
ovqat2=input("ikkinchi ovqatni kiriting :")
ovqat3=input("uchunchi ovqatni kiriting :")
buyurmalar = Menyu.get(ovqat1)
buyurmalar = Menyu.get(ovqat2)
buyurmalar = Menyu.get(ovqat3)

for buyurtma in buyurmalar:
    if buyurtma in Menyu:
        print(Menyu[buyurtma])
    else:
        print("bizda bunday ovqat yo")
        
