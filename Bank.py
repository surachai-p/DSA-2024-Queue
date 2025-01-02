class BankQueue:
    def __init__(self):
        self.queue = []  # เก็บคิวในรูปแบบของลิสต์ (ชื่อ, ประเภทธุรกรรม)

    def add_customer(self, name, transaction_type):
        self.queue.append((name, transaction_type))  # เพิ่มลูกค้าและประเภทธุรกรรม
        print(f"{name} เข้าคิวสำหรับ {transaction_type}")

    def serve_customer(self):
        if self.queue:
            name, transaction_type = self.queue.pop(0)  # เสิร์ฟลูกค้าคนแรกในคิว
            print(f"กำลังให้บริการ {name} สำหรับ {transaction_type}")
        else:
            print("ไม่มีลูกค้าในคิว")

    def show_queue(self):
        if self.queue:
            print("ลูกค้าที่รอในคิว:")
            for i, (name, transaction_type) in enumerate(self.queue, start=1):
                print(f"{i}. {name} ({transaction_type})")
        else:
            print("ไม่มีลูกค้าในคิว")

    def queue_length(self):
        print(f"จำนวนลูกค้าในคิว: {len(self.queue)}")
        return len(self.queue)

    def estimated_wait_time(self):
        wait_time = len(self.queue) * 5  # 5 นาทีต่อธุรกรรม
        print(f"ประมาณการเวลารอ: {wait_time} นาที")
        return wait_time


# การใช้งานระบบคิวธนาคาร
bank_queue = BankQueue()

# เพิ่มลูกค้าเข้าคิว
bank_queue.add_customer("สมชาย", "ฝากเงิน")
bank_queue.add_customer("สมหญิง", "ถอนเงิน")
bank_queue.add_customer("จันทร์เจ้า", "ชำระบิล")

# แสดงจำนวนคิวที่รอ
bank_queue.queue_length()

# แสดงประมาณการเวลารอ
bank_queue.estimated_wait_time()

# แสดงคิวปัจจุบัน
bank_queue.show_queue()

# เรียกลูกค้าเข้ารับบริการ
bank_queue.serve_customer()

# แสดงคิวและเวลารออีกครั้ง
bank_queue.show_queue()
bank_queue.estimated_wait_time()
