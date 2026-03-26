import base64

def encrypt(data, attributes):
    encoded = base64.b64encode(data.encode()).decode()
    return f"{encoded}::{'|'.join(attributes)}"

def decrypt(cipher_text, user_attributes):
    try:
        encoded, attrs = cipher_text.split("::")
        required_attrs = attrs.split("|")

        if all(attr in user_attributes for attr in required_attrs):
            return base64.b64decode(encoded.encode()).decode()
        else:
            return "Access Denied: Attributes mismatch"
    except:
        return "Decryption Error"
