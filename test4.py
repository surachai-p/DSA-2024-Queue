class Customer:
    def __init__(self, name, transaction_type):
        self.name = name
        self.transaction_type = transaction_type

class Queue:
    def __init__(self, capacity):
        self.items = [None] * capacity  # สร้าง list ขนาด capacity
        self.head = 0
        self.tail = 0
        self.size = 0
        self.capacity = capacity

    def is_empty(self):
        return self.size == 0

    def is_full(self):
      return self.size == self.capacity

    def enqueue(self, item):
        if self.is_full():
            print("คิวเต็มแล้ว ไม่สามารถเพิ่มลูกค้าได้")
            return
        self.items[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity # วนรอบเมื่อ tail เกิน capacity
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        item = self.items[self.head]
        self.items[self.head] = None # Clear the dequeued slot
        self.head = (self.head + 1) % self.capacity # วนรอบเมื่อ head เกิน capacity
        self.size -= 1
        return item

    def queue_size(self):
        return self.size

    def display(self):
        if self.is_empty():
            print("คิวว่าง")
            return
        print("คิวปัจจุบัน:")
        current = self.head
        for _ in range(self.size):
          print(f"  - {self.items[current].name} ({self.items[current].transaction_type})")
          current = (current + 1) % self.capacity
        

class Bank:
    def __init__(self, queue_capacity):
        self.waiting_queue = Queue(queue_capacity)
        self.processing_time = 5  # นาที/คน

    def add_customer(self, name, transaction_type):
        customer = Customer(name, transaction_type)
        self.waiting_queue.enqueue(customer)
        print(f"ลูกค้า {name} ({transaction_type}) เข้าคิว")

    def call_customer(self):
        customer = self.waiting_queue.dequeue()
        if customer:
            print(f"กำลังเรียก: {customer.name} ({customer.transaction_type})")
        else:
            print("ไม่มีลูกค้าในคิว")

    def show_queue_status(self):
        self.waiting_queue.display()
        queue_size = self.waiting_queue.queue_size()
        print(f"จำนวนคิวที่รอ: {queue_size} คน")
        estimated_time = queue_size * self.processing_time
        print(f"ประมาณการเวลารอ: {estimated_time} นาที")

# ตัวอย่างการใช้งาน
bank = Bank(5) # กำหนดขนาดคิวสูงสุด 5 คน
bank.add_customer("ธัญเทพ", "ฝาก")
bank.add_customer("วิภัสศศิชา", "ถอน")
bank.add_customer("ศรสวรรค์", "ชำระบิล")
bank.add_customer("กุ๊กไก่", "ฝาก") # คิวเต็ม

bank.show_queue_status()

bank.call_customer()
bank.call_customer()

bank.show_queue_status()