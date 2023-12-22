import random

class NumberEncryptor:
    def __init__(self, number):
        self.number = number
        self._encrypt()

    def _encrypt(self):
        operation = random.choice(['+', '-', '*', '/'])
        operand = random.randint(1, 10)

        if operation == '+':
            self.number += operand
        elif operation == '-':
            self.number -= operand
        elif operation == '*':
            self.number *= operand
        elif operation == '/':
            if operand != 0:
                self.number /= operand

    def decrypt(self):
        return self.number

if __name__ == "__main__":
    input_numbers = [42, 99, 123, 7]

    encrypted_numbers = []
    for num in input_numbers:
        encryptor = NumberEncryptor(num)
        encrypted_numbers.append(encryptor)

    for encrypted_number in encrypted_numbers:
        decrypted_result = encrypted_number.decrypt()
        print(f"Зашифроване число: {encrypted_number}, Розшифроване число: {decrypted_result}")