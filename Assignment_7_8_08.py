def decode_message(encoded_message):
    def decode_helper(s, current_decoding, result):
        if not s:
            result.append(current_decoding)
            return
        # One digit decoding
        if 1 <= int(s[0]) <= 9:
            decode_helper(s[1:], current_decoding + chr(int(s[0]) + 64), result)
        # Two digit decoding
        if len(s) > 1 and 10 <= int(s[:2]) <= 26:
            decode_helper(s[2:], current_decoding + chr(int(s[:2]) + 64), result)

    result = []
    decode_helper(encoded_message, "", result)
    return result

encoded_message = input("Enter an encoded message: ")
decoded = decode_message(encoded_message)
print("Possible decoded messages:", decoded)
