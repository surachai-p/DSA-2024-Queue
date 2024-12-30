class Queue: # แบบฝึกหัดข้อที่3 
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def clear(self): # แบบฝึกหัดข้อที่1
        """ล้างข้อมูลทั้งหมดในคิว""" 
        self.items = []
        print("คิวถูกล้างเรียบร้อยแล้ว")

    def peek_last(self):# แบบฝึกหัดข้อที่2
        """ดูข้อมูลตัวสุดท้ายในคิวโดยไม่นำออก"""
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

# สร้างคลาส Restaurant
class Restaurant:
    def __init__(self):
        self.waiting_queue = Queue()
        
    def add_customer(self, name):
        self.waiting_queue.enqueue(name)
        print(f"ลูกค้า {name} เข้าคิวที่ {self.waiting_queue.size()}")
        
    def serve_customer(self):
        if not self.waiting_queue.is_empty():
            customer = self.waiting_queue.dequeue()
            print(f"กำลังเสิร์ฟลูกค้า: {customer}")
        else:
            print("ไม่มีลูกค้าในคิว")
            
    def show_queue(self):
        print(f"คิวปัจจุบัน: {self.waiting_queue.items}")
        print(f"จำนวนลูกค้าในคิว: {self.waiting_queue.size()}")

# ทดสอบโปรแกรม
restaurant = Restaurant()

# เพิ่มลูกค้าเข้าคิว
restaurant.add_customer("อานนท์")
restaurant.add_customer("บุญมี")
restaurant.add_customer("จินดา")

# แสดงสถานะคิว
restaurant.show_queue()

# ใช้งานเมธอด peek_last()
print(f"ลูกค้าคนสุดท้ายในคิว: {restaurant.waiting_queue.peek_last()}")

# ล้างคิว
restaurant.waiting_queue.clear()

# แสดงสถานะคิวอีกครั้ง
restaurant.show_queue()
