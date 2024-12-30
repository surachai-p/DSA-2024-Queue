class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """เพิ่มข้อมูลเข้าคิว"""
        self.items.append(item)

    def dequeue(self):
        """นำข้อมูลออกจากคิว"""
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def is_empty(self):
        """ตรวจสอบว่าคิวว่างหรือไม่"""
        return len(self.items) == 0

    def size(self):
        """คืนค่าจำนวนข้อมูลในคิว"""
        return len(self.items)


class BarberShopQueue:
    def __init__(self):
        self.queue = Queue()
        self.service_times = {"ตัดผม": 30, "สระ": 20, "ย้อมสี": 60}

    def add_customer(self, name, service):
        """เพิ่มลูกค้าเข้าคิวพร้อมระบุบริการ"""
        if service in self.service_times:
            self.queue.enqueue({"name": name, "service": service})
            print(f"เพิ่มลูกค้า: {name} ({service}) เข้าคิว")
        else:
            print(f"บริการ '{service}' ไม่มีในระบบ")

    def show_queue(self):
        """แสดงรายชื่อลูกค้าในคิวพร้อมเวลารอโดยประมาณ"""
        if self.queue.is_empty():
            print("ไม่มีลูกค้าในคิว")
        else:
            print("คิวปัจจุบัน:")
            total_wait_time = 0
            for i, customer in enumerate(self.queue.items, start=1):
                service_time = self.service_times[customer["service"]]
                total_wait_time += service_time
                print(f"{i}. {customer['name']} - {customer['service']} (รอประมาณ {total_wait_time} นาที)")

    def call_next_customer(self):
        """เรียกลูกค้าคนถัดไป"""
        if not self.queue.is_empty():
            customer = self.queue.dequeue()
            print(f"กำลังให้บริการลูกค้า: {customer['name']} ({customer['service']})")
        else:
            print("ไม่มีลูกค้าในคิว")

    def estimate_total_wait_time(self):
        """แสดงเวลารอโดยประมาณทั้งหมด"""
        total_time = sum(self.service_times[customer["service"]] for customer in self.queue.items)
        print(f"เวลารอรวมประมาณ: {total_time} นาที")


# ตัวอย่างการใช้งานระบบคิวร้านตัดผม
print("=== ร้านตัดผมคุณหรีด ===")
barber_shop = BarberShopQueue()

# เพิ่มลูกค้าเข้าคิว
barber_shop.add_customer("สมชาย", "ตัดผม")
barber_shop.add_customer("สมหญิง", "ย้อมสี")

# แสดงคิว
barber_shop.show_queue()

# เรียกลูกค้าคนถัดไป
barber_shop.call_next_customer()

# แสดงคิวอีกครั้ง
barber_shop.show_queue()
