## การใช้คิว ในการจำลองการรอคิวร้านอาหารถือเป็นวิธีการที่เหมาะสม เพราะคิวทำงานแบบ FIFO คือ ลูกค้าที่เข้าคิวก่อนจะได้รับบริการก่อน ลูกค้าที่เข้าคิวทีหลังจะได้รับบริการตามลำดับ

class Queue:
    def __init__(self, max_size=None):
        self.items = []
        self.max_size = max_size

    def enqueue(self, item):
        if self.max_size and len(self.items) >= self.max_size:
            print("คิวเต็ม! ไม่สามารถเพิ่มลูกค้าได้.")
        else:
            self.items.append(item)
            print(f"ลูกค้า {item} เข้าคิวที่ {len(self.items)}")

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

    def peek_last(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def clear(self):
        self.items.clear()


class Restaurant:
    def __init__(self, max_queue_size=None):
        self.waiting_queue = Queue(max_size=max_queue_size)
        
    def add_customer(self, name):
        self.waiting_queue.enqueue(name)

    def serve_customer(self):
        customer = self.waiting_queue.dequeue()
        if customer:
            print(f"กำลังเสิร์ฟลูกค้า: {customer}")
        else:
            print("ไม่สามารถเสิร์ฟลูกค้าได้เนื่องจากคิวว่าง")

    def show_queue(self):
        if self.waiting_queue.is_empty():
            print("คิวว่าง")
        else:
            print(f"คิวปัจจุบัน: {self.waiting_queue.items}")
        print(f"จำนวนลูกค้าในคิว: {self.waiting_queue.size()}")

    def peek_last_customer(self):
        last_customer = self.waiting_queue.peek_last()
        if last_customer:
            print(f"ลูกค้าคนสุดท้ายในคิว: {last_customer}")
        else:
            print("คิวว่าง")


restaurant = Restaurant(max_queue_size=3)

# เพิ่มลูกค้าเข้าคิว
restaurant.add_customer("อานนท์")
restaurant.add_customer("บุญมี")
restaurant.add_customer("จินดา")

# คิวเต็มแล้ว
restaurant.add_customer("สมชาย")  # จะเกิดข้อความคิวเต็ม

# แสดงสถานะคิว
restaurant.show_queue()

# เสิร์ฟลูกค้า 2 คน
restaurant.serve_customer()
restaurant.serve_customer()

# แสดงสถานะคิวอีกครั้ง
restaurant.show_queue()

# ล้างคิว
restaurant.waiting_queue.clear()

# แสดงสถานะคิวหลังจากล้าง
restaurant.show_queue()