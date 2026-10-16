from app.service import TaskService


def run():
    service = TaskService()

    while True:
        print("\n=== TaskFlow ===")
        print("1. Tambah tugas")
        print("2. Lihat tugas")
        print("3. Selesaikan tugas")
        print("4. Keluar")

        choice = input("Pilih menu: ").strip()

        if choice == "1":
            title = input("Judul tugas: ")
            try:
                task = service.create_task(title)
                print(f"Tugas berhasil dibuat: {task.task_id}")
            except ValueError as error:
                print(error)

        elif choice == "2":
            for task in service.list_tasks():
                status = "Selesai" if task.completed else "Belum"
                print(f"{task.task_id}. {task.title} - {status}")

        elif choice == "3":
            try:
                task_id = int(input("ID tugas: "))
                if service.complete_task(task_id):
                    print("Tugas berhasil diselesaikan.")
                else:
                    print("Tugas tidak ditemukan.")
            except ValueError:
                print("ID harus berupa angka.")

        elif choice == "4":
            print("Terima kasih.")
            break

        else:
            print("Pilihan tidak valid.")
