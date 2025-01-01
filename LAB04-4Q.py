
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("คิวว่าง ไม่สามารถเสิร์ฟลูกค้าได้.")
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def peek_first(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def clear(self):
        self.items.clear()


class BankQueueSystem:
    def __init__(self):
        self.waiting_queue = Queue()

    def add_customer(self, name, transaction_type):
        customer_info = {"name": name, "transaction_type": transaction_type}
        self.waiting_queue.enqueue(customer_info)
        print(f"ลูกค้า {name} ประเภทธุรกรรม : {transaction_type} เข้าคิวที่ {self.waiting_queue.size()}")

    def serve_customer(self):
        customer = self.waiting_queue.dequeue()
        if customer:
            print(f"กำลังเสิร์ฟลูกค้า : {customer['name']} ประเภทธุรกรรม : {customer['transaction_type']}")
        else:
            print("ไม่สามารถเสิร์ฟลูกค้าได้เนื่องจากคิวว่าง")

    def show_queue(self):
        if self.waiting_queue.is_empty():
            print("คิวว่าง")
        else:
            print(f"คิวปัจจุบัน : {[(customer['name'], customer['transaction_type']) for customer in self.waiting_queue.items]}")
        print(f"จำนวนลูกค้าในคิว : {self.waiting_queue.size()}")

    def estimated_wait_time(self):
        if self.waiting_queue.is_empty():
            print("คิวว่าง ไม่มีลูกค้าให้คำนวณเวลารอ")
        else:
            wait_time = self.waiting_queue.size() * 5
            print(f"เวลารอประมาณ : {wait_time} นาที")



bank_system = BankQueueSystem()

# เพิ่มลูกค้าเข้าคิว
bank_system.add_customer("คนเก่ง", "ฝากเงิน")
bank_system.add_customer("สมชื่อ", "ถอนเงิน")
bank_system.add_customer("วิชา", "ชำระบิล")

# แสดงสถานะคิว
bank_system.show_queue()

# แสดงประมาณการเวลารอ
bank_system.estimated_wait_time()

# เสิร์ฟลูกค้า 2 คน
bank_system.serve_customer()
bank_system.serve_customer()

# แสดงสถานะคิวอีกครั้ง
bank_system.show_queue()

# แสดงประมาณการเวลารออีกครั้ง
bank_system.estimated_wait_time()

# ล้างคิว
bank_system.waiting_queue.clear()

# แสดงสถานะคิวหลังจากล้าง
bank_system.show_queue()