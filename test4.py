class Bank:
    def __init__(self):
        self.waiting_queue = []  # เปลี่ยนเป็น list เพื่อเก็บ tuple (ชื่อ, ประเภทธุรกรรม)
        self.average_transaction_time = 5  # นาที/คน

    def add_customer(self, name, transaction_type):
        self.waiting_queue.append((name, transaction_type))
        print(f"ลูกค้า {name} เข้าคิวที่ {len(self.waiting_queue)} ด้วยธุรกรรม {transaction_type}")

    def serve_customer(self):
        if self.waiting_queue:
            customer, transaction_type = self.waiting_queue.pop(0)
            print(f"กำลังเสิร์ฟลูกค้า: {customer} (ธุรกรรม: {transaction_type})")
        else:
            print("ไม่มีลูกค้าในคิว")

    def show_queue(self):
        print("คิวปัจจุบัน:")
        for i, (name, transaction_type) in enumerate(self.waiting_queue, 1):
            print(f"{i}. {name} ({transaction_type})")
        print(f"จำนวนลูกค้าในคิว: {len(self.waiting_queue)}")

    def estimated_waiting_time(self):
        if self.waiting_queue:
            num_customers = len(self.waiting_queue)
            estimated_time = num_customers * self.average_transaction_time
            print(f"ประมาณการเวลาที่ต้องรอ: {estimated_time} นาที")
        else:
            print("ไม่มีลูกค้าในคิว")

# สร้างธนาคาร
bank = Bank()

# เพิ่มลูกค้าเข้าคิว
bank.add_customer("อานนท์", "ฝาก")
bank.add_customer("บุญมี", "ถอน")
bank.add_customer("จินดา", "ชำระบิล")

# แสดงสถานะคิว
bank.show_queue()

# ประมาณการเวลาที่ต้องรอ
bank.estimated_waiting_time()

# เสิร์ฟลูกค้า 2 คน
bank.serve_customer()
bank.serve_customer()

# แสดงสถานะคิวอีกครั้ง
bank.show_queue()