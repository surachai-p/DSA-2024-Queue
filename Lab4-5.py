class Customer:
    def __init__(self, name, service):
        self.name = name
        self.service = service
        self.service_time = self.get_service_time()

    def get_service_time(self):
        # ระบุเวลาที่ใช้ในบริการแต่ละประเภท
        service_times = {"ตัดผม": 30, "สระ": 20, "ย้อมสี": 60}
        return service_times.get(self.service, 0)

    def __str__(self):
        return f"{self.name} ({self.service}, {self.service_time} นาที)"


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


class HairSalonQueueSystem:
    def __init__(self):
        self.queue = Queue()

    def add_customer(self, name, service):
        customer = Customer(name, service)
        self.queue.enqueue(customer)
        print(f"เพิ่มลูกค้า {customer} เข้าคิวเรียบร้อยแล้ว")

    def call_next_customer(self):
        if self.queue.is_empty():
            print("ไม่มีลูกค้าในคิว")
        else:
            customer = self.queue.dequeue()
            print(f"กำลังให้บริการลูกค้า: {customer}")

    def show_queue_status(self):
        print(f"จำนวนลูกค้าที่รออยู่: {self.queue.size()}")
        self.queue.display()

    def estimate_wait_time(self):
        total_time = sum(customer.service_time for customer in self.queue.items)
        print(f"ประมาณการเวลารอทั้งหมด: {total_time} นาที")


# ทดสอบระบบจัดการคิวร้านตัดผม
salon_queue = HairSalonQueueSystem()

# เพิ่มลูกค้าเข้าคิว
salon_queue.add_customer("สมชาย", "ตัดผม")
salon_queue.add_customer("สมหญิง", "ย้อมสี")
salon_queue.add_customer("อนันต์", "สระ")

# แสดงสถานะคิว
salon_queue.show_queue_status()

# ประมาณการเวลารอ
salon_queue.estimate_wait_time()

# เรียกลูกค้าคนถัดไป
salon_queue.call_next_customer()

# แสดงสถานะคิวอีกครั้ง
salon_queue.show_queue_status()

# ประมาณการเวลารออีกครั้ง
salon_queue.estimate_wait_time()
