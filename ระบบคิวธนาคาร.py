class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None
    
    def front(self):
        if not self.is_empty():
            return self.items[0]
        return None
    
    def size(self):
        return len(self.items)
    
    def display(self):
        print(f"Queue: {self.items}")
        
    def clear(self):
        self.items = []
        print("คิวถูกล้างเรียบร้อยแล้ว")
    
    def peek_last(self):
        if not self.is_empty():
            return self.items[-1]
        return None


class BankQueue:
    def __init__(self):
        self.queue = Queue()
    
    def add_customer(self, name, transaction_type):
        """เพิ่มลูกค้าเข้าคิวพร้อมกับระบุประเภทธุรกรรม"""
        self.queue.enqueue((name, transaction_type))
        print(f"ลูกค้า {name} เข้าคิว (ธุรกรรม: {transaction_type})")
    
    def serve_customer(self):
        """เรียกลูกค้าเข้ารับบริการ"""
        if not self.queue.is_empty():
            customer, transaction = self.queue.dequeue()
            print(f"กำลังบริการลูกค้า {customer} สำหรับธุรกรรม {transaction}")
        else:
            print("ไม่มีลูกค้าในคิว")
    
    def show_queue(self):
        """แสดงสถานะคิวปัจจุบัน"""
        print(f"คิวปัจจุบัน: {self.queue.items}")
        print(f"จำนวนลูกค้าในคิว: {self.queue.size()}")
    
    def estimate_wait_time(self):
        """แสดงเวลารอโดยประมาณ สมมติว่าธุรกรรมใช้เวลาเฉลี่ย 5 นาที/คน"""
        wait_time = self.queue.size() * 5  # สมมติว่าใช้เวลา 5 นาทีต่อคน
        print(f"เวลารอโดยประมาณ: {wait_time} นาที")


# ทดสอบการใช้งาน
bank_queue = BankQueue()

# เพิ่มลูกค้าเข้าคิว
bank_queue.add_customer("ชุติวัฒน์", "ฝากเงิน")
bank_queue.add_customer("ธัชชัย", "ถอนเงิน")
bank_queue.add_customer("ชญานนท์", "ชำระบิล")

# แสดงสถานะคิว
bank_queue.show_queue()

# แสดงเวลารอโดยประมาณ
bank_queue.estimate_wait_time()

# เสิร์ฟลูกค้า 2 คน
bank_queue.serve_customer()
bank_queue.serve_customer()

# แสดงสถานะคิวหลังจากเสิร์ฟลูกค้า
bank_queue.show_queue()

# แสดงเวลารอโดยประมาณอีกครั้ง
bank_queue.estimate_wait_time()

# เสิร์ฟลูกค้าคนถัดไป
bank_queue.serve_customer()

# แสดงสถานะคิวหลังจากเสิร์ฟลูกค้าครั้งสุดท้าย
bank_queue.show_queue()

# เสิร์ฟลูกค้าคนถัดไป (กรณีคิวว่าง)
bank_queue.serve_customer()
