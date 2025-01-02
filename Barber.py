class HairSalonQueue:
    def __init__(self):
        self.queue = []  # เก็บคิวลูกค้าในรูปแบบ (ชื่อ, บริการที่ต้องการ)

    # เพิ่มลูกค้าเข้าคิว
    def add_customer(self, name, service):
        self.queue.append((name, service))
        print(f"เพิ่มลูกค้า: {name} ({service})")

    # แสดงคิวลูกค้าพร้อมเวลารอโดยประมาณ
    def show_queue(self):
        if self.queue:
            print("แสดงคิว:")
            total_wait_time = 0
            for i, (name, service) in enumerate(self.queue, start=1):
                wait_time = self._get_service_time(service)
                total_wait_time += wait_time
                print(f"{i}. {name} - {service} (รอประมาณ {total_wait_time} นาที)")
        else:
            print("ไม่มีลูกค้าในคิว")

    # เรียกลูกค้าคนถัดไป
    def serve_customer(self):
        if self.queue:
            name, service = self.queue.pop(0)
            print(f"เรียกลูกค้า: {name} ({service})")
        else:
            print("ไม่มีลูกค้าในคิว")

    # เวลาที่ใช้สำหรับบริการแต่ละประเภท
    def _get_service_time(self, service):
        service_times = {
            "ตัดผม": 30,
            "สระ": 20,
            "ย้อมสี": 60
        }
        return service_times.get(service, 0)

# ตัวอย่างการใช้งาน
print("=== ร้านตัดผมคุณหรีด ===")
salon = HairSalonQueue()

# เพิ่มลูกค้าเข้าคิว
salon.add_customer("สมชาย", "ตัดผม")
salon.add_customer("สมหญิง", "ย้อมสี")

# แสดงคิว
salon.show_queue()

# เรียกลูกค้าคนถัดไป
salon.serve_customer()

# แสดงคิวที่เหลือ
salon.show_queue()
