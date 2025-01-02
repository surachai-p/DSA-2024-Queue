from collections import deque

# สร้างคิวธนาคาร
bank_queue = deque()

# ฟังก์ชันเพิ่มลูกค้าลงคิว
def add_customer():
    name = input("กรุณากรอกชื่อของลูกค้า: ")
    transaction_type = input("กรุณากรอกประเภทธุรกรรม (ฝากเงิน/ถอนเงิน/ชำระบิล): ")
    bank_queue.append((name, transaction_type))
    print(f"{name} ถูกเพิ่มลงคิวสำหรับธุรกรรม {transaction_type}")

# ฟังก์ชันเรียกลูกค้าเข้ารับบริการ
def serve_customer():
    if bank_queue:
        customer = bank_queue.popleft()
        print(f"กำลังให้บริการ {customer[0]} สำหรับธุรกรรม {customer[1]}")
    else:
        print("ไม่มีลูกค้าในคิว")

# ฟังก์ชันแสดงจำนวนคิวที่รอ
def show_queue():
    print(f"ขณะนี้มีลูกค้ารอในคิว {len(bank_queue)} คน")

# ฟังก์ชันประมาณการเวลารอ
def estimated_wait_time():
    wait_time = len(bank_queue) * 5  # 5 นาทีต่อคน
    print(f"ประมาณการเวลารอ: {wait_time} นาที")

# ตัวอย่างการใช้งาน
while True:
    print("\n----- ระบบคิวธนาคาร -----")
    print("1. เพิ่มลูกค้าลงคิว")
    print("2. เรียกลูกค้าเข้ารับบริการ")
    print("3. แสดงจำนวนคิวที่รอ")
    print("4. แสดงประมาณการเวลารอ")
    print("5. ออกจากโปรแกรม")

    choice = input("กรุณาเลือกตัวเลือก: ")

    if choice == "1":
        add_customer()
    elif choice == "2":
        serve_customer()
    elif choice == "3":
        show_queue()
    elif choice == "4":
        estimated_wait_time()
    elif choice == "5":
        print("ขอบคุณที่ใช้บริการ!")
        break
    else:
        print("ตัวเลือกไม่ถูกต้อง กรุณาเลือกใหม่")

