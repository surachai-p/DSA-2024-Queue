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
    
    def size(self):
        return len(self.items)
    
    def display(self):
        return self.items


class BankQueue:
    def __init__(self):
        self.queue = Queue()
        self.avg_service_time = 5  # ธุรกรรมใช้เวลาเฉลี่ย 5 นาที/คน
    
    def add_customer(self, name, transaction_type):
        self.queue.enqueue((name, transaction_type))
        print(f"ลูกค้า {name} ({transaction_type}) เข้าคิวที่ {self.queue.size()}")
    
    def serve_customer(self):
        if not self.queue.is_empty():
            customer = self.queue.dequeue()
            print(f"กำลังให้บริการลูกค้า: {customer[0]} ({customer[1]})")
        else:
            print("ไม่มีลูกค้าในคิว")
    
    def show_queue(self):
        if self.queue.is_empty():
            print("ไม่มีลูกค้าในคิว")
        else:
            print("คิวปัจจุบัน:")
            for i, customer in enumerate(self.queue.display(), 1):
                print(f"{i}. {customer[0]} - {customer[1]}")
            print(f"จำนวนลูกค้าในคิว: {self.queue.size()}")
    
    def estimate_wait_time(self):
        wait_time = self.queue.size() * self.avg_service_time
        print(f"เวลารอโดยประมาณ: {wait_time} นาที (เฉลี่ย {self.avg_service_time} นาที/คน)")


# เมนูสำหรับให้ผู้ใช้เลือกคำสั่ง
def main():
    bank_queue = BankQueue()
    
    while True:
        print("\n=== ระบบคิวธนาคาร ===")
        print("1. เพิ่มลูกค้าเข้าคิว")
        print("2. เรียกลูกค้าเข้ารับบริการ")
        print("3. แสดงคิวที่รอ")
        print("4. แสดงเวลารอโดยประมาณ")
        print("5. ออกจากโปรแกรม")
        
        choice = input("เลือกคำสั่ง: ")
        
        if choice == "1":
            name = input("ชื่อลูกค้า: ")
            transaction_type = input("ประเภทธุรกรรม (ฝาก/ถอน/ชำระบิล): ")
            bank_queue.add_customer(name, transaction_type)
        elif choice == "2":
            bank_queue.serve_customer()
        elif choice == "3":
            bank_queue.show_queue()
        elif choice == "4":
            bank_queue.estimate_wait_time()
        elif choice == "5":
            print("ออกจากโปรแกรม")
            break
        else:
            print("เลือกคำสั่งไม่ถูกต้อง กรุณาลองใหม่")

# เรียกใช้งานโปรแกรม
if __name__ == "__main__":
    main()
