import pickle
import struct
import os

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_grade(self):
        return self.grade

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_grade(self, grade):
        self.grade = grade

    def __str__(self):
        return "{:<15} | {:3d} лет | {:.2f}".format(self.name, self.age, self.grade)


class BinaryFileDemo:
    FILE_NAME = "students.bin"

    @staticmethod
    def create_students():
        students = [
            Student("Иванов Иван", 19, 4.5),
            Student("Петрова Анна", 20, 4.8),
            Student("Сидоров Сергей", 18, 3.9),
            Student("Козлова Мария", 21, 5.0),
            Student("Смирнов Алексей", 19, 4.2),
            Student("Новикова Елена", 20, 4.7),
            Student("Морозов Дмитрий", 18, 3.8),
            Student("Волкова Ольга", 22, 4.9),
            Student("Павлов Андрей", 19, 4.1),
            Student("Соколова Татьяна", 20, 4.6)
        ]
        return students

    @staticmethod
    def print_students(students):
        print("{:<15} | {:<8} | {}".format("Имя", "Возраст", "Оценка"))
        for s in students:
            print(s)
        print("Всего студентов:", len(students))

    @staticmethod
    def write_students_to_file(students, filename):
        try:
            with open(filename, "wb") as f:
                pickle.dump(len(students), f)
                for s in students:
                    pickle.dump(s, f)
            print("  Успешно записано {} студентов".format(len(students)))
            print("  Файл:", filename)
        except IOError as e:
            print("  Ошибка при записи:", e)

    @staticmethod
    def read_students_from_file(filename):
        students = []
        try:
            with open(filename, "rb") as f:
                count = pickle.load(f)
                for _ in range(count):
                    s = pickle.load(f)
                    students.append(s)
            print("  Успешно прочитано {} студентов".format(len(students)))
        except FileNotFoundError:
            print("  Файл не найден:", filename)
        except (IOError, pickle.PickleError) as e:
            print("  Ошибка при чтении:", e)
        return students

    @staticmethod
    def write_students_with_data_stream(students, filename):
        try:
            with open(filename, "wb") as f:
               f.write(struct.pack('>i', len(students))) 
                for s in students:
                    name_bytes = s.get_name().encode('utf-8')
                    f.write(struct.pack('>H', len(name_bytes)))
                    f.write(name_bytes)
                    f.write(struct.pack('>i', s.get_age()))
                    f.write(struct.pack('>d', s.get_grade()))
            print("  DataOutputStream: записано {} студентов".format(len(students)))
        except IOError as e:
            print("  Ошибка при записи:", e)

    @staticmethod
    def read_students_with_data_stream(filename):
        students = []
        try:
            with open(filename, "rb") as f:
                data = f.read()
                if len(data) == 0:
                    return students
                buf = memoryview(data)
                pos = 0
                count = struct.unpack_from('>i', buf, pos)[0]
                pos += 4
                for _ in range(count):
                    name_len = struct.unpack_from('>H', buf, pos)[0]
                    pos += 2
                    name = buf[pos:pos+name_len].tobytes().decode('utf-8')
                    pos += name_len
                    age = struct.unpack_from('>i', buf, pos)[0]
                    pos += 4
                    grade = struct.unpack_from('>d', buf, pos)[0]
                    pos += 8
                    students.append(Student(name, age, grade))
            print("  DataInputStream: прочитано {} студентов".format(len(students)))
        except FileNotFoundError:
            print("  Файл не найден:", filename)
        except (IOError, struct.error) as e:
            print("  Ошибка при чтении:", e)
        return students

    @staticmethod
    def verify_data(original, read):
        if len(original) != len(read):
            print("  Количество студентов не совпадает!")
            return
        all_match = True
        for i, (o, r) in enumerate(zip(original, read)):
            if (o.get_name() != r.get_name() or
                o.get_age() != r.get_age() or
                abs(o.get_grade() - r.get_grade()) > 0.001):
                print("  Несовпадение в записи {}".format(i+1))
                all_match = False
        if all_match:
            print("  Данные полностью совпадают!")
            print("  Целостность данных сохранена!")
        else:
            print("  Обнаружены несовпадения в данных!")

    @staticmethod
    def show_file_info(filename):
        try:
            file_size = os.path.getsize(filename)
            print("\nИНФОРМАЦИЯ О ФАЙЛЕ")
            print("Имя файла:", filename)
            print("Размер: {} байт".format(file_size))
            if file_size > 0:
                per_student = file_size // 10
                print("Размер на одного студента: {} байт".format(per_student))

            print("\nHEX-СОДЕРЖИМОЕ (первые 64 байта)")
            with open(filename, "rb") as f:
                chunk = f.read(64)
                for i, b in enumerate(chunk):
                    print("{:02X}".format(b), end=" ")
                    if (i + 1) % 16 == 0:
                        print()
                if len(chunk) % 16 != 0:
                    print()
        except OSError as e:
            print("Не удалось прочитать HEX:", e)

    @staticmethod
    def main():
        students = BinaryFileDemo.create_students()
        print("\n1. СОЗДАНЫ СТУДЕНТЫ:")
        BinaryFileDemo.print_students(students)

        print("\n2. ЗАПИСЬ В БИНАРНЫЙ ФАЙЛ...")
        BinaryFileDemo.write_students_to_file(students, BinaryFileDemo.FILE_NAME)

        print("\n3. ЧТЕНИЕ ИЗ БИНАРНОГО ФАЙЛА...")
        read_students = BinaryFileDemo.read_students_from_file(BinaryFileDemo.FILE_NAME)

        print("\n4. ПРОЧИТАННЫЕ СТУДЕНТЫ:")
        BinaryFileDemo.print_students(read_students)

        print("\n5. ПРОВЕРКА ЦЕЛОСТНОСТИ ДАННЫХ:")
        BinaryFileDemo.verify_data(students, read_students)

        BinaryFileDemo.show_file_info(BinaryFileDemo.FILE_NAME)


        data_file = "students_data.bin"
        print("\n--- Дополнительная проверка DataOutputStream/DataInputStream ---")
        BinaryFileDemo.write_students_with_data_stream(students, data_file)
        read_data = BinaryFileDemo.read_students_with_data_stream(data_file)
        print("Прочитано через DataInputStream:")
        BinaryFileDemo.print_students(read_data)
        BinaryFileDemo.verify_data(students, read_data)


if __name__ == "__main__":
    BinaryFileDemo.main()
