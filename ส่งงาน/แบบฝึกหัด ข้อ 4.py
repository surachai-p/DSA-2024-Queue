class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, customer):
        self.items.append(customer)
        print(f"ลูกค้า {customer['name']} ({customer['transaction']}) ถูกเพิ่มในคิว")

    def dequeue(self):
        if not self.is_empty():
            customer = self.items.pop(0)
            print(f"เรียกลูกค้า {customer['name']} ({customer['transaction']}) เข้ารับบริการ")
            return customer
        print("ไม่มีลูกค้าในคิว")
        return None

    def size(self):
        return len(self.items)

    def display(self):
        if self.is_empty():
            print("คิวว่าง ไม่มีลูกค้ารออยู่")
        else:
            print("คิวปัจจุบัน:")
            for i, customer in enumerate(self.items, 1):
                print(f"  {i}. {customer['name']} ({customer['transaction']})")

    def estimated_wait_time(self, average_time_per_customer=5):
        """คำนวณเวลารอคิวโดยเฉลี่ย (หน่วย: นาที)"""
        wait_time = self.size() * average_time_per_customer
        print(f"ประมาณการเวลารอ: {wait_time} นาที")
        return wait_time


# ฟังก์ชันจำลองระบบคิวธนาคาร
def bank_queue_simulation():
    q = Queue()

    while True:
        print("\n--- เมนู ---")
        print("1. เพิ่มลูกค้าเข้าคิว")
        print("2. เรียกลูกค้าเข้ารับบริการ")
        print("3. แสดงจำนวนคิวที่รอ")
        print("4. แสดงประมาณการเวลารอ")
        print("5. แสดงคิวปัจจุบัน")
        print("6. ออกจากโปรแกรม")
        
        choice = input("เลือกเมนู (1-6): ")

        if choice == "1":
            name = input("ชื่อของลูกค้า: ")
            transaction = input("ประเภทธุรกรรม (ฝาก/ถอน/ชำระบิล): ")
            q.enqueue({"name": name, "transaction": transaction})
        elif choice == "2":
            q.dequeue()
        elif choice == "3":
            print(f"จำนวนลูกค้าที่รอ: {q.size()}")
        elif choice == "4":
            q.estimated_wait_time()
        elif choice == "5":
            q.display()
        elif choice == "6":
            print("ออกจากโปรแกรม")
            break
        else:
            print("กรุณาเลือกเมนูที่ถูกต้อง")

# เรียกฟังก์ชันหลัก
if __name__ == "__main__":
    bank_queue_simulation()
