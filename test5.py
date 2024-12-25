class Customer:
    def __init__(self, name, service):
        self.name = name
        self.service = service

class BarberShop:
    def __init__(self):
        self.queue = []
        self.service_times = {
            "ตัดผม": 30,
            "ย้อมสี": 60,
        }

    def add_customer(self, name, service):
        if service not in self.service_times:
            print("ไม่มีบริการนี้")
            return
        customer = Customer(name, service)
        self.queue.append(customer)
        print(f"ลูกค้า {name} ต้องการ {service} เข้าคิวแล้ว")

    def show_queue(self):
        if not self.queue:
            print("ไม่มีลูกค้าในคิว")
            return
        print("คิวลูกค้า:")
        for i, customer in enumerate(self.queue):
            print(f"{i+1}. {customer.name} ({customer.service})")

    def call_next_customer(self):
        if not self.queue:
            print("ไม่มีลูกค้าในคิว")
            return
        customer = self.queue.pop(0)  # ดึงลูกค้าคนแรกออกจากคิว
        print(f"กำลังเรียก: {customer.name} ({customer.service})")

    def estimate_waiting_time(self):
        if not self.queue:
            print("ไม่มีลูกค้าในคิว")
            return 0

        total_waiting_time = 0
        for customer in self.queue:
            total_waiting_time += self.service_times[customer.service]

        print(f"เวลารอโดยประมาณ: {total_waiting_time} นาที")
        return total_waiting_time

# ตัวอย่างการใช้งาน
barber_shop = BarberShop()

barber_shop.add_customer("สมชาย", "ตัดผม")
barber_shop.add_customer("สมใจ", "ย้อมสี") # บริการที่ไม่มี

barber_shop.show_queue()
barber_shop.estimate_waiting_time()

barber_shop.call_next_customer()
barber_shop.show_queue()
barber_shop.estimate_waiting_time()

