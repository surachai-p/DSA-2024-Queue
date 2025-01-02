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


class Restaurant:
    def __init__(self):
        self.waiting_queue = Queue()
        
    def add_customer(self, name):
        """เพิ่มลูกค้าเข้าคิว"""
        self.waiting_queue.enqueue(name)
        print(f"ลูกค้า {name} เข้าคิวที่ {self.waiting_queue.size()}")
        
    def serve_customer(self):
        """เสิร์ฟลูกค้าจากคิว"""
        if not self.waiting_queue.is_empty():
            customer = self.waiting_queue.dequeue()
            print(f"กำลังเสิร์ฟลูกค้า: {customer}")
        else:
            print("ไม่มีลูกค้าในคิว")
            
    def show_queue(self):
        """แสดงสถานะคิว"""
        print(f"คิวปัจจุบัน: {self.waiting_queue.items}")
        print(f"จำนวนลูกค้าในคิว: {self.waiting_queue.size()}")


# ทดสอบการทำงานของร้านอาหาร
restaurant = Restaurant()

# เพิ่มลูกค้าเข้าคิว
restaurant.add_customer("อานนท์")
restaurant.add_customer("บุญมี")
restaurant.add_customer("จินดา")

# แสดงสถานะคิว
restaurant.show_queue()

# เสิร์ฟลูกค้า 2 คน
restaurant.serve_customer()
restaurant.serve_customer()

# แสดงสถานะคิวหลังจากเสิร์ฟลูกค้า
restaurant.show_queue()

# เสิร์ฟลูกค้าคนถัดไป
restaurant.serve_customer()

# แสดงสถานะคิวหลังจากเสิร์ฟลูกค้าครั้งสุดท้าย
restaurant.show_queue()

# เสิร์ฟลูกค้าคนถัดไป (กรณีคิวว่าง)
restaurant.serve_customer()
