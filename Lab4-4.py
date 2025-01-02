class Customer:
    def __init__(self, name, transaction_type):
        self.name = name
        self.transaction_type = transaction_type

    def __str__(self):
        return f"{self.name} ({self.transaction_type})"


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
        print("คิวว่าง ไม่มีลูกค้าในคิว")
        return None
    
    def size(self):
        return len(self.items)
    
    def display(self):
        if self.is_empty():
            print("ไม่มีลูกค้าในคิว")
        else:
            print("คิวปัจจุบัน:")
            for i, customer in enumerate(self.items, start=1):
                print(f"{i}. {customer}")


class BankQueueSystem:
    def __init__(self):
        self.queue = Queue()
        self.average_time_per_customer = 5  # นาทีต่อคน

    def add_customer(self, name, transaction_type):
        customer = Customer(name, transaction_type)
        self.queue.enqueue(customer)
        print(f"เพิ่มลูกค้า {customer} เข้าคิวเรียบร้อยแล้ว")

    def call_customer(self):
        if self.queue.is_empty():
            print("ไม่มีลูกค้าในคิว")
        else:
            customer = self.queue.dequeue()
            print(f"กำลังให้บริการลูกค้า: {customer}")

    def show_queue_status(self):
        print(f"จำนวนลูกค้าที่รออยู่: {self.queue.size()}")
        self.queue.display()

    def estimate_wait_time(self):
        wait_time = self.queue.size() * self.average_time_per_customer
        print(f"ประมาณการเวลารอทั้งหมด: {wait_time} นาที")


# ทดสอบระบบคิวธนาคาร
bank_queue = BankQueueSystem()

# เพิ่มลูกค้าเข้าคิว
bank_queue.add_customer("สมชาย", "ฝากเงิน")
bank_queue.add_customer("สมหญิง", "ถอนเงิน")
bank_queue.add_customer("อนันต์", "ชำระบิล")

# แสดงสถานะคิว
bank_queue.show_queue_status()

# ประมาณการเวลารอ
bank_queue.estimate_wait_time()

# เรียกลูกค้าเข้ารับบริการ
bank_queue.call_customer()

# แสดงสถานะคิวอีกครั้ง
bank_queue.show_queue_status()

# ประมาณการเวลารออีกครั้ง
bank_queue.estimate_wait_time()
