import queue

# 1. สร้างคลาสลูกค้า (Customer) ที่จะเก็บข้อมูลของลูกค้า
class Customer:
    def __init__(self, name, service_type):
        self.name = name
        self.service_type = service_type
        # เวลาที่ใช้บริการตามประเภทบริการ
        if service_type == "ตัดผม":
            self.time_needed = 30  # นาที
        elif service_type == "สระ":
            self.time_needed = 20  # นาที
        elif service_type == "ย้อมสี":
            self.time_needed = 60  # นาที

    def __str__(self):
        return f"{self.name} - {self.service_type}"

# 2. สร้างคลาสสำหรับระบบคิวร้านตัดผม
class HairSalonQueue:
    def __init__(self):
        self.queue = queue.Queue()  # สร้างคิวที่ใช้สำหรับจัดการลูกค้า
    
    # 3. เพิ่มลูกค้าเข้าคิว
    def add_customer(self, customer):
        self.queue.put(customer)
        print(f"เพิ่ม {customer} ลงในคิวเรียบร้อยแล้ว")
    
    # 4. เรียกลูกค้าคนถัดไปเข้ารับบริการ
    def serve_customer(self):
        if not self.queue.empty():
            customer = self.queue.get()
            print(f"กำลังให้บริการลูกค้า: {customer}")
        else:
            print("ไม่มีลูกค้าในคิว")
    
    # 5. แสดงรายชื่อลูกค้าที่รอในคิว
    def show_waiting_list(self):
        if self.queue.empty():
            print("ไม่มีลูกค้าในคิว")
        else:
            print("รายชื่อลูกค้าที่รอในคิว:")
            for customer in list(self.queue.queue):  # แสดงรายชื่อในคิวทั้งหมด
                print(customer)
    
    # 6. คำนวณเวลารอโดยประมาณ
    def estimated_wait_time(self):
        waiting_time = 0
        for customer in list(self.queue.queue):  # คำนวณเวลาทั้งหมดในคิว
            waiting_time += customer.time_needed
        print(f"เวลารอโดยประมาณ: {waiting_time} นาที")

# ฟังก์ชันเพื่อให้ผู้ใช้สามารถกรอกข้อมูลลูกค้าเอง
def add_customer_from_input(salon_queue):
    name = input("กรุณากรอกชื่อของลูกค้า: ")
    service_type = input("กรุณากรอกประเภทบริการ (ตัดผม, สระ, ย้อมสี): ")
    
    # ตรวจสอบว่าประเภทบริการที่กรอกมีอยู่ในรายการ
    if service_type not in ["ตัดผม", "สระ", "ย้อมสี"]:
        print("บริการที่เลือกไม่ถูกต้อง กรุณาลองใหม่")
        return

    # สร้างลูกค้าใหม่และเพิ่มเข้าไปในคิว
    customer = Customer(name, service_type)
    salon_queue.add_customer(customer)

# ทดสอบการทำงาน
salon_queue = HairSalonQueue()

# เพิ่มลูกค้าลงในคิวโดยให้ผู้ใช้กรอกข้อมูล
while True:
    add_customer_from_input(salon_queue)
    
    # ถามว่าผู้ใช้ต้องการเพิ่มลูกค้าคนใหม่หรือไม่
    continue_input = input("ต้องการเพิ่มลูกค้าคนใหม่ไหม? (y/n): ").lower()
    if continue_input != 'y':
        break

# แสดงรายชื่อลูกค้าที่รอ
salon_queue.show_waiting_list()

# แสดงเวลารอโดยประมาณ
salon_queue.estimated_wait_time()

# เรียกลูกค้าคนถัดไปเข้ารับบริการ
salon_queue.serve_customer()

# แสดงรายชื่อลูกค้าที่รออีกครั้ง
salon_queue.show_waiting_list()

# แสดงเวลารอโดยประมาณอีกครั้ง
salon_queue.estimated_wait_time()
