import cv2
import os

def lsb1_stegano(image_path, message):
    image_array = cv2.imread(image_path)
    print(image_array)
    # rendre image pair
    image_array = image_array - image_array % 2
    # convertir message en binaire
    binary_message = ''.join(format(ord(carac), '08b') for carac in message)

    # if len(binary_message) > image_array.size():
        # raise Exception("taille de message supérieur aux nombres de pixels de l'image")

    nb_rows, nb_cols, nb_canals = image_array.shape
    index_binary_message = 0 
    for index_row in range(nb_rows):
        for index_col in range(nb_cols):
            for index_canals in range(nb_canals):
                if index_binary_message < len(binary_message):
                    image_array[index_row, index_col, index_canals] += int(binary_message[index_binary_message])
                    index_binary_message += 1
                else:
                    break
    
    cv2.imwrite("../watermarked_coruscant.jpg", image_array)
    cv2.imshow("", image_array)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
def lsb1_extract_message(watermarked_image_path):
    watermarked_image = cv2.imread(watermarked_image_path)
    binary_array_message = watermarked_image % 2
    nb_rows, nb_cols, nb_canals = binary_array_message.shape

    binary_message_list = []

    for index_row in range(nb_rows):
        for index_col in range(nb_cols):
            for index_canals in range(nb_canals):
                # flatten le message
                binary_message_list.append(str(binary_array_message[index_row, index_col, index_canals]))
# coupe les 8 0 consécutif
    # print(binary_message_list)
    # print("_"*80)
    for index_binary_char in range(0, nb_rows*nb_cols*nb_canals, 8):
        if binary_message_list[index_binary_char : index_binary_char+8] == ["0"] * 8:
            binary_message_list = binary_message_list[ : index_binary_char]
            break
    # print(binary_message_list)

    binary_message = "".join(binary_message_list)
    message = "".join([chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8)])
    print(message)


# if __name__ == "__main__":
path = "../coruscant.jpg"
lsb1_stegano(path, "Coucou les loulous")
lsb1_extract_message("../watermarked_coruscant.jpg")
    