import cv2
import os

def lsb1_stegano(image_path, message):
    image_array = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    print(image_array)
    # rendre image pair
    image_array = image_array - image_array % 2
    # convertir message en binaire
    binary_message = ''.join(format(ord(carac), '08b') for carac in message)

    if len(binary_message) > image_array.size():
        raise Exception("taille de message supérieur aux nombres de pixels de l'image")

    nb_rows, nb_cols = image_array.shape
    print()
    for index_row in range(nb_rows):
        for index_col in range(nb_cols):
            print(index_row * nb_cols + index_col)
            if(index_row * nb_cols + index_col < len(binary_message)):
                image_array[index_row, index_col] += int(binary_message[index_row * nb_cols + index_col])
            else:
                break
    
    cv2.imshow("", image_array)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

# if __name__ == "__main__":
path = "../coruscant.jpg"
lsb1_stegano(path, "bonjour les gens")
    