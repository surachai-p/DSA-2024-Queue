from collections import deque

# สร้างคิวร้านตัดผม
haircut_queue = deque()

# ฟังก์ชันเพิ่มลูกค้าลงคิว
def add_customer():
    name = input("กรุณากรอกชื่อของลูกค้า: ")
    service_type = input("กรุณากรอกบริการที่ต้องการ (ตัดผม, สระ, ย้อมสี): ")
    
    if service_type == "ตัดผม":
        wait_time = 30
    elif service_type == "สระ":
        wait_time = 20
    elif service_type == "ย้อมสี":
        wait_time = 60
    else:
        print("บริการไม่ถูกต้อง กรุณากรอกใหม่")
        return
    
    haircut_queue.append((name, service_type, wait_time))
    print(f"{name} ถูกเพิ่มลงคิวสำหรับบริการ {service_type}")

# ฟังก์ชันแสดงรายชื่อลูกค้าที่รออยู่ในคิว
def show_queue():
    if haircut_queue:
        print("=== รายชื่อลูกค้าที่รอ ===")
        for idx, (name, service_type, wait_time) in enumerate(haircut_queue, start=1):
            print(f"{idx}. {name} - {service_type} (รอประมาณ {wait_time} นาที)")
    else:
        print("ไม่มีลูกค้าในคิว")

# ฟังก์ชันเรียกลูกค้าคนถัดไป
def serve_customer():
    if haircut_queue:
        customer = haircut_queue.popleft()
        name, service_type, _ = customer
        print(f"กำลังให้บริการ {name} สำหรับบริการ {service_type}")
    else:
        print("ไม่มีลูกค้าในคิว")

# ฟังก์ชันประมาณการเวลารอ
def estimated_wait_time():
    if haircut_queue:
        total_wait_time = 0
        for _, _, wait_time in haircut_queue:
            total_wait_time += wait_time
        print(f"เวลารอรวม: {total_wait_time} นาที")
    else:
        print("ไม่มีลูกค้าในคิว")

# ตัวอย่างการใช้งาน
while True:
    print("\n=== ร้านตัดผมคุณหรีด ===")
    print("1. เพิ่มลูกค้า")
    print("2. แสดงรายชื่อลูกค้าที่รอ")
    print("3. เรียกลูกค้าคนถัดไป")
    print("4. แสดงเวลารอโดยประมาณ")
    print("5. ออกจากโปรแกรม")

    choice = input("กรุณาเลือกคำสั่ง: ")

    if choice == "1":
        add_customer()
    elif choice == "2":
        show_queue()
    elif choice == "3":
        serve_customer()
    elif choice == "4":
        estimated_wait_time()
    elif choice == "5":
        print("ขอบคุณที่ใช้บริการร้านตัดผมคุณอังคาร!")
        break
    else:
        print("ตัวเลือกไม่ถูกต้อง กรุณาเลือกใหม่")