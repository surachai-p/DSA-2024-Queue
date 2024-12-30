class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """เพิ่มข้อมูลเข้าคิว"""
        self.items.append(item)

    def dequeue(self):
        """นำข้อมูลออกจากคิว"""
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def is_empty(self):
        """ตรวจสอบว่าคิวว่างหรือไม่"""
        return len(self.items) == 0

    def size(self):
        """คืนค่าจำนวนข้อมูลในคิว"""
        return len(self.items)


class BankQueueSystem:
    def __init__(self):
        self.queue = Queue()

    def add_customer(self, name, transaction_type):
        """เพิ่มลูกค้าเข้าคิวพร้อมประเภทธุรกรรม"""
        self.queue.enqueue({"name": name, "transaction_type": transaction_type})
        print(f"เพิ่มลูกค้า {name} ({transaction_type}) เข้าคิว")

    def serve_customer(self):
        """เรียกลูกค้าเข้ารับบริการ"""
        if not self.queue.is_empty():
            customer = self.queue.dequeue()
            print(f"กำลังให้บริการลูกค้า: {customer['name']} ({customer['transaction_type']})")
        else:
            print("ไม่มีลูกค้าในคิว")

    def show_queue(self):
        """แสดงจำนวนคิวที่รอ"""
        print(f"จำนวนลูกค้าในคิว: {self.queue.size()}")
        for i, customer in enumerate(self.queue.items, start=1):
            print(f"ลำดับ {i}: {customer['name']} ({customer['transaction_type']})")

    def estimate_wait_time(self):
        """แสดงประมาณการเวลารอ (5 นาทีต่อคน)"""
        wait_time = self.queue.size() * 5
        print(f"เวลารอประมาณการ: {wait_time} นาที")


# ทดสอบระบบคิวธนาคาร
bank_system = BankQueueSystem()

# เพิ่มลูกค้าเข้าคิว
bank_system.add_customer("สมชาย", "ฝาก")
bank_system.add_customer("สมหญิง", "ถอน")
bank_system.add_customer("จินดา", "ชำระบิล")

# แสดงคิวที่รอ
bank_system.show_queue()

# แสดงเวลารอโดยประมาณ
bank_system.estimate_wait_time()

# ให้บริการลูกค้า
bank_system.serve_customer()
bank_system.serve_customer()

# แสดงสถานะคิวอีกครั้ง
bank_system.show_queue()

# แสดงเวลารอโดยประมาณอีกครั้ง
bank_system.estimate_wait_time()
