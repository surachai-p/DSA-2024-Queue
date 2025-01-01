class Restaurant:
    def __init__(self):
        self.queue = []

    def add_customer(self, name):
        self.queue.append(name)

    def serve_customer(self):
        if self.queue:
            served_customer = self.queue.pop(0)
            print(f"เสิร์ฟลูกค้า : {served_customer}")
        else:
            print("ไม่มีลูกค้าในคิว")

    def show_queue(self):
        if self.queue:
            print("สถานะคิว :")
            for customer in self.queue:
                print(f"- {customer}")
        else:
            print("คิวว่าง")

    def clear(self):
        self.queue.clear()


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

# ล้างข้อมูลในคิว
restaurant.clear()

# แสดงสถานะคิวหลังจากล้างข้อมูล
restaurant.show_queue()