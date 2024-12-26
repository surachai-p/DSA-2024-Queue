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
    
    def size(self):
        return len(self.items)
    
    def display(self):
        if self.is_empty():
            print("คิวว่าง")
        else:
            for idx, item in enumerate(self.items, start=1):
                print(f"{idx}. {item}")

class BarberShopQueue:
    SERVICE_TIMES = {
        "ตัดผม": 30,
        "สระ": 20,
        "ย้อมสี": 60
    }

    def __init__(self):
        self.waiting_queue = Queue()
    
    def add_customer(self, name, service):
        """เพิ่มลูกค้าเข้าคิว พร้อมระบุบริการที่ต้องการ"""
        if service not in self.SERVICE_TIMES:
            print(f"บริการ '{service}' ไม่มีในระบบ กรุณาเลือกบริการใหม่")
            return
        self.waiting_queue.enqueue((name, service))
        print(f"ลูกค้า {name} ({service}) เข้าคิวที่ {self.waiting_queue.size()}")
    
    def show_queue(self):
        """แสดงรายชื่อลูกค้าที่รออยู่ในคิว"""
        if self.waiting_queue.is_empty():
            print("คิวว่าง ไม่มีลูกค้าในคิว")
        else:
            print("รายชื่อลูกค้าในคิว:")
            self.waiting_queue.display()
    
    def call_next_customer(self):
        """เรียกลูกค้าคนถัดไป"""
        customer = self.waiting_queue.dequeue()
        if customer is not None:
            name, service = customer
            print(f"กำลังให้บริการลูกค้า {name} ({service}) ใช้เวลาประมาณ {self.SERVICE_TIMES[service]} นาที")
    
    def estimate_wait_time(self):
        """แสดงเวลารอโดยประมาณ"""
        if self.waiting_queue.is_empty():
            print("ไม่มีลูกค้าในคิว ไม่ต้องรอเวลา")
            return
        
        total_time = 0
        print("เวลารอโดยประมาณสำหรับลูกค้าในคิว:")
        for idx, (name, service) in enumerate(self.waiting_queue.items, start=1):
            total_time += self.SERVICE_TIMES[service]
            print(f"{idx}. {name} ({service}) - รอประมาณ {total_time} นาที")
        print(f"เวลารอรวม: {total_time} นาที")

# ตัวอย่างการใช้งาน
if __name__ == "__main__":
    shop_queue = BarberShopQueue()

    # เพิ่มลูกค้าเข้าคิว
    shop_queue.add_customer("ธัยเทพ", "ตัดผม")
    shop_queue.add_customer("ศรสวรรค์", "สระ")
    shop_queue.add_customer("วิภัสศศิชา", "ย้อมสี")

    # แสดงรายชื่อลูกค้าในคิว
    shop_queue.show_queue()

    # แสดงเวลารอโดยประมาณ
    shop_queue.estimate_wait_time()

    # เรียกลูกค้าคนถัดไป
    shop_queue.call_next_customer()

    # แสดงสถานะคิวและเวลารออีกครั้ง
    shop_queue.show_queue()
    shop_queue.estimate_wait_time()

    # เรียกลูกค้าคนถัดไป
    shop_queue.call_next_customer()

    # เรียกลูกค้าคนถัดไป
    shop_queue.call_next_customer()

    # พยายามเรียกลูกค้าเมื่อคิวว่าง
    shop_queue.call_next_customer()
