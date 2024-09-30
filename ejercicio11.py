i = 0
while i < 4:
    codVendedor =int(input("codigo de vendedor: "))
    importe = float(input("importe: "))
    if i == 0:
        codMax = codVendedor
        codMin = codVendedor
        impMax = importe
        impMin = importe
    if importe == 0:
        i = 4
    else:
        if importe > impMax:
            impMax = importe
            codMax = codVendedor
        if importe < impMin:
            impMin = importe
            codMin = codVendedor
    i = i+1
print(f"venta mas alta: Vendedor {codMax}, ${impMax}")
print(f"venta mas baja: Vendedor {codMin}, ${impMin}")