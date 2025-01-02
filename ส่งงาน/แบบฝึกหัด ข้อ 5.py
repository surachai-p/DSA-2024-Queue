class BarberQueue:
    def __init__(self):
        self.queue = []
        self.services_time = {"ตัดผม": 30, "สระ": 20, "ย้อมสี": 60}

    def add_customer(self, name, service):
        """เพิ่มลูกค้าเข้าคิว พร้อมระบุบริการที่ต้องการ"""
        if service in self.services_time:
            self.queue.append({"name": name, "service": service})
            print(f"เพิ่มลูกค้า: {name} ({service})")
        else:
            print(f"บริการ '{service}' ไม่มีในระบบ")

    def call_next(self):
        """เรียกลูกค้าคนถัดไป"""
        if self.queue:
            customer = self.queue.pop(0)
            print(f"เรียกลูกค้า: {customer['name']} ({customer['service']})")
        else:
            print("ไม่มีลูกค้าในคิว")

    def display_queue(self):
        """แสดงรายชื่อลูกค้าที่รออยู่ในคิว"""
        if not self.queue:
            print("คิวว่าง ไม่มีลูกค้ารออยู่")
        else:
            print("คิวปัจจุบัน:")
            total_time = 0
            for i, customer in enumerate(self.queue, 1):
                service_time = self.services_time[customer["service"]]
                total_time += service_time
                print(f"  {i}. {customer['name']} - {customer['service']} (รอประมาณ {total_time} นาที)")

    def estimated_wait_time(self):
        """แสดงเวลารอโดยประมาณ"""
        total_time = sum(self.services_time[customer["service"]] for customer in self.queue)
        print(f"เวลารอโดยประมาณทั้งหมด: {total_time} นาที")


# ฟังก์ชันหลัก
def barber_shop_simulation():
    barber_queue = BarberQueue()

    while True:
        print("\n=== ร้านตัดผมคุณหรีด ===")
        print("1. เพิ่มลูกค้า")
        print("2. เรียกลูกค้าคนถัดไป")
        print("3. แสดงคิว")
        print("4. ออกจากโปรแกรม")
        choice = input("เลือกเมนู (1-5): ")

        if choice == "1":
            name = input("ชื่อของลูกค้า: ")
            service = input("บริการที่ต้องการ (ตัดผม/สระ/ย้อมสี): ")
            barber_queue.add_customer(name, service)
        elif choice == "2":
            barber_queue.call_next()
        elif choice == "3":
            barber_queue.display_queue()
        elif choice == "4":
            print("ออกจากโปรแกรม")
            break
        else:
            print("กรุณาเลือกเมนูที่ถูกต้อง")


# เรียกฟังก์ชันหลัก
if __name__ == "__main__":
    barber_shop_simulation()
