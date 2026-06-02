import os

while True:
    print("\n===== CyberShield IDS =====")
    print("1. Train Model")
    print("2. Run Detection")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        os.system("python src/train_model.py")

    elif choice == "2":
        os.system("python src/detect.py")

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid Choice")