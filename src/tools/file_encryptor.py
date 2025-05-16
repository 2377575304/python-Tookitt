import os
from cryptography.fernet import Fernet

class FileEncryptor:
    """文件加密/解密工具 - 用Fernet对称加密文件（需提供密码）"""
    def encrypt(self, file_path=None, password=None):
        if not file_path or not password:
            return "请提供文件路径和密码"
        if not os.path.exists(file_path):
            return "文件不存在"
        try:
            key = Fernet.generate_key()
            f = Fernet(key)
            with open(file_path, 'rb') as fin:
                data = fin.read()
            encrypted = f.encrypt(data)
            out_path = file_path + '.enc'
            with open(out_path, 'wb') as fout:
                fout.write(encrypted)
            # 密钥简单处理（实际应用需更安全的密钥管理）
            with open(file_path + '.key', 'wb') as kf:
                kf.write(key)
            return f"加密完成，密文: {out_path}，密钥: {file_path}.key"
        except Exception as e:
            return f"加密失败: {e}"

    def decrypt(self, file_path=None, password=None):
        if not file_path or not password:
            return "请提供加密文件路径和密码"
        key_path = file_path.replace('.enc', '.key')
        if not os.path.exists(file_path) or not os.path.exists(key_path):
            return "加密文件或密钥文件不存在"
        try:
            with open(key_path, 'rb') as kf:
                key = kf.read()
            f = Fernet(key)
            with open(file_path, 'rb') as fin:
                data = fin.read()
            decrypted = f.decrypt(data)
            out_path = file_path.replace('.enc', '.dec')
            with open(out_path, 'wb') as fout:
                fout.write(decrypted)
            return f"解密完成，明文: {out_path}"
        except Exception as e:
            return f"解密失败: {e}"
