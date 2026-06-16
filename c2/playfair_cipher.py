import sys
import requests
from PyQt5 import QtWidgets

from ui.playfair import Ui_MainWindow

API_URL = "http://127.0.0.1:5000/api/playfair"


class PlayFairWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)
        self.ui.btn_matrix.clicked.connect(self.call_api_matrix)
        self.ui.btn_clear.clicked.connect(self.clear_data)

        self.statusBar().showMessage("Ready")
        self.call_api_matrix()

    def post_api(self, endpoint: str, payload: dict):
        try:
            response = requests.post(
                f"{API_URL}/{endpoint}",
                json=payload,
                timeout=5
            )

            data = response.json()

            if not data.get("success"):
                raise Exception(data.get("error", "Unknown error"))

            return data
        except requests.exceptions.ConnectionError:
            raise Exception("Không kết nối được API. Hãy chạy file api.py trước.")
        except Exception as error:
            raise Exception(str(error))

    def call_api_encrypt(self):
        try:
            payload = {
                "key": self.ui.txt_key.text(),
                "plaintext": self.ui.txt_input.toPlainText()
            }

            data = self.post_api("encrypt", payload)

            self.ui.txt_output.setPlainText(data["ciphertext"])
            self.ui.txt_matrix.setPlainText(data["matrix"])
            self.statusBar().showMessage("Encrypt success")
        except Exception as error:
            QtWidgets.QMessageBox.warning(self, "Encrypt error", str(error))

    def call_api_decrypt(self):
        try:
            payload = {
                "key": self.ui.txt_key.text(),
                "ciphertext": self.ui.txt_input.toPlainText()
            }

            data = self.post_api("decrypt", payload)

            self.ui.txt_output.setPlainText(data["plaintext"])
            self.ui.txt_matrix.setPlainText(data["matrix"])
            self.statusBar().showMessage("Decrypt success")
        except Exception as error:
            QtWidgets.QMessageBox.warning(self, "Decrypt error", str(error))

    def call_api_matrix(self):
        try:
            payload = {
                "key": self.ui.txt_key.text()
            }

            data = self.post_api("matrix", payload)

            self.ui.txt_matrix.setPlainText(data["matrix"])
            self.statusBar().showMessage("Matrix generated")
        except Exception:
            # Khi API chưa chạy, không hiện popup lúc mở chương trình.
            self.statusBar().showMessage("API is not running")

    def clear_data(self):
        self.ui.txt_input.clear()
        self.ui.txt_output.clear()
        self.ui.txt_matrix.clear()
        self.statusBar().showMessage("Cleared")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PlayFairWindow()
    window.show()
    sys.exit(app.exec_())
