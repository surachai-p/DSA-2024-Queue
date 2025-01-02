from collections import deque

class BarberShopQueue:
    def __init__(self):
        self.queue = deque()
        self.service_times = {
            "ตัดผม": 40,
            "สระ": 30,
            "ย้อมสี": 120,
        }

    def add_customer(self, name, service):
        """เพิ่มลูกค้าเข้าคิว พร้อมระบุบริการที่ต้องการ"""
        if service in self.service_times:
            self.queue.append((name, service))
            print(f"เพิ่มลูกค้า: {name} ({service}) เข้าคิวเรียบร้อย")
        else:
            print(f"บริการ '{service}' ไม่มีในระบบ")

    def show_queue(self):
        """แสดงรายชื่อลูกค้าที่รออยู่ในคิว"""
        if not self.queue:
            print("ไม่มีลูกค้าในคิว")
        else:
            print("แสดงคิว:")
            total_wait_time = 0
            for i, (name, service) in enumerate(self.queue, start=1):
                wait_time = self.service_times[service]
                total_wait_time += wait_time
                print(f"{i}. {name} - {service} (รอประมาณ {total_wait_time} นาที)")

    def call_next_customer(self):
        """เรียกลูกค้าคนถัดไป"""
        if not self.queue:
            print("ไม่มีลูกค้าในคิว")
        else:
            name, service = self.queue.popleft()
            print(f"เรียกลูกค้า: {name} ({service})")

    def estimated_wait_time(self):
        """แสดงเวลารอโดยประมาณ"""
        total_wait_time = sum(self.service_times[service] for _, service in self.queue)
        print(f"เวลารอโดยประมาณทั้งหมด: {total_wait_time} นาที")
        return total_wait_time

print("=== ร้านตัดผมคุณติ๋ม ===")
barber_shop = BarberShopQueue()
# เพิ่มลูกค้าเข้าคิว
barber_shop.add_customer("สมชาย", "ตัดผม")
barber_shop.add_customer("สมหญิง", "ย้อมสี")
# แสดงคิว
barber_shop.show_queue()
# เรียกลูกค้าคนถัดไป
barber_shop.call_next_customer()
# แสดงคิวที่เหลือ
barber_shop.show_queue()
