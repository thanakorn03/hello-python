# โปรแกรมแยกธนบัตร

# กำหนดราคาของแต่ละธนบัตร
denominations = [1000, 500, 100, 50, 20, 10]

# รับจำนวนเงินที่ต้องการแยก
amount = int(input("กรุณาใส่จำนวนเงินที่ต้องการแยก (บาท): "))

# วนลูปหาธนบัตรที่ใช้แยกเงิน
for denomination in denominations:
    # หาจำนวนธนบัตรที่ใช้แยกเงิน
    count = amount // denomination
    # ถ้ามีธนบัตรให้แยก
    if count > 0:
        print(f"ใช้ธนบัตร {denomination} บาท จำนวน {count} ใบ")
    # ลบจำนวนเงินที่ใช้แยกด้วยจำนวนธนบัตร
    amount -= count * denomination