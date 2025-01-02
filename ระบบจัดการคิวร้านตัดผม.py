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


class HairSalonQueue:
    def __init__(self):
        self.queue = Queue()
    
    def add_customer(self, name, service_type):
        """เพิ่มลูกค้าเข้าคิวพร้อมกับระบุบริการที่ต้องการ"""
        self.queue.enqueue((name, service_type))
        print(f"ลูกค้า {name} เข้าคิวสำหรับบริการ {service_type}")
    
    def serve_customer(self):
        """เรียกลูกค้าเข้ารับบริการ"""
        if not self.queue.is_empty():
            customer, service = self.queue.dequeue()
            print(f"กำลังบริการลูกค้า {customer} สำหรับบริการ {service}")
        else:
            print("ไม่มีลูกค้าในคิว")
    
    def show_queue(self):
        """แสดงสถานะคิวปัจจุบัน"""
        print(f"คิวปัจจุบัน: {self.queue.items}")
        print(f"จำนวนลูกค้าในคิว: {self.queue.size()}")
    
    def estimate_wait_time(self):
        """แสดงเวลารอโดยประมาณ (ตัดผม 30 นาที, สระ 20 นาที, ย้อมสี 60 นาที)"""
        total_wait_time = 0
        for _, service in self.queue.items:
            if service == 'ตัดผม':
                total_wait_time += 30
            elif service == 'สระผม':
                total_wait_time += 20
            elif service == 'ย้อมสีผม':
                total_wait_time += 60
        print(f"เวลารอโดยประมาณ: {total_wait_time} นาที")


# ทดสอบการใช้งาน
salon_queue = HairSalonQueue()

# เพิ่มลูกค้าเข้าคิว
salon_queue.add_customer("ปองพล", "ตัดผม")
salon_queue.add_customer("ณัฐกิตติ์", "สระผม")
salon_queue.add_customer("อชิรกรณ์", "ย้อมสีผม")

# แสดงสถานะคิว
salon_queue.show_queue()

# แสดงเวลารอโดยประมาณ
salon_queue.estimate_wait_time()

# เสิร์ฟลูกค้า 2 คน
salon_queue.serve_customer()
salon_queue.serve_customer()

# แสดงสถานะคิวหลังจากเสิร์ฟลูกค้า
salon_queue.show_queue()

# แสดงเวลารอโดยประมาณอีกครั้ง
salon_queue.estimate_wait_time()

# เสิร์ฟลูกค้าคนถัดไป
salon_queue.serve_customer()

# แสดงสถานะคิวหลังจากเสิร์ฟลูกค้าครั้งสุดท้าย
salon_queue.show_queue()

# เสิร์ฟลูกค้าคนถัดไป (กรณีคิวว่าง)
salon_queue.serve_customer()
