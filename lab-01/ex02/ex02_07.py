print("Nhap cac dong van ban (nhap 'done' de ket thuc):")
lines=[]
while True:
    line=input()
    if line=="done":
        break
    lines.append(line)
print("\nCac dong da nhap sau khi chuyen thanh chu hoa:")
for line in lines:
    print(line.upper())