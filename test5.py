class Customer:
    def __init__(self, name, service):
        self.name = name
        self.service = service
        self.estimated_time = self.get_estimated_time()

    def get_estimated_time(self):
        if self.service == "ตัดผม":
            return 30
        elif self.service == "สระ":
            return 20
        elif self.service == "ย้อมสี":
            return 60
        else:
            return 0

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, customer):
        self.items.append(customer)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def display(self):
        if not self.is_empty():
            for customer in self.items:
                print(f"ชื่อ: {customer.name}, บริการ: {customer.service}, เวลาประมาณ: {customer.estimated_time} นาที")
        else:
            print("คิวว่าง")

# สร้างคิว
queue = Queue()

# เพิ่มลูกค้าเข้าคิว
queue.enqueue(Customer("สมชาย", "ตัดผม"))
queue.enqueue(Customer("นางสาวบุญมี", "สระ"))
queue.enqueue(Customer("นายสิทธา", "ย้อมสี"))

# แสดงคิว
queue.display()

# เรียกลูกค้าคนถัดไป
customer = queue.dequeue()
if customer:
    print(f"เรียกลูกค้า: {customer.name}")
else:
    print("ไม่มีลูกค้าในคิว")