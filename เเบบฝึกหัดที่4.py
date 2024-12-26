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
        else:
            print("คิวว่าง ไม่มีลูกค้าในคิว")
            return None
    
    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("คิวว่าง ไม่มีข้อมูลหน้าคิว")
            return None
    
    def size(self):
        return len(self.items)
    
    def display(self):
        if self.is_empty():
            print("คิวว่าง")
        else:
            print(f"Queue: {self.items}")

class BankQueueSystem:
    def __init__(self):
        self.waiting_queue = Queue()
        self.average_service_time = 5  # เวลาบริการเฉลี่ย 5 นาทีต่อคน
    
    def add_customer(self, name, transaction_type):
        """เพิ่มลูกค้าเข้าคิว"""
        self.waiting_queue.enqueue((name, transaction_type))
        print(f"ลูกค้า {name} ({transaction_type}) เข้าคิวที่ {self.waiting_queue.size()}")
    
    def serve_customer(self):
        """เรียกลูกค้าเข้ารับบริการ"""
        customer = self.waiting_queue.dequeue()
        if customer is not None:
            name, transaction_type = customer
            print(f"กำลังให้บริการลูกค้า {name} ({transaction_type})")
    
    def show_queue_status(self):
        """แสดงสถานะของคิว"""
        if self.waiting_queue.is_empty():
            print("คิวว่าง ไม่มีลูกค้าในคิว")
        else:
            print("สถานะคิวปัจจุบัน:")
            for idx, (name, transaction_type) in enumerate(self.waiting_queue.items, start=1):
                print(f"{idx}. {name} ({transaction_type})")
            print(f"จำนวนลูกค้าในคิว: {self.waiting_queue.size()}")
    
    def estimate_wait_time(self):
        """แสดงประมาณการเวลารอ"""
        num_customers = self.waiting_queue.size()
        estimated_time = num_customers * self.average_service_time
        if num_customers == 0:
            print("ไม่มีลูกค้าในคิว ไม่ต้องรอเวลา")
        else:
            print(f"จำนวนลูกค้าในคิว: {num_customers}")
            print(f"ประมาณการเวลารอ: {estimated_time} นาที")

# ตัวอย่างการใช้งาน
if __name__ == "__main__":
    bank_queue = BankQueueSystem()

    # เพิ่มลูกค้าเข้าคิว
    bank_queue.add_customer("วิภัสศศิชา", "ฝาก")
    bank_queue.add_customer("ศรสวรรค์", "ถอน")
    bank_queue.add_customer("ธัญเทพ", "ชำระบิล")

    # แสดงสถานะคิว
    bank_queue.show_queue_status()

    # ประมาณการเวลารอ
    bank_queue.estimate_wait_time()

    # ให้บริการลูกค้า
    bank_queue.serve_customer()
    bank_queue.serve_customer()

    # แสดงสถานะคิวและเวลารออีกครั้ง
    bank_queue.show_queue_status()
    bank_queue.estimate_wait_time()

    # ให้บริการลูกค้าคนสุดท้าย
    bank_queue.serve_customer()

    # พยายามเรียกลูกค้าเมื่อคิวว่าง
    bank_queue.serve_customer()
