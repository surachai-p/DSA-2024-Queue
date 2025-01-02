class Restaurant:
    def __init__(self):
        self.queue = []  # เก็บคิวลูกค้าในรูปแบบลิสต์

    def add_customer(self, name):
        self.queue.append(name)  # เพิ่มชื่อลูกค้าเข้าคิว
        print(f"{name} เข้าคิวแล้ว")

    def serve_customer(self):
        if self.queue:
            served_customer = self.queue.pop(0)  # เสิร์ฟลูกค้าคนแรกในคิว
            print(f"กำลังเสิร์ฟ {served_customer}")
        else:
            print("ไม่มีลูกค้าในคิว")

    def show_queue(self):
        if self.queue:
            print("คิวลูกค้าในปัจจุบัน:")
            for i, name in enumerate(self.queue, start=1):
                print(f"{i}. {name}")
        else:
            print("ไม่มีลูกค้าในคิว")

# สร้างร้านอาหาร
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

# แสดงสถานะคิวอีกครั้ง
restaurant.show_queue()
