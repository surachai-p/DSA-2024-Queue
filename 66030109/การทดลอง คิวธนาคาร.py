import queue

# 1. สร้างคลาสลูกค้า (Customer) ที่จะเก็บข้อมูลของลูกค้า
class Customer:
    def __init__(self, name, transaction_type):
        self.name = name
        self.transaction_type = transaction_type
    
    def __str__(self):
        return f"{self.name} - {self.transaction_type}"

# 2. สร้างคลาสสำหรับระบบคิวธนาคาร
class BankQueue:
    def __init__(self):
        self.queue = queue.Queue()  # สร้างคิวที่ใช้สำหรับจัดการลูกค้า
    
    # 3. เพิ่มลูกค้าเข้าคิว
    def add_customer(self, customer):
        self.queue.put(customer)
        print(f"เพิ่ม {customer} ลงในคิวเรียบร้อยแล้ว")
    
    # 4. เรียกลูกค้าเข้ารับบริการ
    def serve_customer(self):
        if not self.queue.empty():
            customer = self.queue.get()
            print(f"กำลังให้บริการลูกค้า: {customer}")
        else:
            print("ไม่มีลูกค้าในคิว")
    
    # 5. แสดงจำนวนลูกค้าที่รอในคิว
    def show_waiting_count(self):
        print(f"จำนวนลูกค้าที่รอในคิว: {self.queue.qsize()}")
    
    # 6. คำนวณเวลาที่ลูกค้ารอ (สมมติว่าใช้เวลา 5 นาที/คน)
    def estimated_wait_time(self):
        waiting_count = self.queue.qsize()
        estimated_time = waiting_count * 5  # 5 นาทีต่อคน
        print(f"เวลาประมาณการในการรอ: {estimated_time} นาที")
        
# ทดสอบการทำงาน
bank_queue = BankQueue()

# เพิ่มลูกค้าลงในคิว
bank_queue.add_customer(Customer("Alice", "ฝากเงิน"))
bank_queue.add_customer(Customer("Bob", "ถอนเงิน"))
bank_queue.add_customer(Customer("Charlie", "ชำระบิล"))

# แสดงจำนวนลูกค้าที่รอ
bank_queue.show_waiting_count()

# แสดงเวลาที่รอลูกค้า
bank_queue.estimated_wait_time()

# เรียกลูกค้าเข้ารับบริการ
bank_queue.serve_customer()

# แสดงจำนวนลูกค้าที่รออีกครั้ง
bank_queue.show_waiting_count()

# แสดงเวลาที่รอลูกค้าอีกครั้ง
bank_queue.estimated_wait_time()
