from ArabicOcr import arabicocr
import os


class OCR:
    def __init__(self):
        self.image = ""

    def get_info(self):
        out_image = 'outputs/output_image.jpg'
        results = arabicocr.arabic_ocr(self.image, out_image)
        print(results)
        words = []
        transcription = ""
        for i in range(len(results)):
            word = results[i][1]
            words.append(word)
            transcription += word + " / "
        with open('outputs/file.txt', 'r+', encoding='utf-8')as myfile:
            myfile.seek(0, os.SEEK_END)
            myfile.write("\n--------------- New CIN ------------------\n")
            for word in words:
                myfile.write(f"\n -> {word}")
        return transcription
