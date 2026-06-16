import string


class PlayfairCipher:
    """
    PlayFair Cipher.
    Quy ước:
    - Chỉ lấy chữ A-Z.
    - J được thay bằng I.
    - Nếu cặp ký tự bị trùng, chèn X.
    - Nếu bản rõ bị lẻ ký tự, thêm X cuối chuỗi.
    """

    def __init__(self, key: str):
        self.key = self.clean_text(key)

        if not self.key:
            raise ValueError("Khóa không được để trống.")

        self.matrix = self.create_matrix()
        self.position = self.create_position_map()

    @staticmethod
    def clean_text(text: str) -> str:
        text = text.upper().replace("J", "I")
        return "".join(ch for ch in text if ch in string.ascii_uppercase)

    def create_matrix(self):
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Không dùng J
        used = set()
        letters = []

        for ch in self.key + alphabet:
            if ch not in used and ch in alphabet:
                used.add(ch)
                letters.append(ch)

        return [letters[i:i + 5] for i in range(0, 25, 5)]

    def create_position_map(self):
        position = {}

        for row in range(5):
            for col in range(5):
                position[self.matrix[row][col]] = (row, col)

        return position

    def prepare_plaintext(self, plaintext: str) -> str:
        text = self.clean_text(plaintext)

        if not text:
            raise ValueError("Bản rõ không được để trống.")

        result = []
        i = 0

        while i < len(text):
            first = text[i]

            if i + 1 >= len(text):
                second = "X"
                i += 1
            else:
                second = text[i + 1]

                if first == second:
                    second = "X"
                    i += 1
                else:
                    i += 2

            result.append(first + second)

        return "".join(result)

    def prepare_ciphertext(self, ciphertext: str) -> str:
        text = self.clean_text(ciphertext)

        if not text:
            raise ValueError("Bản mã không được để trống.")

        if len(text) % 2 != 0:
            raise ValueError("Bản mã PlayFair phải có số ký tự chẵn.")

        return text

    def encrypt(self, plaintext: str) -> str:
        text = self.prepare_plaintext(plaintext)
        result = []

        for i in range(0, len(text), 2):
            a = text[i]
            b = text[i + 1]

            row_a, col_a = self.position[a]
            row_b, col_b = self.position[b]

            if row_a == row_b:
                result.append(self.matrix[row_a][(col_a + 1) % 5])
                result.append(self.matrix[row_b][(col_b + 1) % 5])
            elif col_a == col_b:
                result.append(self.matrix[(row_a + 1) % 5][col_a])
                result.append(self.matrix[(row_b + 1) % 5][col_b])
            else:
                result.append(self.matrix[row_a][col_b])
                result.append(self.matrix[row_b][col_a])

        return "".join(result)

    def decrypt(self, ciphertext: str) -> str:
        text = self.prepare_ciphertext(ciphertext)
        result = []

        for i in range(0, len(text), 2):
            a = text[i]
            b = text[i + 1]

            row_a, col_a = self.position[a]
            row_b, col_b = self.position[b]

            if row_a == row_b:
                result.append(self.matrix[row_a][(col_a - 1) % 5])
                result.append(self.matrix[row_b][(col_b - 1) % 5])
            elif col_a == col_b:
                result.append(self.matrix[(row_a - 1) % 5][col_a])
                result.append(self.matrix[(row_b - 1) % 5][col_b])
            else:
                result.append(self.matrix[row_a][col_b])
                result.append(self.matrix[row_b][col_a])

        return "".join(result)

    def matrix_to_text(self) -> str:
        return "\n".join(" ".join(row) for row in self.matrix)
