class Queue:
    def __init__(self, max_size=None):
        self.items = []
        self.max_size = max_size  # กำหนดขนาดสูงสุดของคิว (สามารถกำหนดเป็น None เพื่อไม่จำกัดขนาด)

    def enqueue(self, item):
        if self.max_size and len(self.items) >= self.max_size:
            print("คิวเต็ม ไม่สามารถเพิ่มลูกค้าได้")
            return False
        self.items.append(item)
        return True
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None
    
    def size(self):
        return len(self.items)
    
    def is_empty(self):
        return len(self.items) == 0
    
    def peek_last(self):
        """ดูข้อมูลลูกค้าตัวสุดท้ายในคิวโดยไม่ทำการนำออก"""
        if not self.is_empty():
            return self.items[-1]
        return None

    def clear(self):
        """ล้างข้อมูลทั้งหมดในคิว"""
        self.items = []

class Restaurant:
    def __init__(self, max_queue_size=None):
        self.waiting_queue = Queue(max_size=max_queue_size)
        
    def add_customer(self, name):
        if self.waiting_queue.enqueue(name):
            print(f"ลูกค้า {name} เข้าคิวที่ {self.waiting_queue.size()}")
        else:
            print(f"ไม่สามารถเพิ่มลูกค้า {name} เข้าคิวได้")
        
    def serve_customer(self):
        if not self.waiting_queue.is_empty():
            customer = self.waiting_queue.dequeue()
            print(f"กำลังเสิร์ฟลูกค้า: {customer}")
        else:
            print("ไม่มีลูกค้าในคิว")
            
    def show_queue(self):
        print(f"คิวปัจจุบัน: {self.waiting_queue.items}")
        print(f"จำนวนลูกค้าในคิว: {self.waiting_queue.size()}")
    
    def peek_last_customer(self):
        last_customer = self.waiting_queue.peek_last()
        if last_customer:
            print(f"ลูกค้าตัวสุดท้ายในคิว: {last_customer}")
        else:
            print("คิวว่าง")
    
    def clear_queue(self):
        self.waiting_queue.clear()
        print("คิวทั้งหมดถูกล้างเรียบร้อยแล้ว")

# สร้างร้านอาหาร
restaurant = Restaurant(max_queue_size=5)  # จำกัดขนาดของคิวไว้ที่ 5

# เพิ่มลูกค้าเข้าคิว
restaurant.add_customer("อานนท์")
restaurant.add_customer("บุญมี")
restaurant.add_customer("จินดา")
restaurant.add_customer("ปกรณ์")
restaurant.add_customer("สาวิตรี")
restaurant.add_customer("วิลาศ")  # คิวเต็มจะไม่สามารถเพิ่มได้

# แสดงสถานะคิว
restaurant.show_queue()

# เสิร์ฟลูกค้า 2 คน
restaurant.serve_customer()
restaurant.serve_customer()

# แสดงสถานะคิวอีกครั้ง
restaurant.show_queue()

# ดูลูกค้าตัวสุดท้ายในคิว
restaurant.peek_last_customer()

# ล้างคิว
restaurant.clear_queue()

# แสดงสถานะคิวหลังจากล้าง
restaurant.show_queue()
