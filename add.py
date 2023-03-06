class StringCalculator:
    def add(self, numbers):
        if numbers == "":
            return 0
        else:
            x = [
                int(element) if int(element) < 1000 else 0
                for element in numbers.split(",")
            ]
            # print(x)
            if any(el < 0 for el in x):
                # print("Negative numbers not allowed")
                # raise Exception("Negative numbers not allowed")
                pass

            return sum(x)
