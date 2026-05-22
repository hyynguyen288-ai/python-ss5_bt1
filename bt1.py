branch_count = int(input("Nhập số lượng chi nhánh: "))
month_count = 3
revenues = []
for branch in range(branch_count):
    temp = []
    for month in range(month_count):
        revenue = int(input(
            f"Nhập doanh thu Chi nhánh {branch+1}, tháng {month+1}: "
        ))
        temp.append(revenue)
    revenues.append(temp)
print("-------------- Kết quả --------------")
for branch in range(branch_count):
    for month in range(month_count):
        print(
            "Chi nhánh", branch+1,
            ", tháng", month+1, ":",
            revenues[branch][month],
            "triệu đồng"
        )
 #loi do sap xep sai thu tu vong lap