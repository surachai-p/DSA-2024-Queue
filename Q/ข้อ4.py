from collections import deque

class BankQueue:
    def __init__(self):
        self.queue = deque()

    def add_customer(self, name, transaction_type):
        """เพิ่มลูกค้าเข้าคิว พร้อมประเภทธุรกรรม"""
        self.queue.append((name, transaction_type))
        print(f"เพิ่มลูกค้า: {name}, ธุรกรรม: {transaction_type} เข้าคิวเรียบร้อย")

    def serve_customer(self):
        """เรียกลูกค้าเข้ารับบริการ"""
        if not self.queue:
            print("ไม่มีลูกค้าในคิว")
        else:
            name, transaction_type = self.queue.popleft()
            print(f"กำลังให้บริการลูกค้า: {name}, ธุรกรรม: {transaction_type}")

    def queue_length(self):
        """แสดงจำนวนคิวที่รอ"""
        length = len(self.queue)
        print(f"จำนวนลูกค้าในคิว: {length}")
        return length

    def estimated_wait_time(self):
        """แสดงประมาณการเวลารอ (5 นาที/คน)"""
        wait_time = len(self.queue) * 5
        print(f"เวลารอประมาณ: {wait_time} นาที")
        return wait_time

# ตัวอย่างการใช้งาน
bank_queue = BankQueue()

# เพิ่มลูกค้าเข้าคิว
bank_queue.add_customer("คุณศิริวรรณ", "ฝาก")
bank_queue.add_customer("คุณอัครภูมิ", "ถอน")
bank_queue.add_customer("คุณสุนิสา", "ชำระบิล")

# แสดงจำนวนคิวและเวลารอ
bank_queue.queue_length()
bank_queue.estimated_wait_time()

# ให้บริการลูกค้า
bank_queue.serve_customer()
bank_queue.serve_customer()

# แสดงจำนวนคิวและเวลารออีกครั้ง
bank_queue.queue_length()
bank_queue.estimated_wait_time()
